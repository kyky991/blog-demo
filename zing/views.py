#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from manager import app
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_required, login_user, logout_user, current_user
from .models import User, Permission, Post
from .forms import LoginForm, PostForm
from datetime import datetime
from . import db


@app.route('/', methods=['GET', 'POST'])
def index():
	form = PostForm()
	if current_user.can(Permission.WRITE_ARTICLES) and form.validate_on_submit():
		post = Post(body=form.body.data, author=current_user._get_current_object())
		db.session.add(post)
		db.session.commit()
		return redirect(url_for('index'))
	posts = Post.query.order_by(Post.timestamp.desc()).all()
	return render_template('index.html', Permission=Permission, current_time=datetime.utcnow(), form=form, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.remember_me.data)
			return redirect(request.args.get('next') or url_for('index'))
		flash('Invalid username or password.')
	return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have been logged out.')
	return redirect(url_for('index'))


#@app.before_app_request	
#def before_request():
#	if current_user.is_authenticated:
#		current_user.ping()
#		if not current_user.confirmed


@app.route('/user/<username>')
def user(username):
	user = User.query.filter_by(username=username).first()
	if user is None:
		abort(404)
	return render_template('user.html', user=user)


@app.route('/secret')
@login_required
def secret():
	return 'authenticated users only'


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500
