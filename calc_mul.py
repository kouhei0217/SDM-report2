#!/usr/bin/python3

import re
                
def calc(A,B):
        if not isinstance(A, int) or not isinstance(B, int):
                valid = False
        else :
                if 1 <= A <= 999 and 1 <= B <= 999:
                        valid=True
                else:
                        valid=False
        if valid:
                ans=A*B
                return ans
        else:
                return -1
        
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
