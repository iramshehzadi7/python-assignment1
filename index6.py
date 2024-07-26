'''Given the string s, use string methods to:
Split into a list: break the string into a list of substrings based on the delimiter ,.
Join with spaces: combine the list of substrings back into a single string, with each element separated by a space.
s:str ="apple,banana,cherry,dates"'''

s = "apple,banana,cherry,dates"
fruit_list = s.split(",")
print(fruit_list)  

joined_string = " ".join(fruit_list)
print(joined_string)  

