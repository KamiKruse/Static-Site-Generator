import re

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    if matches:
        return matches
    
    if re.search(r"!(?:\[[^\[\]]*\][^\(]*|\s*[^[]+[^()\s]*https?:\/\/\S*|[^\[]*\([^\)]*\)|\[[^\[\]]+[\)\(])", text):
        raise Exception("Malformed markdown image syntax")
    
    return text  

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    if matches:
        return matches

    if re.search(r"\[.*?(?!\])|\((?!.*?\))|[^[]]\(|\][^(]", text):
        raise Exception("Malformed markdown link syntax")

    return text  

