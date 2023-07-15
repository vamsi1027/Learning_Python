# TODO: Short Circuiting
# Case 1:
is_frd = True
is_not_frd = True
if is_frd is not is_not_frd:
    print("Hey, I'm vamsi krishna")
else:
    print("Hello, I'm not a grate")
# Case 2:
is_frd = True
is_not_frd = True
if is_frd and is_not_frd:
    print("Hey, I'm vamsi krishna")
else:
    print("Hello, I'm not a grate")
# Case 3:
is_frd = True
is_not_frd = False
if is_frd is not is_not_frd:
    print("Hey, I'm vamsi krishna")
else:
    print("Hello, I'm not a grate")
