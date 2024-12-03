
def markdown_to_blocks(markdown):
    # Split text into lines
    lines = markdown.splitlines()

    # Group lines based on empty line breaks
    groups = []
    current_group = []

    for line in lines:
        stripped_line = line.strip()
        if stripped_line:  # If the line is not empty
            current_group.append(stripped_line)
        else:  # If the line is empty, start a new group
            if current_group:
                groups.append("\n".join(current_group))
                current_group = []

    # Add the last group if any
    if current_group:
        groups.append("\n".join(current_group))

    return groups




text2 = """## Block One


This is block two with consecutive blank lines above.
"""
text3 = """A single block of text without any blank lines separating it.
It should all be treated as one block despite the lack of newlines.
"""
text4 = """### Heading



Paragraph text.


- Item 1
- Item 2
"""
