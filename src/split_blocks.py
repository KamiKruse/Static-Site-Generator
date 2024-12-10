
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

def block_passing(groups):
    block_types = []
    for block in groups:
        val = block_to_block_type(block)
        block_types.append(val)
    return block_types
    

def block_to_block_type(block):
    if block[0] == '#':
        count = 0
        first_space = block.find(" ")
        for i in range(0, len(block)):
            if block[i] == '#' and i <=5:
                count += 1
            if block[i] == "#" and i > 5:
                return "Invalid markdown"
        if count == 1 and count == first_space:
            return "h1"
        if count == 2 and count == first_space:
            return "h2"
        if count == 3 and count == first_space:
            return "h3"
        if count == 4 and count == first_space:
            return "h4"
        if count == 5 and count == first_space:
            return "h5"
        if count == 6 and count == first_space:
            return "h6"
        return 'Invalid markdown'
    
    if block[0] == '*':
        if block[1] != " ":
            return "Invalid markdown"
        for i in range(0, len(block)):
            if block[i] == "\n":
                if block[i+1] != "*":
                    return "Invalid markdown"
                elif block[i+2] != " ":
                    return "Invalid markdown"
        return "unordered list"
    
    if block[0] == '-':
        if block[1] != " ":
            return "Invalid markdown"
        for i in range(0, len(block)):
            if block[i] == "\n":
                if block[i+1] != "-":
                    return "Invalid markdown"
                elif block[i+2] != " ":
                    return "Invalid markdown"
        return "unordered list"
    
    if block[0] == "`":
        if block[1:3] != "``":
            return "Invalid markdown"
        if block[-4:-1] != "```":
            return "Invalid markdown"
        return "code"

    if block[0] == ">":
        return "quote"
    
    if  block[0].isdigit():
        if block[0] != '1':
            return "Invalid markdown"
        if block[1] != ".":
            return "Invalid markdown"
        if block[2] != " ":
            return "Invalid markdown"
        val = int(block[0])
        for i in range(0, len(block)):
            if block[i] == "\n":
                val += 1
                try:
                    if int(block[i+1]) != val:
                        return "Invalid markdown"
                except ValueError:
                    return "Invalid markdown"
                if block[i+2] != ".":
                    return "Invalid markdown"
                if block[i+3] != " ":
                    return "Invalid markdown"
        return "ordered list"
                
    return "paragraph"

# text = """# This is a heading

#         This is a paragraph of text. It has some **bold** and *italic* words inside of it.

#         1. This is the first list item in a list block
#         2. This is a list item
#         3. This is another list item
#         """
