# treasury

A parser that generates `.csv` files from text documents. I use this program with Excel PivotTables to track my monthly expenses.

## Usage

The parser expects an input text file of the following format:
```
2/1                         # Dates can have any format, as long as it's in a line by itself.
Some expenses A 11.7
Other expenses B 12.5       # All entries of the same date should have no blank lines among  
Another expense C 30        #   themselves or between them and the date.


2/2                         # Different dates should be separated by 1 or more blank lines.
Today's expense 12          # The amount should be the last part of an entry, separated by a space.
...
```

Once you have an `input.txt` file with the above format, run the following command:
```
python3 parser.py input.txt output.csv
```
This writes to a `.csv` file called `output.csv`. While running, the parser will ask for the category of an entry if it is the first time that the entry appears. For example, the parser will prompt the first time it encounters `Movie` in the file
```
Please enter the category for 'Movie': 
```
and it will accept an input. Once the category is set for `Movie`, however, any future mention of `Movie` in the text file will be automatically supplied with the category that it was previously set. The category data will be saved to a file called `categories.csv`, and will be read and appended each additional time the parser is run. This is very useful when dealing with limited categories such as expense types.

The parser also supports tab complete when prompting for categories.
