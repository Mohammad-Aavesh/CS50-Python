# Title: CLI - Based Data Analyzer
## Name: Mohammad Aavesh
## edx username: MA_2510_5G4P
## GitHub username: Mohammad-Aavesh
## City: Harda, Madhya pradesh
## Country: India
#### Video Demo: <https://youtu.be/7yfDOwBqCUs>
#### Description:
My Project is a command-line tool that analyzes any CSV file and automatically generates a statistical summaries for each column. The program reads the CSV file provided as a command-line arguement, identifies whether each column contains numeric or categorial data, and outputs the appropiate statistics for each and in the numerical_calculations() fuction their is a specific condition if a list is empty, it can also handle it.

For numeric columns, the program computes the count of values, their sum, mean, median, maximum, and minimum. For categorical columns, it identifies all unique values and shows how many times each value appears in the dataset. The program also handles real-world data problems like missing values, ragged rows with unequal column counts, empty files, and invalid file types - outputting clean error messages instead of Python Error tracebacks.

## How to Run
```bash
python project.py yourfile.csv
```

## Example
```bash
python project.py Students.csv
```

## Features
 - Auto-detects numeric vs categorical columns
 - Numeric columns: count, mean, median, max, min
 - Categorical columns: unique values + full occurance count
 - Handles missing values
 - handles ragged rows (missing cells treated as empty)
 - Clean error messages for missing files, wrong format, empty files

 ## Functions
  - `input_validation()` - validates CLI args, reads and
     transposes CSV data, returns structured output
  - `calculations()` - detects column type, routes to
     appropriate calculator
  - `numerical_calculations()` - computes stats for numeric columns
  - `categorical_calculations()` - computes stats for text columns
  - `median_calculator` - calculates median for sorted numeric list
  - `print_data()` - formats and prints results per column

## Files
- `project.py` - main program
- `test_project.py` - pytest test cases
- `requirements.txt` - pytest for testing the functions
