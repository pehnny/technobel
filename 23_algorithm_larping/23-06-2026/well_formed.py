"""
CHALLENGE 5

A configuration language uses three kinds of brackets to open and close
blocks: ( ), [ ], and { }. A configuration string is well-formed only
if every block that opens is closed by the matching bracket, and blocks
are closed in the reverse order they were opened. Given such a string
(containing only bracket characters), return True if it is well-formed.

Examples:
    well_formed("{[()]}")  -> True
    well_formed("{[(])}")  -> False
    well_formed("(()")     -> False

"""

from testkit import check, report


def well_formed(config):
    brackets = {
        ")": "(",
        "]": "[",
        "}": "{"    
    }

    stack = []
    for char in config:
        if char in brackets:
            if len(stack) == 0:
                return False
            
            previous = stack.pop()
            if previous != brackets[char]:
                return False
        else:
            stack.append(char)
    return len(stack) == 0

if __name__ == "__main__":
    check("nested ok", well_formed("{[()]}"), True)
    check("crossed", well_formed("{[(])}"), False)
    check("unclosed", well_formed("(()"), False)
    check("empty", well_formed(""), True)
    check("flat sequence", well_formed("()[]{}"), True)
    check("lone closer", well_formed("]"), False)
    report()
