''' Given the string s, use string methods to:
Remove leading/trailing spaces: remove all leading and trailing whitespace characters from the string.
Left justify with '*': left justify the string within a field of width 20, using * as the fill character.
Right justify with '*': right justify the string within a field of width 20, using * as the fill character.
s:str ="   Python is fun!   "'''

s = "   Python is fun!   "
trimmed_s = s.strip()
print(trimmed_s)  

left_justified_s = s.ljust(20, "*")
print(left_justified_s)  

right_justified_s = s.rjust(20, "*")
print(right_justified_s)  


