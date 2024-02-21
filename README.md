## Hi! Welcome to the bots repo

I am currently working on a set of bots to spice up our household's slack. These are for fun.

This project is a Slack bot designed to manage a simple list directly from Slack commands. It is built with Flask and the Slack SDK for Python.

Here is a brief overview of what's in here:

### `views.py`

This file defines the routes and views for the Slack bot. It handles incoming Slack commands and interacts with the bot's functionalities, such as adding and removing items from a list.

### `models.py`

Contains the logic for managing the list. It defines functions to add and remove items from the list.

### `__init__.py`

This is the initialization file for the Flask application. It sets up the Flask app and the Slack client with tokens from the environment variables.

### `main.py`

The entry point for the Flask application. It loads environment variables and runs the Flask app.

## Dependencies

To install the necessary dependencies for this project, navigate to the project's root directory and run:

`pip install -r requirements.txt`

## To boot the slackbot locally run the following command:

`python main.py`

## Testing with Postman

1. **Start Your Flask App**: Ensure your Flask app is running locally on port 3000. To run the slackbot locally check the instructions above.
   
2. **Configure Postman Request**: In Postman, set up a new POST request to your Flask app's `/slack/command` endpoint. The full URL will be `http://127.0.0.1:3000/slack/command` if you're running the app locally.

3. **Send POST request**: In the request body, select `x-www-form-urlencoded` and enter the following key-value pairs:
   - `command`: The Slack slash command you want to test (e.g., `/add` or `/rem`).
   - `text`: The text that follows the command (e.g., `This is an item`) which would be what a string value that is added or removed from the list.

After sending the request, Postman will display the response from the Flask app. 

For example, when testing the `/add` command, you should see a JSON response indicating that the item has been added to the list. This response will mimic what the Slack API would send back and display in a Slack channel.

Here is an example of a successful JSON response after adding an item:

```json
{
  "response_type": "in_channel",
  "text": "Added 'This is an item' to the list :acowg: \n\n:sparkles:Updated wishlist:sparkles:: \n- TEST1"
}
```

## Deployment

This is the work in progress portion of this project. This bot will eventually be deployed to a Heroku server (hence the Procfile)

## Notes:

:acowg: is a slackmoji only available if you download it from slackmojis.com and set it up in your slack!

Also, for privacy reasons I have not included my real `.env` file here which contains sensitive information about my slack channel. You must create your own `.env` file and initialize the variables `SLACK_TOKEN` and `SLACK_CHANNEL_ID` with your own slack channel values.

Have fun :)

