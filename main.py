from flask import (
    Flask, 
    request,
    render_template,
)


app = Flask(__name__)
json_users={
    "vladimir":"pastykhanov",
    "elena":"slanikova",
    "alexey":"yanyk",
    "ivan":"samsonov"
}
posts=[]
post={}

@app.route("/", methods=["GET", "POST"])
def login_in():
    alert = None
    global login
    if request.method == "POST":
        
        login = request.form.get("log")
        passw = request.form.get("pass")
        for i in json_users:
            if login == i and passw == json_users[i]:
                return render_template("index2.html", posts=posts)
        

        alert="Wrong login or password!"
        return render_template("index.html", error=alert)
       
    
    return render_template("index.html")
    
@app.route("/posts", methods=["GET", "POST"])
def write_post():
    global post
    global posts
    global login
    user=f"Написал {login}"
    text=request.form.get("comment")
    print(text)
    if text != "":
        post={"user":user, "text":text}
        posts.insert(0,post)
        return render_template("index2.html", posts=posts)   
    else:
        return render_template("index2.html" , posts =posts)


if __name__ == '__main__':
    app.run(debug=True, port=8007)