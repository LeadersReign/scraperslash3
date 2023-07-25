import praw
from rich import print as rprint
from rich.console import Console
from rich.tree import Tree
from rich.layout import Layout
from rich.progress import track
from time import sleep
from openpyxl import Workbook

#Create a console instance
console = Console()
layout = Layout()
console.print("[bold Yellow]Reddit Bot[/bold Yellow] by [bold magenta]Damiclone👽[/bold magenta]", style="bold red")

#Create a workbook instance
wb = Workbook()
sheet = wb.active
sheet.append(["NAME", "TITLE", "DESCRIPTION", "URL/LINK", "NO OF SUBSCRIBERS", "ACTIVE USERS", "DATE CREATED (UTC)", "NSFW", "ALLOWS IMAGE", "ALLOWS VIDEO"])

#Get user input
_client_id = str(input("Enter client id: "))
_client_secret = str(input("Enter client secret: "))

#Create a Global reddit instance (for now, user agent is hardcoded)
reddit = praw.Reddit(client_id=_client_id,
                            client_secret=_client_secret,
                            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')

def main():
    #Get user input
    rprint("=====================================================")
    rprint("[bold Green]Welcome, What will you like to do ( 0 to quit )?[/bold Green] \n 1. Analyse a subreddit \n 2. Scrape Popular subreddits \n 3. Search for subreddits by a phrase/word: ")

    option = int(input("Enter option: "))
    if option == 1:
        rprint("[bold Yellow]Enter Subreddit to analyse: [/bold Yellow]")
        option = str(input())
        analyseSubreddit(option)
    elif option == 2:
        scrapePopularSubreddit()
    elif option == 3:
        searchSubredditsByName()
    elif option == 0:
        rprint("[bold red]Bye Bye,[/bold red] [bold magenta]Have a great Day Scrapper![/bold magenta]")
        quit()
    else:
        rprint("[bold red]Invalid option, Please try again with numbers![/bold red]")
        main()

#Function to analyse a subreddit
def analyseSubreddit(_option):
    try:
        subreddit = reddit.subreddit(_option)
        print("=====================================================")
        rprint("** Subreddit Name: ", subreddit.display_name)
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
        tree = Tree("** [bold red]Subreddit Rules[/bold red] **")
        for rule in subreddit.rules:
            tree.add(str(rule))
        rprint(tree)
        rprint("[bold green]Done[/bold green]")
        print("=====================================================")
        keepFunctionAlive()
    except:
        rprint("[bold red]An error occurred, Please Check what you entered and try again![/bold red]")
        keepFunctionAlive()


#function to scrape subreddits
def scrapePopularSubreddit():
    try:
        for subreddit in track(reddit.subreddits.popular(), description="searching for popular subreddits..."):
            sheet.append([subreddit.display_name, subreddit.title, subreddit.public_description, "https://reddit.com"+subreddit.url, subreddit.subscribers, subreddit.active_user_count, subreddit.created_utc, subreddit.over18, subreddit.allow_images, subreddit.allow_videos])
            sleep(0.1)
        worksheetName = str(input("Enter name of worksheet to save subreddits to: "))
        wb.save(worksheetName+".xlsx")
        rprint("=====================================================")
        rprint("[bold green]Done![/bold green] \n[bold Yellow]Subreddits has been saved to "+worksheetName+".xlsx[/bold Yellow]")
        rprint("=====================================================")
        keepFunctionAlive()
    except:
        rprint("[bold red]Error occured, Please try again![/bold red]")
        keepFunctionAlive()


#function to search subreddits by name
def searchSubredditsByName():
    print("=====================================================")
    try:
        searchPhrase = str(input("Enter phrase/word to search: "))
        for subreddit in track(reddit.subreddits.search(searchPhrase), description="Searching for subreddits..."):
            sheet.append([subreddit.display_name, subreddit.title, subreddit.public_description, "https://reddit.com"+subreddit.url, subreddit.subscribers, subreddit.active_user_count, subreddit.created_utc, subreddit.over18, subreddit.allow_images, subreddit.allow_videos])
        worksheetName = str(input("Enter name of worksheet to save the scrapped subreddits to: "))
        wb.save(worksheetName+".xlsx")
        rprint("=====================================================")
        rprint("[bold green]Done![/bold green] \n[bold Yellow]Scrapped Subreddits has been saved to "+worksheetName+".xlsx[/bold Yellow]")
        rprint("=====================================================")
        keepFunctionAlive()
    except:
        rprint("[bold red]Subreddit not found! Please try again![/bold red]")
        keepFunctionAlive()


#function to keep the program running
def keepFunctionAlive():
    while True:
        rprint("[bold Blue]What else will you like to do ( 0 to quit )[/bold Blue]? \n 1. Analyse a subreddit \n 2. Scrape Popular subreddits \n 3. Search for subreddits by a phrase/word: ")
        option = int(input("Enter option:"))
        if option == 1:
            print("=====================================================")
            rprint("[bold Yellow]Enter Subreddit to analyse: [/bold Yellow]")
            phrase = str(input())
            analyseSubreddit(phrase)
        elif option == 2:
            scrapePopularSubreddit()
        elif option == 3:
            searchSubredditsByName()
        elif option == 0:
            rprint("[bold blue]Bye Bye,[/bold blue] [bold magenta]Have a great Day Scrapper![/bold magenta]")
            quit()
        else:
            rprint("[bold red]Invalid option, Please try again with numbers![/bold red]")

if __name__ == '__main__':
    main()