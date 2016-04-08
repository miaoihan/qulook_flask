# coding:utf8
from app import app

#  必须加秘钥 不然session不工作
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/qulookdb'

