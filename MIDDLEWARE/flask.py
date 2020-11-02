from flask import Flask, render_template,redirect,url_for,request
import os



app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/submit",methods=['POST'])
def submit():
    if request.method == 'POST':
        return os.system('pyt.py')



if __name__ == "__main__":
    app.run(debug=True)
