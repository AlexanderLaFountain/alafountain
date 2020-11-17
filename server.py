# cd Projects\WebDevelopment
# .\Scripts\activate
# deactivate

# $env:FLASK_APP = "server.py" 
# $env:FLASK_ENV='development' # changes env to development and allows debugging; changes things with refresh 
# flask run

# .js and .css must be placed in static folder

## Portfolio Website

from flask import Flask, render_template, request, redirect
import csv 

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html') # put all files into a template folder; render_template points there

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_database_txt(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')
        return file

def write_to_database_csv(data):
    with open('database.csv', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
        return csv_writer

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # print(data)
            write_to_database_csv(data)
            return redirect('/submission_page.html')
        except:
            return 'Something went wrong! Did not save to database!'
    else:
        return 'Something went wrong! Try again!'

