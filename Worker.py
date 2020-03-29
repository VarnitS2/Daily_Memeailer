import praw
import datetime
import os
import ezgmail
import urllib.request

today = datetime.date.today()
date = '{}-{}-{}'.format(today.month, today.day, today.year)

os.makedirs('Memes', exist_ok=True)

clientSecretFileName = 'client_secret.txt'
emailsFileName = 'emails.txt'

with open(clientSecretFileName) as f:
    tokens = f.readline().split(", ")
    reddit = praw.Reddit(client_id=tokens[0], client_secret=tokens[1], user_agent=tokens[2])

subreddit = reddit.subreddit('memes')

for post in subreddit.top('day', limit=1):
    urllib.request.urlretrieve(post.url, 'Memes/{}.jpg'.format(date))

def sendMail(mail):
    ezgmail.send(mail, 'Daily Meme!', 'Greetings!\nHere is your daily meme!\nAlso, wash your damn hands and stay away from people.\n\n-VS-', ['Memes/{}.jpg'.format(date)])

with open(emailsFileName) as f:
    emails = f.readline().split(", ")
    for email in emails:
        sendMail(email)