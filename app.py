from flask import render_template
from flask import Flask
#-import db
from flask import request
from keywordfind import *
#import search
#import requests
app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sellers.html')
def sellers():
    return render_template('sellers.html')
@app.route('/food.html')
def food():
    return render_template('food.html')

@app.route("/admin")
def admin():
    print("Admin Panel verification.")
    print("Retaining request until verified.")
    u = input("Do you allow this request? (y)es or (n)o ->")
    if u == "y":
        print("Request accepted, rendering.")
        return render_template("adminaccess.html")
    else:
        print("Request denied.")
        reason = input("Reason ->")
        if reason == "":
            return("6909 - uwuDenied")
        else:
            return(reason)
@app.route('/access', methods=['GET', 'POST'])
def access():
    print("-")

@app.route("/buyers.html", methods=["GET", "POST"])
def buyers():
    print("Buyers Access")
    return render_template("buyers.html")

@app.route("/index.php", methods=["GET", "POST"])
def indexphp():
    print("index.php")
    return render_template("index.php")
@app.route("/token_generator.php")
def tkngen():
    return render_template("token_generator.php")
@app.route("/script.js")
def scriptjs():
    return render_template("script.js")
@app.route('/submit', methods=['POST'])
def submit():
    print("access")
    ret = request.form['ret']
    print(ret)
    keys = get_keywords(ret)
    print(keys)
    return render_template('submit.html', keys=keys)

@app.route("/keyword.html")
def keywordtester():
    return render_template("keyword.html")
@app.route('/robots.txt', methods=['GET', 'POST'])
def robots():
    print("ROBOT -------- robots.txt")
    return render_template('robots.txt')

@app.route('/title/<title>')
def searchByTitle(title):
    return search.searchByTitle(title)

@app.route('/keyword/<keyword>')
def searchByKeyword(keyword):
    return search.searchByKeyword(keyword)

    
@app.route('/<name>/<quantity>/<comments>/<status>')
def handle_order(name, quantity, comments, status):
    db.add_order(name, quantity, comments, status)

#using only first letters for readability
@app.route('/<n>/<d>/<p>/<z>/<q>/<s>/<e>/<k>/<i>')
def handle_food(n, d, p, z, q, s, e, k, i):
    db.add_food(n, d, p, z, q, s, e, k, i)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    #http://5.225.9.35/
# pretty basic