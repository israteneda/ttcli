def instructions():
    message = (
            banner() + '\n' +
            usage() + '\n' +
            options() + '\n' +
            examples()
    )

    return message


def banner():
    return """
 _______  ___   __   __  _______    _______  ______    _______  _______  ___   _  _______  ______   
|       ||   | |  |_|  ||       |  |       ||    _ |  |   _   ||       ||   | | ||       ||    _ |  
|_     _||   | |       ||    ___|  |_     _||   | ||  |  |_|  ||       ||   |_| ||    ___||   | ||  
  |   |  |   | |       ||   |___     |   |  |   |_||_ |       ||       ||      _||   |___ |   |_||_ 
  |   |  |   | |       ||    ___|    |   |  |    __  ||       ||      _||     |_ |    ___||    __  |
  |   |  |   | | ||_|| ||   |___     |   |  |   |  | ||   _   ||     |_ |    _  ||   |___ |   |  | |
  |___|  |___| |_|   |_||_______|    |___|  |___|  |_||__| |__||_______||___| |_||_______||___|  |_|"""


def check(argv):
    if argv == "-h":
        print(instructions())


def usage():
    return """
    Usage:
        tt clock-in [now | time] [task]
        tt clock-out [task]
        tt -h | --help
        tt --version"""


def options():
    return """
    Options:
        -h --help   Show this screen
        --version   Show version"""


def examples():
    return """
    Examples:
        tt clock-in now
        tt clock-out "Creation of the Time Tracker CLI project"""
