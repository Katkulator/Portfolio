from keyword import iskeyword

def contains_keyword(*args):
    return any(iskeyword(item) for item in args)
    
