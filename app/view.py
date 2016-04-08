#!/usr/bin/python
# coding=utf-8
from flask.ext.login import login_user

from app import app, db
from flask import render_template, request, url_for, redirect, flash
from .model import Question, User
from .forms import QuestionForm, LoginForm


@app.route('/')
def home():
    #主页动态
    questions = Question.query.filter_by(del_status=1).order_by('created_time DESC')
    form = QuestionForm()
    return render_template('index.html', questions=questions, form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect('/')
        flash('Invalid username or password.')
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'han' and password == '1234':
            return redirect(url_for('home'))
        else:
            return render_template('register.html')
    return render_template('register.html')


@app.route('/questions')
def show_question():
    questions = Question.query.filter_by(del_status=1)
    return render_template('show_question.html', questions=questions)


@app.route('/new_question', methods=['GET', 'POST'])
def new_question():
    form = QuestionForm()
    if form.validate_on_submit():
        question_id = request.form['question_id']
        # session['question_id'] = request.form['question_id']
        # question_id = session.get('question_id')
        # return '<script>alert("OK!")</script>'
        # if not question_id:
        #     question = Question(question=form.question.data,
        #                         author=form.author.data,
        #                         answer=form.answer.data)
        question = Question(id=question_id,
                            question=form.question.data,
                            author=form.author.data,
                            answer=form.answer.data)
        db.session.merge(question)
        db.session.commit()
        # flash('保存成功')
        return redirect(url_for('home'))
    # 校验不通过时把id值传过去，防止merge失效
    if request.method == 'POST':
        question_id = request.form['question_id']
        return render_template('new_question.html', form=form, question_id=question_id)
    return render_template('new_question.html', form=form)


@app.route('/edit_question/<question_id>', methods=['GET', 'POST'])
def edit_question(question_id):
    # print(question_id)
    question = Question.query.get_or_404(question_id)
    form = QuestionForm()
    # 设置编辑传过去的值
    form.question.data = question.question
    form.author.data = question.author
    form.answer.data = question.answer
    return render_template('new_question.html', form=form, question_id=question_id)


@app.route('/del_question/<question_id>')
def del_question(question_id):
    question = Question.query.get_or_404(question_id)
    question.del_status = 0
    db.session.commit()
    return redirect(url_for('show_question'))
