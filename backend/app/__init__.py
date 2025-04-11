from flask import Flask

app = Flask(__name__)  # This creates the Flask app instance

# Import routes AFTER creating app to avoid circular imports
from app.routes import api
app.register_blueprint(api)