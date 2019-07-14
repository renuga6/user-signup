from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True
form = """
<!doctype html>
<html>
    <head>
<style>
    .error {{ color:red;}}
</style>
</head>
</body>
<h1> Sign Up </h1>
<form  method = 'POST'>
    <label> Username: </label>
    <input type ="text" name="usern"  >
     <p class="error">{1} </p>
     <p class="error">{5} </p>
    <br>
    <label> Password: </label>
    <input type ="password" name ="pwd" >
    <p class="error">{2} </p> 
    <br>
    <label> Verify Password: </label>
    <input type = "password" name = "vpwd" >
    <p class="error">{3} </p>
    <br>
    <p class="error">{0} </p>
    <label> Email id (optional) </label>
    <input type = "text" name ="email" >
    <br>
    <p class="error">{4} </p>
    <label> Submit </label>
    <input type = "submit" value ="submit">
    </form>
    </body>
    </html>"""

@app.route("/")
def index():
   return form.format("","","","","","")
   
@app.route("/",methods = ["POST"])   
def validation():
    if request.method == 'POST':
        vusern = request.form['usern']  
        vpswd = request.form['pwd'] 
        vvpswd = request.form['vpwd']
        vemailid = request.form['email']
    generalresult = "" 
    usernameresult = "" 
    passwordresult = ""
    veripasswordresult = ""
    veriemailresult = ""
    hellostr = ""
    spaceinusnresult =""
    if vusern == "" or vpswd == "" or vvpswd == "":
        generalresult = "enter values" 
    elif " " in vusern  or " "  in vpswd:
        spaceinusnresult = "No space allowed in user name and in password"    
    elif len(vusern) < 3 or len(vusern) > 20 :
        usernameresult = "enter values more than 3 and less than 20"
    elif len(vpswd) <3 or len(vpswd) > 20:
        passwordresult = "enter values more than 3 and less than 20"
    elif vpswd != vvpswd:
        veripasswordresult = "does not match" 
    elif  "@" not in vemailid or "." not in vemailid:
        veriemailresult = "Invalid email id" 
    if generalresult == "" and usernameresult =="" and passwordresult=="" and veripasswordresult=="" and veriemailresult=="" and spaceinusnresult=="":
        hellostr = "Hello"
        return "<h1>" + hellostr + " " + vusern + "</h1>"
    else:    
        return form.format(generalresult,usernameresult,passwordresult ,veripasswordresult,veriemailresult,spaceinusnresult)       
app.run()        