import praw
def main():
    _client_id = str(input("Enter client id: "))
    _client_secret = str(input("Enter client secret: "))
    _user_agent = str(input("Enter user agent: "))

    #Create a reddit instance
    reddit = praw.Reddit(client_id=_client_id,
                            client_secret=_client_secret,
                            user_agent=_user_agent)
    

if __name__ == "__main__":
    main()