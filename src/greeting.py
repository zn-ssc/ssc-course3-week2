from .data_fetcher import fetch_user_name


def generate_greeting(user_id):
    try:
        name = fetch_user_name(user_id)
        return f"Hello, {name}!"
    except ConnectionError:
        return "Error fetching user"
