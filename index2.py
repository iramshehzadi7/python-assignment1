''' Given the variables name, age, and city, use f-strings to construct a sentence that describes a person using these variables.
name:str = "Alice"
age:int = 30
city:str = "New York"
Instructions: Use an f-string to create a sentence in the format: "Alice is 30 years old and lives in New York."
Expected Output:
Alice is 30 years old and lives in New York.'''

name = "Alice"
age = 30
city = "New York"

sentence = f"{name} is {age} years old and lives in {city}."
print(sentence)
