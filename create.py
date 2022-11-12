import os
import sys
from github import Github
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')
path = os.getenv('FOLDERPATH')

if __name__ == "__main__":
    repo_name = str(sys.argv[1])
    try:
        os.mkdir(path+repo_name)
    except:
        pass
    user = Github(token).get_user()
    repo = user.create_repo(repo_name)
    print(repo_name+" create succefully")
