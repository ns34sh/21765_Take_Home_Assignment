# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 21:45:40 2023

@author: namit
"""
from file_parsing_module import parse_input
from read_clean_data import read_data
from print_results import print_output

# Function to print a csv file as a table after modifying the data based on
# some filtering and sorting criteria provided by the user
def main():
    print_output(read_data(parse_input()))
    
if __name__ == "__main__":
    main()