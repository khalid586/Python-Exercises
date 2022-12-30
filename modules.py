# builtin library
import math
import calendar

# user defined library
import Function as f
area, circum, diameter = f.circle_calc(5)
print(round(area, 2))  # 78.54 (calculated from the Function.py file

# if you want to import from a different directory
# import  sys
# sys.path.append("address")
