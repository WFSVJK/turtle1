from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/')
def vjk_hello ():
    print ("vijay's website")
    return ("Successful")
     
@app.route('/page1')
def vjk_page1 ():
    return ("Now we are in Page")
app.run()
