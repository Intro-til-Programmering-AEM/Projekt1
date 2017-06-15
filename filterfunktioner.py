#Filter relaterede funktioner

def print_filters(filters):
    if not filters:
        print("No active filters.")
    else:
        print("Active filter:")
        for f in filters:
            print("* "+f[1])

def continous_filter_closure(col_number, bound):
    col = row.Temperature if col_number == 1 else row.GrowthRate
    filter_fun = lambda r: col < bound if choice == 1 else col > bound
    return filter_fun