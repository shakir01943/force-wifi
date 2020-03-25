from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def ihdex():
    return render_template('index.html')

@app.route("/", methods=["POST"])

def gv():
    n1 = request.form['fname']
    n2 = request.form['lname']
    print(n1,n2)
    return render_template('pass.html', s = n1, v = n2)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)