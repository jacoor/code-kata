# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
# solution
def move_zeros(lst):
    zeros = [0] * lst.count(0)
    ret = [ x  for x in lst if x !=0 ]
    return ret + zeros
