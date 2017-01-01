#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField
from wtforms.validators import Required, Length, Email


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
	password = PasswordField('Password', validators=[Required()])
	remember_me = BooleanField('Keep me logged in')
	submit = SubmitField('Log In')


class PostForm(FlaskForm):
	body = TextAreaField("What's on your mind?", validators=[Required()])
	submit = SubmitField('Submit')

