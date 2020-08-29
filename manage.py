import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_cors import CORS

from app.main import create_app, db
from app.main.model import user, blacklist, blog, comments, products
from app import blueprint

app = create_app(os.getenv('BOILERPLATE_ENV') or 'prod')
app.register_blueprint(blueprint)
CORS(app, support_credentials=True)


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
