name = "Jatin"
greeting = f"Hello, {name}"
# fstring

print(greeting)

name = "Jatin1"

# To embed data at run time

greeting1 = "Hello , {}"
with_name = greeting1.format(name);
with_name_two = greeting1.format("Jatin Sharma");

print(with_name)
print(with_name_two)

longer_phrase = "Hello, {}. Today is {}"

formatted_longer_phrase = longer_phrase.format("Jatin", "Monday")

print(formatted_longer_phrase)