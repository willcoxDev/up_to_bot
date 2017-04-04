import praw
import config
import time
import sys

def bot_login():
    print ("logging in...")
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "up to bot by /u/up_to_bot")
    print ("logged in...")
    return r

r = bot_login()


def run_bot():
    subreddit = r.subreddit('all')
    found_text = 'C:\\Users\\Rick\\Desktop\\redditbot\\commentid_found_txt.txt' //Change the directory to your files here
    notfound_text = 'C:\\Users\\Rick\\Desktop\\redditbot\\commentid_notfound_txt.txt' //Change the directory to your files here
    correct_text = 'C:\\Users\\Rick\\Desktop\\redditbot\\commentid_correct_txt.txt' //Change the directory to your files here
    words_to_match = [' upto ']
    words_up_to = ['up to']
    print ("\nconnecting to subreddit...")
    comments = subreddit.comments()
    print ("gathering comments...")
    print ("searching for spelling error in /r/%s" %subreddit)
    for comment in comments:
        comment_text = comment.body.lower()
        comment_id = comment.id
        is_match = any(string in comment_text for string in words_to_match)
        is_correct = any(string in comment_text for string in words_up_to)
        found = comment_found(comment_id, found_text)
        correctfound = comment_correct(comment_id, correct_text)
        contain = percent_found(found_text)
        #notcontain = percent_notfound(notfound_text) 
        correct = percent_correct(correct_text)
        percent = (contain/(contain+correct))*100

        if found is False and is_match:
            comment.reply("\nThe correct spelling is 'up to', if it makes you feel any better this is [me IRL](http://imgur.com/a/aZmW1), up to is spelled incorrectly in " + "%.2F"%percent+"%  of posts that use the word 'upto' in /r/all")
            print ("\n*********************************\n")
            print ("up to error sent to user!")
            print ("\n*********************************\n")
            write_found(comment_id, found_text)
            sleep_bot()
        #if is_match is False:
         #  write_notfound(comment_id, notfound_text)
        if  correctfound is False and is_correct is True:
            write_correct(comment_id, correct_text)


def comment_found(comment_id, found_text):
    found = False
    if comment_id in open(found_text).read():
        found = True
        return found
    else:
        return found

def comment_correct(comment_id, correct_text):
    found = False
    if comment_id in open(correct_text).read():
        found = True
        return found
    else:
        return found

def sleep_bot():

    print ("\nbot is sleepy, waiting 10 minutes")
    for x in range(600,0,-1):
        sys.stdout.write("\r")
        sys.stdout.write("%s seconds remaining" %x)
        sys.stdout.flush()
        time.sleep(1)

def write_found(comment_id, found_text):
    with open(found_text,'a') as x:
        x.write('%s\n' %comment_id)

def write_notfound(comment_id, notfound_text):
    with open(notfound_text, 'a') as x:
        x.write('%s\n' %comment_id)

def write_correct(comment_id, correct_text):
    with open(correct_text, 'a') as x:
        x.write('%s\n' %comment_id)

def percent_found(found_text):
    with open(found_text, 'r') as f:
        contain =  sum(1 for line in f)
    return contain

def percent_notfound(notfound_text):
    with open(notfound_text, 'r') as f:
        notcontain =  sum(1 for line in f)
    return notcontain

def percent_correct(correct_text):
    with open(correct_text, 'r') as f:
        correct =  sum(1 for line in f)
    return correct

while True:
    run_bot()
