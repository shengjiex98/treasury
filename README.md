# treasury

A parser that generates `.csv` files from text documents. I use this program with Excel PivotTables to track my monthly expenses.

## Usage

The parser expects an input text file of the following format:
```
2/1                 # Dates can have any format, as long as it's in a line by itself.
Domino's 11.7
Target 12.5         # There should be no blank lines among the entries of the same 
Hibachi & Co 30     #   day or between the entries and the date.

2/2                 # Different dates should be separated by 1 or more blank lines.
Movie 12            # The amount should be the last part of an entry, separated from
Target 36           #   the description by a space.
...
```
This format should feel natural to type on a mobile device. Once you have an `input.txt` file with the above format, run the following command:
```
python3 parser.py input.txt output.csv
```
`parser.py` processes the text file and writes to a `.csv` file called `output.csv`. While running, the parser will ask for the category of an entry if it has not seen it before. For example, the parser will prompt for the first time it encounters `Target` in the file
```
Please enter the category for 'Target': 
```
and it will accept an input. Once the category is set for `Target`, however, any future mention of `Target` in the text file will be automatically supplied with the category that has been previously set. The resulting `output.csv` file should look something like this:
```
2/1,Domino's,Restaurant,11.7
2/1,Target,Grocery,12.5
2/1,Hibachi & Co,Restaurant,30
2/2,Movie,Entertainment,12
2/2,Target,Grocery,36
```

### Tab Completion

The parser also supports tab completion when prompting for categories. For example, if you have already entered `Resaurant` as the category for `Domino's`, then when you are prompt for entering the category for `Hibachi & Co`, you can just type `r` or `re` (as long as there's no conflict) and followed by `tab` and the program will autocompletes it to `Restaurant`. This is very useful when you have a limited number of categories.

## The Data File

The category data will be saved to a file called `categories.csv` for future use, and will be read and appended each time the parser is run. It has a format like this
```
Domino's,Restaurant
Target,Grocery
Hibachi & Co,Restaurant
Movie,Entertainment
```
