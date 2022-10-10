## Setup

### Prerequisites 
- Create a virtual environment `python -m venv ./venv`, `source ./venv/bin/activate` or `source ./venv/Scripts/activate`
- Install the relevant packages `pip install -r requirements.txt`
- To deactivate the virtual environment `deactivate`

### Running the clock in app
- To output the current time in human-friendly text `python ./src/app.py`
- To output the human-friendly text with user input for time `python ./src/app.py 18:52`

### Running the REST API clock
- To run the API on localhost:8080 `python ./src/rest_app.py`
- A GET request outputs the current time in human-friendly text `curl -X GET http://localhost:8080`       
- A POST request accepts input for time and outputs human-friendly text `curl -X POST -d '15:30' http://localhost:8080`

### Running unittests
To run unittests `PYTHONPATH=./src python -m pytest ./test`
