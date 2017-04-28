from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def todolist():
    list = [('do something', 'email', 'privu')]
    return render_template('todo.html', list=list)


# @app.route('/submit', methods = ['POST'])
# def sumbit():
#     email = request.form['email']
#     task = request.form['task']
#     priority = request.form['priority']
#     todolist.list = (email + '' + task + '' + priority )
#     return 'Added Item'


@app.route('/clear', methods = ['POST'])
def clear():
    return redirect ('/')


if __name__ == '__main__':
    app.run()