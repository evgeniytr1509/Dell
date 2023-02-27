def format_ingredients(items):
    if len(items) > 1:
        first_three = items[0:len(items)-1]
        end = ", ".join(first_three)
        end += " and "
        last = items[-1]
        end += last
    else:
        end = "".join(items)
    return end

format_ingredients("2 eggs", "1 liter sugar", "1 tsp salt", "vinega")
