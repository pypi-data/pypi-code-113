from qplay_cli.user.user import User
import click
import getpass

@click.group()
def user():
    pass

@user.command()
def signup():
    print("Enter your username:")
    username = input()
    
    print("Enter email address:")
    email = input()
    
    print("Enter your name:")
    name = input()
    
    p = getpass.getpass()
    
    response = User().signup(username, name, email, p)
    print(response['message'])
    
    print("Enter verification code")
    code = input()
    response = User().confirm_signup(username, name, code)
    print(response['message'])
    
    User().signin(username, p)
    
 
@user.command() 
def signin():
    print("Enter your username:")
    username = input()
    
    password = getpass.getpass()
    User().signin(username, password)
    print("Sign in sucessfull")