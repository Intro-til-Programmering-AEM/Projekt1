#Input handlers og fejlsikring

# Denne funktion tager et brugerinput (options) og sender det videre, hvis det er valid.
# Hvis ikke så kommer der en fejlmeddelelse
def input_option(options):
    while(True):
        try:
            # Get number that may be a legal option
            x = int(input_wrapper("Select an option: "))
            # Check if it's legal
            if x <= len(options) and x > 0:
                return x
            else:
                print("Not an option, please try again.")
        except EOFError:
            return None
        except ValueError:
            print("Please input a number corresponding to the option you want to select.")
            pass

# Denne funktion tager alle reelle tal
# Returnerer en float eller None
def input_float(request):
    while(True):
        try:
            x = float(input_wrapper(request))
            return x
        except (ValueError, EOFError):
            print("Please input a real number.")
            pass


# Denne funktion ser om der er et input fra brugeren og laver en EOFError, hvis input er tomt.
# Den returnerer en string
def input_wrapper(request):
    x = input(request)
    if x == "":
        raise EOFError
    return x



