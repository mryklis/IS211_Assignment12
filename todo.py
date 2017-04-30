from flask import Flask, request, redirect, render_template
import os.path
import re

app = Flask(__name__)

file_path = 'list.txt'
list_exist = os.path.isfile(file_path)

@app.route('/')
def todolist():
    todo = []
    if list_exist == True:
        f = open(file_path, 'r')
        todo = f.readlines()
        f.close()
        return render_template('todo.html', list=todo)
    else:
        todo = []
        return render_template('todo.html', list=todo)


@app.route('/submit', methods = ['POST'])
def sumbit():

    email = request.form['email']
    task = request.form['task']
    priority= request.form['priority']

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return redirect('/')
    elif str(priority) not in ("high", "medium", "low"):
        return redirect('/')
    else:
        with open(file_path, 'a') as f:
            f.write('{}, {}, {}'.format(task, email, priority))
            f.write('\n')
        return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():

    f = open(file_path, 'w')
    f.truncate()
    f.close()
    return redirect ('/')

@app.route('/save', methods=['POST'])
def save():
    if list_exist == True:
        return redirect('/')

if __name__ == '__main__':
    app.run()