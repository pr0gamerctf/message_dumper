import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token="XXXXXXXXX-XXXXXXXXXXXX-XXXXXXXXXXX")
channel_id = "1231242"

try:
    result = client.conversations_history(channel=channel_id)

    # Print results
    for message in result["messages"]:
        print(message)

except SlackApiError as e:
    print("Error:", e)
