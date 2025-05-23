def is_leap_year_mutant(year):
    if year % 4 == 0:
        if (
            year % 100 == 0 or year % 400 != 0
        ):  # Mutation: Composition of conditions and the logic must be connected with and instead of or
            # This condition is incorrect because it will return True for years that are divisible by 100 but not by 400
            return True
        else:
            return False
    else:
        return False
