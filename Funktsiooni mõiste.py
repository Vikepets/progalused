# Inside the function
def func():
    print("im inside the function")
func()
func()
func()

# My name is
name = "Naatan"
def my_name_is(Naatan):
    print(f"my name is, {name}")
my_name_is("Naatan")

# Sum six
def sum_six(num):
    return 6 + num

print(sum_six(1))
print(sum_six(6))

#Sum numbers

def sum_numbers(a, b):
    return a + b

print(sum_numbers(5, 5))
print(sum_numbers(0, 25))

#USD to EUR
def usd_to_euro(dollar):
    return round(dollar * 0.8)

print(usd_to_euro(100))
print(usd_to_euro(70))