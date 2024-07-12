import requests
import random
import os

# GitHub repository details
owner = 'prefix-dev'
repo = 'pixi'
issue_number = '1607'
token = os.getenv('GITHUB_TOKEN') 

def get_issue_reactions(owner, repo, issue_number, token):
    url = f'https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/reactions'
    headers = {
        'Accept': 'application/vnd.github.squirrel-girl-preview+json',
        'Authorization': f'token {token}'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching reactions: {response.status_code} - {response.text}")

def pick_random_user(reactions):
    users = [reaction['user']['login'] for reaction in reactions]
    if users:
        return random.choice(users)
    else:
        return None
    

def print_reactions_nicely(reactions):
    if not reactions:
        print("No reactions found.")
        return

    for reaction in reactions:
        user = reaction['user']['login']
        content = reaction['content']
        print(f'User: {user} | Reaction: {content}')

def main():
    try:
        reactions = get_issue_reactions(owner, repo, issue_number, token)
        print_reactions_nicely(reactions)
        random_user = pick_random_user(reactions)
        if random_user:
            print(f'Randomly selected user: {random_user}')
        else:
            print('No reactions found.')
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
