import json
import requests
import mysql.connector
import sys
from flask import Flask, request, jsonify
from flags import flags
from decouple import config

app = Flask(__name__)

# Mysql connection settings
mydb = mysql.connector.connect(
    host=config("DB_HOST"),
    user=config("DB_USER"),
    password=config("DB_PASS"),
    database=config("DB_NAME"),
)

# Helper method to populate both HN tables
def getHNPosts():
    response = requests.get("https://hacker-news.firebaseio.com/v0/showstories.json")
    data = response.json()
    # print(data)
    for post in data:
        postResponse = requests.get(
            "https://hacker-news.firebaseio.com/v0/item/{0}.json".format(post)
        )
        postData = postResponse.json()
        # print(postData["by"])

        mycursor = mydb.cursor()

        sql = "INSERT INTO hn_posts_score (id, author, title, score, url, descendants) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (
            postData["id"],
            postData["by"],
            postData["title"],
            postData["score"],
            postData["url"],
            postData["descendants"],
        )
        # sql = "INSERT INTO hn_posts_no_score (id, author, title, url, descendants) VALUES (%s, %s, %s, %s, %s)"
        # val = (postData["id"], postData["by"], postData["title"], postData["url"], postData["descendants"])
        mycursor.execute(sql, val)

        mydb.commit()

        sql = "INSERT INTO hn_posts_no_score (id, author, title, url, descendants) VALUES (%s, %s, %s, %s, %s)"
        val = (
            postData["id"],
            postData["by"],
            postData["title"],
            postData["url"],
            postData["descendants"],
        )

        mycursor.execute(sql, val)

        mydb.commit()


# Function that grabs posts from DB
def getDBPosts():
    mycursor = mydb.cursor()

    if flags.score.is_enabled():
        mycursor.execute(
            "SELECT id, author, title, score, url, descendants FROM hn_posts_score"
        )
    else:
        mycursor.execute(
            "SELECT id, author, title, url, descendants FROM hn_posts_no_score"
        )

    row_headers = [x[0] for x in mycursor.description]  # this will extract row headers
    myresult = mycursor.fetchall()
    json_data = []
    for result in myresult:
        json_data.append(dict(zip(row_headers, result)))

    return json_data


# Function that saves post updates to DB
def storeNewPost():
    mycursor = mydb.cursor()

    if flags.score.is_enabled():
        sql = "INSERT INTO hn_posts_score (id, author, title, score, url, descendants) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (
            postData["id"],
            postData["by"],
            postData["title"],
            postData["score"],
            postData["url"],
            postData["descendants"],
        )
    else:
        sql = "INSERT INTO hn_posts_no_score (id, author, title, url, descendants) VALUES (%s, %s, %s, %s, %s)"
        val = (
            postData["id"],
            postData["by"],
            postData["title"],
            postData["url"],
            postData["descendants"],
        )

    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


# Flask routing
@app.route("/", methods=["GET"])
def home():
    response = jsonify(getDBPosts())
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


# Flask routing
@app.route("/run-helper", methods=["GET"])
def runHelper():
    getHNPosts()


if __name__ == "__main__":
    app.run(debug=True)
