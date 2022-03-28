from flask import * 
import requests
from bs4 import BeautifulSoup
import pyrebase
app = Flask(__name__)  

config = {
    "apiKey": "AIzaSyDNU26xF-_sFVVN0_2S3b-ozbfdrrojVEA",
 "authDomain": "hackathon-be0ca.firebaseapp.com",
  "projectId": "hackathon-be0ca",
  "storageBucket": "hackathon-be0ca.appspot.com",
  "messagingSenderId": "480402636484",
  "appId": "1:480402636484:web:169d12cff0d3d39af09391",
  "databaseURL" : "https://hackathon-be0ca-default-rtdb.asia-southeast1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


@app.route('/login',methods = ['POST'])  
def login():
    if request.method == 'POST':
        email = request.json['email']
        password = request.json['password']
        try:
            user = auth.sign_in_with_email_and_password(email,password)
            customer = db.child("users").child(user['localId']).get()
            typeofuser = customer.val()["type"]
            return {"auth":typeofuser}
        except:
            return {"auth" : False, "msg":"Invalid Credentials"}
    else:
        return {"auth":"Something is wrong"}



@app.route('/register', methods=['POST'])  
def register():
    if request.method == "POST":
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']
        type = request.json['type']
        try:
            user = auth.create_user_with_email_and_password(email,password)
            data = {
                "name":name,
                "email":email,
                "type":type,
                "score":0,
                "github":" ",
                "codechef":" ",
                "leetcode":" ",
                "upvotes":0,
                "downvotes":0

            }
            results = db.child("users").child(user['localId']).set(data)
            return {"auth" : True, "msg":'Thanks for registering with us.'}
        except Exception as e:
            return {"auth" : False, "msg":"Email ID already registered or passowrd is less than 6 characters"}
    else:
        return {"auth":False, "msg":"Something is wrong"}

@app.route('/submitlinks', methods=['POST'])  
def submitlinks():
    if request.method == "POST":
        email = request.json['email']
        github = request.json['github']
        codechef = request.json['codechef']
        leetcode = request.json['leetcode']
        r = requests.get(github)
        soup = BeautifulSoup(r.content, 'html5lib')
        table = soup.find('h2', attrs = {"class":"f4 text-normal mb-2"})
        commits = (table.text).split('\n')
        commits = commits[1].strip()
        table = soup.find('span', attrs = {"class":"Counter"})
        repos = table.text
        r = requests.get(codechef)
        soup = BeautifulSoup(r.content, 'html5lib')
        table = soup.find('strong', attrs = {"class":"global-rank"})
        codechefglobalrank = table.text
        r = requests.get(leetcode)
        soup = BeautifulSoup(r.content, 'html5lib')
        table = soup.find_all(class_ = "stat")
        globalrank = table[10].text
        codewarsglobalrank = ((globalrank.split("Leaderboard Position:"))[1].split("#"))[1]
        print(repos, codechefglobalrank, codewarsglobalrank)
        try:
            users = db.child("users").get()
            users = users.val()
            for i in users:
                foundemail = db.child("users").child(i).child("email").get()
                foundemail = foundemail.val()
                if foundemail == email:
                    user = i
            print(user)
            result = db.child("users").child(str(user)).get()
            result = result.val()
            print(result)
            result['github'] = github
            result['codechef'] = codechef
            result['leetcode'] = leetcode
            data = {
                "name" : (db.child("users").child(str(user)).child("name").get()).val(),
                "email" : (db.child("users").child(str(user)).child("email").get()).val(),
                "type" : (db.child("users").child(str(user)).child("type").get()).val(),
                "github": github,
                "codechef":codechef,
                "leetcode":leetcode,
                "score":(db.child("users").child(str(user)).child("score").get()).val(),
                "upvotes":(db.child("users").child(str(user)).child("upvotes").get()).val(),
                "downvotes":(db.child("users").child(str(user)).child("downvotes").get()).val()
            }
            print(data)
            db.child("users").child(str(user)).set(data)
            return {"auth":True}
        except:
            return {"auth":False}


@app.route('/getprofile', methods=['POST'])
def getprofile():
    if request.method == "POST":
        email = request.json['email']
        users = db.child("users").get()
        users = users.val()
        for i in users:
            foundemail = db.child("users").child(i).child("email").get()
            foundemail = foundemail.val()
            if foundemail == email:
                user = i
        try:
            if user:
                data = {
                "name" : (db.child("users").child(str(user)).child("name").get()).val(),
                "email" : (db.child("users").child(str(user)).child("email").get()).val(),
                "type" : (db.child("users").child(str(user)).child("type").get()).val(),
                "github": (db.child("users").child(str(user)).child("github").get()).val(),
                "codechef":(db.child("users").child(str(user)).child("codechef").get()).val(),
                "leetcode":(db.child("users").child(str(user)).child("leetcode").get()).val(),
                "score":(db.child("users").child(str(user)).child("score").get()).val(),
                "upvotes":(db.child("users").child(str(user)).child("upvotes").get()).val(),
                "downvotes":(db.child("users").child(str(user)).child("downvotes").get()).val()
                }
                return {"auth":True, "data":data}
        except:
            return {"auth":False, "data":"No user with these details found"}
        

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    results = db.child("users").get()
    results = results.val()
    for i in range(0, len(results)):
        for j in range(0, len(results)):
            if results[j]['score'] > results[j+1]['score']:
                results[j], results[j+1] = results[j+1], results[j]
    return {"auth":True, "data":results}









if __name__ == '__main__':  
   app.run(debug = True)  
