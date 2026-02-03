import re
def parse_command(command):
    """
    Docstring for parse_command
    
    :param command: Command should always be in this format "ws-key-words-with-hypher-for-space-50"
        - Here 'ws' denotes that whole phrase is a word salad command
        - anything after "ws" until the last literal is considered as the keyword
        - last literal must be a number which will be considered as the no.of words in the required paragraph to be generated
    """
    command_pattern = "^ws-[A-Za-z0-9-]{-[1-9][0-9]{0,2}$"
    print(re.match(command_pattern, command))
    if not re.match( command_pattern, command):
        return
    literals = command.split("-")
    paragraph_length = literals[-1]
    keyword = " ".join(literals[1:-1])
    return keyword, paragraph_length


