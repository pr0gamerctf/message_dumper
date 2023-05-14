import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Set the SLACK_BOT_TOKEN environment variable to your bot token
client = WebClient(token="XXXXXXXXX-XXXXXXXXXXXX-XXXXXXXXXXX")


try:
    # Call the conversations.history method using the WebClient
    # conversations.history returns the first 100 messages by default
    # These results are paginated, see: https://api.slack.com/methods/conversations.history$pagination
    result = client.conversations_history(channel=channel_id)

    # Print results
    for message in result["messages"]:
        print(message)

except SlackApiError as e:
    print("Error:", e)
