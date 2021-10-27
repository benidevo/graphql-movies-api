import os
from flask import Flask
from flask_migrate import Migrate
from flask_graphql import GraphQLView

from models.db import db
from controllers.schema import schema


# USERNAME = os.environ.get('USERNAME')
# PASSWORD = os.environ.get('PASSWORD')
# DB_NAME = os.environ.get('DB_NAME')

USERNAME='graph'
PASSWORD='postgres'
DB_NAME='graphql_flask'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{USERNAME}:{PASSWORD}@localhost:5432/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = os.environ.get('SECRET_KEY')

db.init_app(app)
migrate = Migrate(app, db)

@app.before_first_request
def create_tables():
    db.create_all()

app.add_url_rule(
    '/graphql/',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True,
    )
)

if __name__ == '__main__':
    app.run()
    