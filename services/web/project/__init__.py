from flask import Flask
import os
import  json
from time import sleep
from datetime import datetime
import mysql.connector
from .generator import Generator
import threading
from random import randint

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello"

def generate(count:int):
    with mysql.connector.connect(host="db", user="root", password="root", database="db") as db:
        gen = Generator()
        n = 1
        for i in range(count):
            user = gen.generate_user()

            sql = "INSERT INTO users (birth_day,registration_date,user_login,user_email,firstname,surname,patronymic,sex,job_position,description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (user["birth"], user["reg"], user["login"], user["mail"], user["name"], user["surname"], user["patronymic"], user["sex"], user["job"], user["descr"])

            cursor = db.cursor()
            cursor.execute(sql, val)

            if(int(i/1000) == n):
                n = n+1
                db.commit()
        db.commit()

@app.route("/add/<count>")
def add_user(count):
    count = int(count)
    if(count>1):
        r = threading.Thread(name='gen', target=lambda: generate(count))
        r.start()
    else:
        generate(1)
    return "OK"

g_db = None

@app.route("/slow")
def slow_query():
    with mysql.connector.connect(host="db", user="root", password="root", database="db") as db:
        sql = [ 
               "select * from users  Limit 900000;",
               "select * from users  Limit 1100000;",
               "select * from users  Limit 1500000;",
              ]
        cursor = db.cursor()
        cursor.execute(sql[randint(0, len(sql)-1)])
    return 'OK'
