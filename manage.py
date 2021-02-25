import os
import unittest
from dotenv import load_dotenv

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_cors import CORS

from app.main import create_app, db
from app.main.model import user, blacklist, blog, comments, products
from app import blueprint

load_dotenv('.env')
app = create_app('dev')
app.register_blueprint(blueprint)
CORS(app, support_credentials=True)
app.config["API_ENVIRONMENT"] = "sandbox"  # sandbox or live
app.config["APP_KEY"] = "AofMYItO2UcRTan0OoaW8DsQTViSXnZ9"  # App_key from developers portal
app.config["APP_SECRET"] = "WJz6uVZUeeymoJAQ"  # App_Secret from developers portal
app.run(threaded=True)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Runs the unit tests. """
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
