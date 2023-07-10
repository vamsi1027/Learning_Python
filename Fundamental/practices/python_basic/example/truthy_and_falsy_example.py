# =================================================================================
# TODO : Truthy and Falsy
# https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false

# TODO Case 1:
is_boolean = "vamsi"
is_int = 123
if is_boolean and is_int:
    print("Yes, I'm executed")
else:
    print("No, I'm not able to executed right now")

# TODO Case 2:
print(bool(123))
print(bool(''))
print(bool(0))