# Filter relaterede funktioner

# Denne funktion printer filtrene
# Returnerer print
def print_filters(filters):
    if not filters:
        print("No active filters.")
    else:
        print("Active filters:")
        # Printer hvilke filtre, der er aktiveret
        for f in filters:
            print("* "+f[1])

# Denne funktion laver en ny funktion - en filterfunktion
# Returnerer true eller false
def continous_filter_closure(choice, col_number, bound):
    # filter_fun virker for en hver række enten for Temperature eller GrowthRate
    def filter_fun(row):
        col = row.Temperature if col_number == 1 else row.GrowthRate
        # Herefter undersøger den om den col er større eller mindre end bound afhængig af om der er valgt upper eller lower bound
        return col < bound if choice == 1 else col > bound
    return filter_fun
