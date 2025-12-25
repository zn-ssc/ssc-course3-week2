def count_vowels(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    vowels = "aeiouAEIOU"
    count = sum(1 for char in text if char in vowels)

    return count
