from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def todolist():
    list = ()
    if len(list) > 0:
        return render_template('todo.html', list=list)
    else:
        return render_template('todo.html')


@app.route('/submit', methods = ['POST'])
def sumbit():
    email = request.form['email']
    task = request.form['task']
    priority = request.form['priority']
    todolist.list = (email + '' + task + '' + priority )
    return 'Added Item'


@app.route('/clear', methods = ['POST'])
def clear():
    return redirect ('/')


if __name__ == '__main__':
    app.run()