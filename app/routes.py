from flask import Blueprint, render_template, request, redirect
from models import Task
from database import db

bp = Blueprint("main", __name__)


# 📌 READ — показать все задачи
@bp.route("/")
def index():
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)


# 📌 CREATE — добавить задачу
@bp.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")

    if title:
        new_task = Task(title=title)
        db.session.add(new_task)
        db.session.commit()

    return redirect("/")


# 📌 UPDATE — отметить выполненной
@bp.route("/complete/<int:id>")
def complete(id):
    task = Task.query.get(id)
    if task:
        task.completed = True
        db.session.commit()

    return redirect("/")


# 📌 DELETE — удалить задачу
@bp.route("/delete/<int:id>")
def delete(id):
    task = Task.query.get(id)
    if task:
        db.session.delete(task)
        db.session.commit()

    return redirect("/")