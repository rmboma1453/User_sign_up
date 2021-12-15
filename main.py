from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too


#Route for the welcome page and error page
@app.route("/welcome", methods=['POST'])
def welcome():
    
    #creating variables to use for input requiremetns
    at = '@'
    point = '.'
    space = ' '
    
    #getting and assigning input for requests to variable
    username = request.form['username']
    password = request.form['password']
    confpassword = request.form['confpassword']
    email = request.form['email']
    
    #initializing all the error statements
    name_error =''
    pass_error =''
    confpass_error =''
    email_error =''
    
    # stating condition for inputs
    if username =='':
        name_error = 'You did not enter a username.'
        username =''
    elif space in username:
        name_error = 'Do not put space in your username.'
        username =''
    elif len(username) < 3:
        name_error = 'Username must have more than 3 letters.'
        username =''
    
    if password =='':
        pass_error = 'You did not enter a password.'
        password =''
    elif len(password) < 3:
        pass_error = 'Username must have more than 3 letters.'
        password =''
    elif space in password:
        pass_error = 'Do not put space in your password.'
        password ='' 
        confpass_error = ''
        confpassword = ''
    
    elif confpassword =='':
        confpass_error = 'You did not enter the confirmation password.'
        confpassword =''
    
    elif confpassword != password:
        confpass_error = 'The confirmatiom password does not match the password.'
        confpassword =''
    
    if email !='':
        if len(email) < 3:
            email_error = 'Your email must have more than 3 letters.'
            email =''
        elif len(email) > 20:
            email_error = 'Your email must have less than 20 letters.'
        else:
            if not at in email:
                email_error = 'You are missing -@- .'
                email =''
            elif not point in email:
                email_error = 'You are missing -.- .'
                email =''
    
    #Rendering a welcome page if none errors were found
    if (not name_error and not confpass_error) and (not pass_error and not email_error):
        username_bold = "<strong>" + username + "</strong>"
        sentence = "Welcome, " + username_bold
        content = "<p>" + sentence + "</p>"
        return content
    #Rendering a page with errors founds
    else:
        return render_template('edit.html', name_error = name_error, pass_error = pass_error, confpass_error = confpass_error,email_error = email_error, username = username, password = password, confpassword = confpassword, email = email)

@app.route("/")
def index():
    #Rendering the initial user sign up page
    return render_template('edit.html')
app.run()