from app import app
from flask import render_template, request, send_file
from app import insertDB
import csv

@app.route('/', methods=["POST","GET"])
def home():
   if request.method == "POST":
      email = request.form["email"]
      name = request.form["name"]
      betreff = request.form["betreff"]
      text = request.form["message"]
      print(name)
      print(betreff)
      print(text)
      print(email)
      insertDB.add_Nachricht(name, email, betreff, text)
      f = open("Backup.csv", "w")
      write = csv.writer(f, delimiter=";")

      insert = [name, email, betreff, text]
      write.writerow(insert)
      f.close()

   return render_template('index.html') 

@app.route('/#about_me')
def about():
   return render_template('index.html#about_me')

@app.route('/#skills')
def skills():
   return render_template('index.html#skills')

@app.route('/#contact_me')
def contact():
   return render_template('index.html#contact_me')


@app.route('/projects')
def projects():
   return render_template('projects.html') 

@app.route('/projects/homeserver')
def homeserver():
   return render_template('homeserver.html')



@app.route('/download_file')
def download_file():
   path = "Examples.pdf"
   return send_file(path, as_attachment=True)
