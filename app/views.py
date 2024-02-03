from flask import Blueprint, request, jsonify, current_app
from .models import add_item, remove_item

bp = Blueprint('slack_bot', __name__, url_prefix='/slack')

@bp.route("/command", methods=["POST"])
def handle_slack_command():
    client = current_app.config['SLACK_CLIENT']
    data = request.form
    command_text = data.get("text")
    command_name = data.get("command")
    channel_id = current_app.config.get('SLACK_CHANNEL_ID', 'default_channel_id')
    
    if command_name == "/add":
        response_text = add_item(command_text)
    elif command_name == "/rem":
        response_text = remove_item(command_text)
    else:
        response_text = "Unknown command."

    client.chat_postMessage(channel=channel_id, text=response_text)
    return jsonify({"response_type": "in_channel", "text": response_text})
