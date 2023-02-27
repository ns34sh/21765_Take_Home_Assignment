# 21765_Take_Home_Assignment
Python modules for printing table based on filtered csv input file

How to run the program:

-> User can run the program by executing csv_2_table.py from the command line as shown below:
python csv_2_table.py [options] <data_file>

where the options are:
-s <string> specifies the separator of the fields; default: comma;
-l outputs just the list of column names found in the csv file instead of the table;
-o <string> includes only the specified column; can be used repeatedly to include more columns;
order matters; default: list all columns;
-u <string> sort the table by ordering up the specified column; default: no sort;
-d <string> sort the table by ordering down the specified column; default: no sort;
-m <string> lists only the rows having at least one element containing the string; multiple
appearances are joined by OR;
-n <integer> displays only the first specified number of rows of the table (after matching and
ordering).
  
** For parameters -o, -u, -d; column names are case-sensitive.
** Similary, for -m parameter; the string is filtering is case-sensitive.
** Only one parameter out of -u or -d should be used at a time. 
