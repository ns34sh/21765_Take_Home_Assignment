# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 21:33:52 2023

@author: namit
"""
from tabulate import tabulate

# Function that takes an integer (indicating number of rows in csv file) and
# a list of strings which will be used to populate table. 
def print_output(args):
    num_rows, filtered_data = args
    # Print the number of rows in the orginal csv file
    print(f'Total number of rows in input data file: {num_rows}')
    # Print the number of rows in the filtered data
    print(f'Total number of rows in filtered data file: {len(filtered_data)}')
    # Print the number of discarded rows
    print(f'Total number of discarded rows: {num_rows - len(filtered_data)}')
    # Print the tabulated data based on filtered_data
    print (tabulate(filtered_data, headers = "firstrow", tablefmt="grid"))