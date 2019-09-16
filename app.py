import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId



app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'My_Cocktails'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')


@app.route('/')
    def get_cocktails():
    return ('base.html')