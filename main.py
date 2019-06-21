from flask import Flask, request, render_template, redirect
import random

app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"
app.config['DEBUG'] = True

def rotator():
    rotate_list = ["Impish", "Admirable"]
    return rotate_list[random.randint(0,1)]

page2 = '''
<html>
<head>
    <link rel="stylesheet" href="static/styles.css" type="text/css">
</head>
<title></title>
<body>
    <main>
        <h1>Impish or Admirable</h1>
        <div id="dwight"></div>
        <h2>You have been {0}!!!!!</h2>
    </main>
    <article></article>
</body>
</html>'''.format(rotator())

@app.route('/')
def my_form():
    return render_template('doc.html')

@app.route('/find_out')
def find_out():
    return page2

app.run()