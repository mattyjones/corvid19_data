## Setup

This requires python3 and has only been test with Python 3.6 and 3.7.

### Python 
1. `pipenv --python python3 # create a new env`
1. `pipenv shell # start the env`
1. `pipenv install # install the deps`

## Running locally

You can run the development server locally use `python run.py`. The debug flag is set to false globally. This flag can be set either globally or on a  


## Troubleshooting

~~**Address already in use**~~
 
~~ The auth is starting a server and the server is already running locally. The solution is to stop the development server, then run `python survey.py` to generate the necessary creds. At this point you can start the development server.~~
