is_male = True
is_tall = False


if is_male:
    print("You are a male")
else:
    print("You are not a male")

## AND // OR

if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are neither")

if is_male or is_tall:
    print("You are a tall male or a male")
else:
    print("You are not male or tall or both")

## ELIF

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
else:
    print("You are neither")