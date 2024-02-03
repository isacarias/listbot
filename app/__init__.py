from flask import Flask
from slack_sdk import WebClient
from os import environ

def create_app():
    # Initialize the Flask application
    app = Flask(__name__)

    # Load the SLACK_TOKEN from environment variables
    slack_token = environ.get('SLACK_TOKEN')
    if not slack_token:
        print("Warning: SLACK_TOKEN environment variable is not set.")

    # Loads the SLACK_CHANNEL_ID from the environment variables
    slack_channel_id = environ.get('SLACK_CHANNEL_ID')
    if not slack_channel_id:
        print("Warning:SLACK_CHANNEL_ID environment variable is not set.")

    # Initialize the Slack client with the token
    client = WebClient(token=slack_token)

    # Configure the application with necessary components
    app.config['SLACK_CLIENT'] = client

    # Assign SLACK_CHANNEL_ID to app config
    app.config['SLACK_CHANNEL_ID'] = slack_channel_id

    # Dynamically import views to register them with the Flask application
    from .views import bp as slack_bot_bp
    app.register_blueprint(slack_bot_bp)

    return app
