#Filter relaterede funktioner

def print_filters(filters):
    if not filters:
        print("No active filters.")
    else:
        print("Active filter:")
        for f in filters:
            print("* "+f[1])

def continous_filter_closure(choice, col_number, bound):
    def filter_fun(row):
        col = row.Temperature if col_number == 1 else row.GrowthRate
        return col < bound if choice == 1 else col > bound
    return filter_fun