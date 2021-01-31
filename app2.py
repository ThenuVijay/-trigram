from flask import *
import sqlite3


app=Flask(__name__)           

@app.route('/')
def index():
    return render_template("home1.html")



@app.route('/', methods=["GET","POST"])
def home():
    if request.method == "POST":
        text=request.form['u']
        connection = sqlite3.connect("C:\\Users\\User\\Desktop\\python practice\\resultnew.db")
        print("Database opened successfully")
        if request.form.get("Word Suggestion"):
            con=sqlite3.connect("resultnew.db")
            cur=con.cursor()
            cur.execute("SELECT field2,field3 from trigram where field1=:text",{"text":text})
            out=cur.fetchall()
            Out1=""
            for i in out:
                data=i
                Out1=Out1+text
                for m in range(0,len(data)):
                    Out1=Out1+" "+data[m]+""
                Out1=Out1+"\n"   
        if Out1=="":
            Out1="Word is not in DB"
              
    return render_template("home1.html",out=Out1)
   


if __name__ == '__main__':
    app.run()
