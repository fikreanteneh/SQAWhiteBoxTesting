def is_leap_year_mutant(year):
    if year % 4 != 0:  # Mutation: '==' → '!='
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
