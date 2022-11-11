import os
import sys
from github import Github
from dotenv import load_dotenv

load_dotenv()
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
path = os.getenv('FOLDERPATH')


if __name__ == "__main__":
    repo_name = str(sys.argv[1])
    os.mkdir(path+repo_name)
    user = Github(username, password).get_user()
    repo = user.create(repo_name)
    print(repo_name+" create succefully")

