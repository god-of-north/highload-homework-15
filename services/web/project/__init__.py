from flask import Flask
import os
import  json
from time import sleep
from datetime import datetime
import mysql.connector
from .generator import Generator
import threading


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

@app.route("/test")
def test():
    global g_db
    if g_db == None or not g_db.is_connected():
        g_db = mysql.connector.connect(host="db", user="root", password="root", database="db")

    gen = Generator()
    user = gen.generate_user()

    sql = "INSERT INTO users (birth_day,registration_date,user_login,user_email,firstname,surname,patronymic,sex,job_position,description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (user["birth"], user["reg"], user["login"], user["mail"], user["name"], user["surname"], user["patronymic"], user["sex"], user["job"], user["descr"])

    cursor = g_db.cursor()
    cursor.execute(sql, val)
    g_db.commit()

    return "OK"

@app.route("/slow")
def slow_query():
    with mysql.connector.connect(host="db", user="root", password="root", database="db") as db:
        sql = "select count(*) from users;"
        cursor = db.cursor()
        cursor.execute(sql, val)
