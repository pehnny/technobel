def TreeConstructor(strArr) -> str:
    def parse(node: str) -> tuple[str, str]:
        split = node.split(",")
        child = split[0].lstrip("(")
        parent = split[1].rstrip(")")
        return (child, parent)

    nodes = [parse(node) for node in strArr]
    children = [node[0] for node in nodes]
    tree = {}

    for node in nodes:
        child, parent = node
        if parent not in tree:
            tree[parent] = [child]
        else:
            tree[parent].append(child)
            if len(tree[parent]) > 2:
                return "false"
    
    root_count = 0
    for node in tree:
        if node not in children:
            root_count += 1
            if root_count > 1:
                return "false"
  
    return "true"

def BracketMatcher(strParam):
    state = 1
    for char in strParam:
        if char == "(":
            state += 1
        elif char == ")":
            state -= 1
        if state < 1:
            return 0

    if state > 1:
        return 0
    return 1
