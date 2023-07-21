import praw

#Get user input
_client_id = str(input("Enter client id: "))
_client_secret = str(input("Enter client secret: "))

#Create a Global reddit instance (for now, user agent is hardcoded)
reddit = praw.Reddit(client_id=_client_id,
                            client_secret=_client_secret,
                            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')

#Function to analyse a subreddit
def analyseSubreddit():
    option = str(input("Enter Subreddit to analyse: "))
    subreddit = reddit.subreddit(option)
    print("=====================================================")
    print("* Subreddit: ", subreddit.display_name)
    print("=====================================================")
    print("* Title: ", subreddit.title)
    print("* Description: ", subreddit.public_description)
    print("* URL: ", "https://www.reddit.com"+subreddit.url)
    print("* Subscribers: ", subreddit.subscribers)
    print("* NSFW: ", subreddit.over18)
    print("* Allow Images: ", subreddit.allow_images)
    print("* Allow Videos: ", subreddit.allow_videos)

    print("=====================================================")
    print("* Rules: ")
    [print("=>", rule) for rule in subreddit.rules]



analyseSubreddit()