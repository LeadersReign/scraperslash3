import praw
import rich
from rich import print as rprint
from rich.console import Console
from rich.tree import Tree
from rich.progress import track
from time import sleep



#Create a console instance
console = Console()
console.print("[bold Yellow]Reddit Scrapper[/bold Yellow] by [bold magenta]0xDamiclone👽[/bold magenta]", style="bold red")
#Get user input
_client_id = str(input("Enter client id: "))
_client_secret = str(input("Enter client secret: "))
#Create a Global reddit instance (for now, user agent is hardcoded)
reddit = praw.Reddit(client_id=_client_id,
                            client_secret=_client_secret,
                            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')

def main():
    #Get user input
    option = int(input("Enter 1 to analyse a subreddit, 2 to scrape subreddits: "))
    if option == 1:
        option = str(input("Enter Subreddit to analyse: "))
        analyseSubreddit(option)
    elif option == 2:
        scrapeSubreddit()
#Function to analyse a subreddit
def analyseSubreddit(_option):
    subreddit = reddit.subreddit(_option)
    print("=====================================================")
    print("* Subreddit Name: ", subreddit.display_name)
    print("=====================================================")
    print("* Title: ", subreddit.title)
    print("* Description: ", subreddit.public_description)
    print("* URL: ", "https://www.reddit.com"+subreddit.url)
    print("* Subscribers: ", subreddit.subscribers)
    print("* Active Users: ", subreddit.active_user_count)
    print("* Created: ", subreddit.created_utc)

    # list comprehension to print out if NSFW or not
    [print("* NSFW: Yes, it is NSFW") if subreddit.over18 else print("* NSFW: No, it is not NSFW")]
    print("* Allow Images: ", subreddit.allow_images)
    print("* Allow Videos: ", subreddit.allow_videos)

    print("=====================================================")
    tree = Tree("** [red]Subreddit Rules")
    for rule in subreddit.rules:
        tree.add(str(rule))
    rprint(tree)


#function to scrape subreddits
def scrapeSubreddit():
    print("Scraping subreddits...")
    

if __name__ == '__main__':
    main()