import requests
import json

def GitHub(userID):
    # sets URL with the user's ID
    gitUrl = "https://api.github.com/users/" + str(userID) + "/repos"
    # gets the user's account
    account = requests.get(gitUrl)

    # checks if account is valid
    if account.status_code  == 404:
        return("This account is not valid")

    else:
        # gets json info for all repos in user account
        account = account.json()
        repos = []
        for repo in account:
            # gets commit info for repo
            commits = requests.get("https://api.github.com/repos/" + str(userID) + "/" + str(repo["name"]) + "/commits")
            # counter for commits
            numCommits = 0
            # loop to count commits
            for commit in commits.json():
                numCommits  = numCommits + 1
            # add repo info to repo list
            repos.append("Repo: " + str(repo["name"]) + " Number of commits: " + str(numCommits))
            # print("Repo: " + str(repo["name"]) + " Number of commits: " + str(numCommits))
        return repos
    