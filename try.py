
def do_something(arg1: str):
    number = 90
    print("hello")
    print(f"by the way, the argument you gave me is {arg1=}")
    print(f"which has {len(arg1)} characters")
    print(number)


do_something("Lisa")
do_something("Maya")
do_something("Papa")
do_something(arg1="Maman")

