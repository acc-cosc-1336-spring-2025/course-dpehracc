import decisions#

#Gather options and total input
options = int(input("What is the number of options?"))
total = int(input("What is the total?"))

#Calculate the ratio
result = decisions.get_options_ratio(options, total)

#Display the faculty rating
rating = decisions.get_faculty_rating(result)
print("Faculty Rating: " + rating)