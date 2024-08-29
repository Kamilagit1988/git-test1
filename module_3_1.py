calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for item in list_to_search:
        if string == item.lower():
            return True
            return False

# Пример вызова функций
result1 = string_info("Capybara")
print(result1)

result2 = string_info("Armageddon")
print(result2)

result3 = is_contains('Urban', ['ban', 'BaNaN', 'urBAN']) # Urban ~ urBAN)
print(result3)

result4 = is_contains('cycle', ['recycling', 'cyclic']) # No matches
print(result4)

print(calls)
