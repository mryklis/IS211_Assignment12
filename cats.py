from flask import Flask, request, redirect, render_template

app = Flask(__name__)



@app.route('/')
def hello_world():
    author = "Me"
    name = "You"
    return render_template('index.html', author=author, name=name)

if __name__ == "__main__":
    app.run()


@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    print("The email address is '" + email + "'")
    return redirect('/')

if __name__ == '__main__':
    app.run()