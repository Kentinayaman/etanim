import re

def remove_inner_tags(text):
    # Use regular expression to replace tags with an empty string
    return re.sub('<[^<]+?>', '', text)

# Example usage
text_with_tags = "<p>Hello, <em>world</em>!</p>"
clean_text = remove_inner_tags(text_with_tags)
print(clean_text)  # Output: Hello, world!
