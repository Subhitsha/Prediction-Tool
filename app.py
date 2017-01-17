from flask import Flask, flash, jsonify, request, redirect, url_for
from flask_restful import Api, Resource
from flask import g, render_template
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)


@app.route('/')
def get_home():
	return render_template('load.html')


@app.route('/login')
def get_login():
	return render_template('login.html')

@app.route('/prepare')
def get_prepare():
	return render_template('prepare.html')

@app.route('/train')
def get_train():
	return render_template('train.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
