from app import create_app,db
from app.models import User,Pitch,Comments
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

# We import the Manager class from flask-script that will initialize
# our extension and the Server class that helps us launch
# our application.

# Creating app instance 
app = create_app('production')


manager = Manager(app)
manager.add_command('server', Server)

@manager.shell
def make_shell_context():
    return dict(app=app,db= db,User=User,Pitch =Pitch,Comments=Comments)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    manager.run()
