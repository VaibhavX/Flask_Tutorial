from app import app, db #db added for Flask Shell
from app.models import User, Post #Model Instance Added for Flask Shell

@app.shell_context_processor #Decorator register this function as a shell context fn
def make_shell_context():
    return {'db': db, 'User': User, 'Post' : Post}
