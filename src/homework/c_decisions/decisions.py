#create function to accept two parameters with names option, total and returns the ratio
def get_options_ratio(options, total):
    return options / total

#create a function named get_faculty_rating that accepts the ratio according to the table
def get_faculty_rating(ratio):
    if 0.9 <= ratio < 1:
        return "Excellent"
    elif ratio > 0.8:
        return "Very Good"
    elif ratio > 0.7:
        return "Good"
    elif ratio > 0.6:
        return "Needs Improvement"
    else:
        return "Unacceptable"