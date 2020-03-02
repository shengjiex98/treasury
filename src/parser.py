import sys
import csv
import readline
import os.path

class CategoryCompleter:
    """Autocompleter for categories defined in a database"""
    def __init__(self, database: dict):
        self.database = database

    def complete(self, text, state):
        """Autocompletes if there's a category in database that matches the input text"""
        results = [x for x in list(set(self.database.values())) if x.startswith(text.lower().capitalize())] + [None]
        return results[state]

def main():
    set_date    = True
    results     = []

    if not os.path.isfile("categories.csv"):
        open("categories.csv", "a").close()

    with open("categories.csv", "r") as file_data:
        # Load the database from the file
        reader = csv.reader(file_data)
        database = {rows[0]: rows[1] for rows in reader}

    # Create and link the completer
    completer = CategoryCompleter(database)

    readline.parse_and_bind("tab: complete")
    readline.set_completer(completer.complete)

    with open(sys.argv[1], 'r') as file_input:
        for line in (s.strip("\n") for s in file_input):
            if line == "":
                # Done processing for one day, moving on to the next
                set_date = True
            elif set_date:
                date = line.strip()
                set_date = False
            else:
                # Date remains the same, read entries.
                words = line.split(" ")
                name, value = " ".join(words[0:-1]), words[-1]
                if name not in database:
                    database[name] = input("Please enter the category for '" + name + "': ").lower().capitalize()
                    with open("categories.csv", "a") as file_data:
                        # Write to the database file as new categories are added.
                        file_data.write(name + "," + database[name] + "\n")
                results.append((date, name, database[name], value))

    with open(sys.argv[2], 'w') as file_output:
        for entry in results:
            file_output.write(",".join([x for x in entry]) + "\n")

if __name__ == "__main__":
    main()
