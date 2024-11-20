import re

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    if matches:
        return matches
    # Check for potential malformed markdown
    if re.search(r"(?:!\[[^\[\]]*\]\([^\(\)]*\)|!\[[^\[\]]*\][^\(]*|!\s*[^[]+[^()\s]*https?:\/\/\S*|\[[^\[\]]*\]\([^\)]*|[^\[\]]*\([^\)]*|![^\[]*\([^\)]*\)|!\[[^\[\]]+[\)\(])", text):
        raise Exception("Malformed markdown image syntax")

    return text  # Returning None if no matches and no malformed syntax found

    # pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    # matches = re.findall(pattern, text)    
    # # If no markdown images found, return original text
    # if len(matches) == 0:
    #     # Additional check to catch malformed markdown
    #     if re.search(r"!\[.*\]|\[.*\(.*\)", text):
    #         raise Exception("Malformed markdown image syntax")
    #     return text   
    # # If markdown images found, return the matches
    # return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    if matches:
        return matches

    # Check for potential malformed markdown
    if re.search(r"\[.*?(?!\])|\((?!.*?\))|[^[]]\(|\][^(]", text):
        raise Exception("Malformed markdown link syntax")

    return text  # Returning None if no matches and no malformed syntax found
    # pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    # matches = re.findall(pattern, text)  
   
    # # If no markdown links found, return original text
    # if len(matches) == 0:
    #     # Additional check to catch malformed markdown
    #     if re.search(r"\[.*\](?!\(.*\))|\[.*\(.*\)(?!\])", text):
    #         print(matches)
    #         raise Exception("Malformed markdown link syntax")
    #     return text
    # # If markdown links found, return the matches
    # return matches

# test_text = " and a ![image](https://test.com)"
# print(extract_markdown_images(test_text))

