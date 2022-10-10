from flask import Flask, request
from app import no_user_input, with_user_input
import json

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def request_times() -> json:
    """GET requests return the current time in human-friendly text, the POST request
    gets the time through user input and returns the time in a human-friendly text

    Parameters: Time in the format HH:MM (POST request only)
    Returns: Time in human friendly text or formatting suggestions (POST request only)

    """

    if request.method == 'GET':
        time_sentence = no_user_input()
    if request.method == 'POST':
        request_data = request.get_data().decode('utf-8')
        time_sentence = with_user_input(request_data)
    dict_time = {'payload_message' : time_sentence}
    return json.dumps(dict_time)


if __name__ == "__main__":
    app.run(port=8080, host='0.0.0.0')
