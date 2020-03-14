""" Helper functions for working with git """

import shutil
import os
from git import Repo, Git
import config

DEBUG = False


def define_version(repo, version):
    """If a version is not defined then grab the latest tag."""
    if version == "":
        j = []
        for i in repo.tag(l=True).splitlines():
            j.append(i)
        version = max(j)
    return version


def clone_repo(repo_name, repo_version, repo_location):
    """Clone the needed repo and checkout the desired branch"""

    Repo.clone_from(repo_name, repo_location)
    repo = Git(repo_location)
    repo.init()

    version = define_version(repo, repo_version)

    if DEBUG or config.DEBUG:
        print("Checking out version: " + version)
    if version != "master":
        repo.checkout(version)


def repo_setup(data_version):
    """ Setup the repos needed to update the controls spreadsheet.
    The version can either be an empty string which will force the latest tag to be pulled, a branch which will be
    checked out, or tag that will then get checked out. At a low level git considers branches and tags identical
    and treats them the same.
    Only SSH is currently supported for cloning repos.
    """

    # clean up the directories if they exist
    for directory in config.dir_list:
        if os.path.exists(directory):
            shutil.rmtree(directory)

    clone_repo(config.COVID_19_REPO, data_version, config.COVID_19_DIR)

def cleanup():
    """ Cleanup after yourself
    """
    for directory in config.dir_list:
        if os.path.exists(directory):
            shutil.rmtree(directory)
