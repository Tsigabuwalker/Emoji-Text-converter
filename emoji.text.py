# First, ensure you have the emoji library installed
# You can install it using pip if you haven't already:
# pip install emoji

import emoji

def convert_emoji_to_text(input_string):
    """Convert emojis in a string to their text representation."""
    return emoji.demojize(input_string)

def convert_text_to_emoji(input_string):
    """Convert text representation back to emojis."""
    return emoji.emojize(input_string)

# Example usage
if __name__ == "__main__":
    text_with_emojis = "I love Python! 🐍❤️"
    converted_text = convert_emoji_to_text(text_with_emojis)
    print("Converted to text:", converted_text)

    text_with_descriptions = "I love Python! :snake: :heart:"
    converted_emojis = convert_text_to_emoji(text_with_descriptions)
    print("Converted to emojis:", converted_emojis)