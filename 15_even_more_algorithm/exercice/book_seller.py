def stock_list(stocklist: list[str], categories: list[str]) -> str:
    if len(stocklist) == 0:
        return ""
    
    robert = {key : 0 for key in categories}
    for stock in stocklist:
        code, quantity = stock.split()
        category = code[0]
        if category in robert:
            robert[category] += int(quantity)
    return " - ".join([f"({category} : {robert[category]})" for category in categories])
