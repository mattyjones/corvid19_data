""" API and internal endpoints """
from flask import render_template, request

from app import app, git , data


DEBUG = False


@app.route('/')
def main():
    """Generate the homepage"""

    return "hello World"

@app.route('/update_data')
def update_data():
    """Pull a new copy of the repo, generate the dict from the yaml, and push it to the cache as a json string"""

    repo_version = "master"

    # pull the needed repos
    git.repo_setup(repo_version)

    # convert the yaml to csv and write it to a tmp file
    data_json = data.generate_data()

    git.cleanup()

    return data_json
