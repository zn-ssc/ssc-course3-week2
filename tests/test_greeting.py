from unittest.mock import patch

from src.greeting import generate_greeting


@patch("src.greeting.fetch_user_name")
def test_generate_greeting_returns_correct_message(mock_fetch_user_name):
    mock_fetch_user_name.return_value = "[Your name]"
    result = generate_greeting(5)
    assert result == "Hello, [Your name]!"


@patch("src.greeting.fetch_user_name")
def test_fetch_user_name_called_once(mock_fetch_user_name):
    generate_greeting(5)
    mock_fetch_user_name.assert_called_once()


@patch("src.greeting.fetch_user_name")
def test_fetch_user_name_raises_connection_error(mock_fetch_user_name):
    mock_fetch_user_name.side_effect = ConnectionError
    result = generate_greeting(5)
    assert result == "Error fetching user"
