#!/usr/bin/python
# coding=utf-8
from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from .model import User


class QuestionForm(Form):
    # email = StringField('Email', validators=[Required(), Length(1, 64),
    #                     Email()])
    # password = PasswordField('Password', validators=[Required()])
    question = StringField(u'问题', validators=[DataRequired(message=u'不能是空的哦'), Length(4, 60, message=u'长度在4-60之间')])
    author = StringField(u'作者', validators=[DataRequired()])
    answer = TextAreaField(u'回答', validators=[DataRequired()])
    submit = SubmitField(u'提问')


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField(u'记住我')
    submit = SubmitField(u'登录')


class RegistrationForm(Form):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                              'Usernames must have only letters, '
                                              'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
