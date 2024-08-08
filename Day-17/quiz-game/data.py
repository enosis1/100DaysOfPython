import requests


def get_posts():
    """Define the API endpoint URL"""
    url = "https://opentdb.com/api.php?amount=10&category=9&type=boolean"

    try:
        # Make a GET request to the API endpoint using request.get()
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print(f"Error: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        # Handle any network-related errors or exceptions
        print(f"Error: {e}")
        return None


def main():
    posts = get_posts()
    if posts:
        print("Generating a random list of questions...")
    else:
        print("Failed to fetch posts from API.")
    return posts


if __name__ == "__main__":
    main()
