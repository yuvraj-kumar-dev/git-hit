import json
import datetime
from git import Repo
import os

DATE = datetime.datetime.now()
DATE = DATE - datetime.timedelta(days=5)  # Adjust to your required date
DATE = DATE.strftime('%Y-%m-%d %H:%M:%S')

os.environ['GIT_AUTHOR_DATE'] = DATE
os.environ['GIT_COMMITTER_DATE'] = DATE

REPO_PATH = 'https://github.com/yuvraj-kumar-dev/flask'

# Function to append new date to JSON file
def write_json(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        # Load existing data into a dictionary
        file_data = json.load(file)
        
        # Append new data to the 'emp_details' list
        file_data["DATE"].append(new_data)
        
        # Move the cursor to the beginning of the file
        file.seek(0)
        
        # Write the updated data back to the file
        json.dump(file_data, file, indent=4)

# New date to append
date = {
    "Date": DATE
}

write_json(date)

def make_commit():
    repo = Repo(REPO_PATH)
    repo.git.add('data.json')
    repo.index.commit(f'{DATE}')
    origin = repo.remote(name='origin')
    origin.push()

make_commit()


