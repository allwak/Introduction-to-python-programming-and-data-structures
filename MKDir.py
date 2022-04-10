import os

from sympy import sstr
  
for i in range (1,24):
    chapter_num = "0"*(2-len(str(i))) + str(i)
    os.mkdir(f"Chapter {chapter_num}")