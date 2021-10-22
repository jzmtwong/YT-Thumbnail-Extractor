# Import Dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_yt import yt_extract

# instance of flask app
app = Flask(__name__)

# flask/ pymongo connection
app.config["MONGO_URI"] = 'mongodb://localhost:27017/YT_EXTR'
mongo = PyMongo(app)


# Create route for index.html template
@app.route("/", methods=['POST','GET'])
def home():
   return render_template('index.html')
   img_url = yt_extract(yt_url)

   #return index template and img url
   return index tempalte("index.html",

if __name__ == "__main__":
    app.run(debug=True)