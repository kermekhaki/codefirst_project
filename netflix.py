import csv

# Debug for files that might contain errors - it will stop at a StopIterarion error and skip UnicodeDecodeError errors
my_data = []
with open('netflix_titles.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    row_iter = iter(spreadsheet)
    while True:
        try:
            row = next(row_iter)
        except StopIteration:
            break
        except UnicodeDecodeError:
            continue
        my_data.append(row)

print("Number of titles:", len(my_data))

# Programme type
netflix = []
for row in my_data:
    programme_type = (row['type'])
    netflix.append(programme_type)
# print(netflix)


# How many movies are there in total?
# How many TV shows are there in total?
def type_count(type_programme):
    number_of_programmes = 0
    for row in my_data:
        if row["type"] == type_programme:
            # number_of_programmes = number_of_programmes + 1
            number_of_programmes += 1
    return number_of_programmes


def print_type_count(type_program):
    # print("We are counting how many titles are a", type_program)
    number_of_programmes = (type_count(type_program))
    print("Total number of {}s:".format(type_program), number_of_programmes)


print_type_count("Movie")
print_type_count("TV Show")


# Total running time for movies in minutes and for TV shows in seasons
def programme_length(type_programme):
    total_running_time = 0
    for row in my_data:
        if row["type"] == type_programme:
            duration_str = row["duration"]
            quantity_str, unit = duration_str.split()
            if row["type"] == "Movie":
                assert unit == "min", "we expect unit to be 'min'"
            elif row["type"] == "TV Show":
                assert unit in ("Season", "Seasons"), "we expect unit to be 'Season' or 'Seasons'"
            else:
                raise NotImplementedError
            duration = int(quantity_str)
            total_running_time = total_running_time + duration

    return total_running_time


def print_programme_length(type_programme):
    if type_programme == "Movie":
        units = "minutes"
    else:
        units = "seasons"

    length = programme_length(type_programme)

    print("The total running time for all the {}s in {} is:".format(type_programme, units), programme_length(type_programme))
    print(f"The total running time for all the {type_programme}s is {length} {units}")


print_programme_length("Movie")
print_programme_length("TV Show")


# If I look for a specific programme, what are its details?
programme_title = input("What programme are you looking for?").lower()

netflix = []
for row in my_data:
    if row["title"] is None:
        continue
    if programme_title in (row['title']).lower():
        print(row["title"])
        print(row["type"])
        print(row["release_year"])
        print(row["rating"])
        print(row["duration"])


