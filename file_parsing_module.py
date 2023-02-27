# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 21:21:01 2023

@author: namit
"""

from argparse import ArgumentParser

# function to parse command line arguments. Checks if the argument type is as 
# expected and returns a tuple with arguments to be used by other modules 
def parse_input():
    parser = ArgumentParser()
    
    parser.add_argument('--separator', '-s', 
                        help = 'specifies the separator of the fields;' 
                        'default: comma', type = str, default =',')
    
    parser.add_argument('--list', '-l',
                        help = 'outputs just the list of column names found in' 
                        'the csv file instead of the table', action = 'store_true')
    
    parser.add_argument('-o', 
                        help = 'includes only the specified column; can be used'
                        'repeatedly to include more columns;'
                        'order matters; default: list all columns',
                        action = 'append')
    
    parser.add_argument('-u', type = str,
                        help = 'sort the table by ordering up the specified column;'
                        'default: no sort', default = '')
    
    parser.add_argument('-d', type = str,
                        help = 'sort the table by ordering down the specified column;'
                        'default: no sort', default = '')
    
    parser.add_argument('-m', type = str,
                        help = 'lists only the rows having at least one element '
                        'containing the string', default = '')
    
    parser.add_argument('-n', type = int,
                        help = 'displays only the first specified number of rows of'
                        'the table (after matching and ordering)')
    
    parser.add_argument('data_file',
                        help = 'Path of the csv file')
    
    args = parser.parse_args()
    
    # If the user has provided column names for sorting up and down, raise error
    if args.u != '' and args.d != '':
        raise Exception('Use either -u or -d parameters!')
    
    return args.separator, args.list, args.o, args.u, args.d, args.m, args.n, \
            args.data_file    
    

        