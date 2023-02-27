# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 21:24:18 2023

@author: namit
"""

import csv
import re

# Function takes in a string and removes non-alphanumeric a string is alphanumeric.
# Function also truncates the input string if its length exceeds more than 10 characters.
def filter_word(word):
    word = re.sub('[^0-9a-zA-Z]+', '', word)
    if len(word) > 10:
        word = word[0:10]
    return word

# Function takes in a dictionary and a list of strings and returns a list
# of strings that are made of dictionary values corresponding to the keys present in
# input list of strings
def filter_row(row, include_col):
    filtered_row = []
    for key, value in row.items():
        if (include_col == None or key in include_col):
            filtered_row.append(filter_word(value))
    return filtered_row
    
# Function that takes as input the parameters returned by file_parsing_module
# and returns the number of rows in the input data and filtered data for further
# processing by print_results module.
def read_data(separator, display_headers, include_col, sort_up_col, 
                  sort_down_col, specified_string, max_rows, path):
    
    # Raise error if the input file is not a csv file
    if path[-4:] != ".csv":
        raise Exception("File type is not csv")
    
    #Read the input csv file
    with open(path,'r') as file:
        reader = csv.DictReader(file, delimiter = separator)
        data_list = list(reader)
    
    filtered_data = []
    
    # Total number of rows in the input csv file
    num_rows = len(data_list) + 1
    # headers in the input csv file
    headers = list(data_list[0].keys())
    # Number of columns in the input csv file
    num_cols = len(headers)
    
    # Check if the user-provided column names for filtering (if any) and 
    # sorting (if any) match with headers in the input csv file
    # and raise an error if user input is not valid
    if include_col != None:
        for col_name in include_col:
            if not col_name in headers:
                raise Exception(f'Column name "{col_name}" for parameter -o is not valid!')            
    if sort_up_col != '' and not (sort_up_col in headers):
        raise Exception('Specified column name for parameter -u is not valid!')
    if sort_down_col != '' and not (sort_down_col in headers):
        raise Exception('Specified column name for parameter -d is not valid!')
    
    # Sort the table based on ascending order of column name given by user
    if sort_up_col != '':
        data_list = sorted(data_list, key=lambda x: x[sort_up_col], reverse = False)
    
    # Sort the table based on descending order of column name given by the user    
    if sort_down_col != '':
        data_list = sorted(data_list, key=lambda x: x[sort_down_col], reverse = True)
    
    # If the user wants table to contain specific columns, only include headers of those columsn
    if include_col == None:
        filtered_data.append(headers)
    else:
        filtered_data.append(include_col)
    
    # for each row of inoput data, check various filtering criteria provided by the user
    # and populate a new list with filtered data
    for rownum, row in enumerate(data_list):
        
        # Restrict number of rows in output table to max_rows specified by the user
        if len(filtered_data) == max_rows:
            break
        
        # print column names and exit if --list parameter is provided by the user
        if display_headers:
            print(headers)
            exit()
        
        # If any row contains more entries than number of headers, then ignore such rows
        if len(row) == num_cols:
            values_list = list(row.values())
            # If user has specified a string that should be present in each row
            # then only include rows with such strings
            if specified_string == '' or specified_string in values_list:
                #Remove alphanumeric characters and truncate 
                filtered_data.append(filter_row(row, include_col))
    
    return num_rows, filtered_data 