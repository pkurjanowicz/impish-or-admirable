from flask import Flask, request, redirect, render_template
import random
import os

app = Flask(__name__)
# app.config["CACHE_TYPE"] = "null"
app.config['DEBUG'] = False

@app.route('/')
def my_form():
    return render_template('doc.html')

@app.route('/find_out')
def find_out():
    list_1 = [render_template('impish.html', title='Impish'),render_template('admirable.html', title='Admirable')]
    return list_1[random.randint(0,1)]
    
# app.listen(process.env.PORT || 3000, function(){
# console.log("Express server listening on port %d in %s mode", this.address().port, app.settings.env);
# });
app.run()

