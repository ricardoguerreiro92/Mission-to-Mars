from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import Mission_to_Mars_Challenge

app = Flask(__name__)

#use flask_pymongo to set up mongo connection
app.config["MONGO_URI"]= "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#route for our index page
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

#route for scrape button
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   #variable holding newly scraped data
   mars_data = Mission_to_Mars_Challenge.scrape_all()
   #Next, we'll use the data we have stored in mars_data. The syntax used here is {"$set": data}. This means that the document will be modified ("$set") with the data in question.
   #Finally, the option we'll include is upsert=True. This indicates to Mongo to create a new document if one doesn't already exist, and new data will always be saved (even if we haven't already created a document for it).
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   #this will redirect the page to the main page
   return redirect("/", code=302)

if __name__ == "__main__":
   app.run()
