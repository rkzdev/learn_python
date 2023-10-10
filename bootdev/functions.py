# Functions
# def area_of_ricle(r):
#     return 3.14 * r * r


# player1_area = area_of_ricle(1)
# player2_area = area_of_ricle(0.5)

# print(f"Player 1 has an attack area of {player1_area} square meters")
# print(f"Player 2 has an attack area of {player2_area} square meters")


# Multiple Parameters
# def calculate_damage(enemy_one_dmg, enemy_two_dmg, enemy_three_dmg):
#     return enemy_one_dmg + enemy_two_dmg + enemy_three_dmg


# print(f"You dealt {calculate_damage(2, 3, 4)} points of damage!")
# print(f"You dealt {calculate_damage(-1, 4, 3)} points of damage!")
# print(f"You dealt {calculate_damage(3, 2, 4)} points of damage!")
# print(f"You dealt {calculate_damage(1, 4, 2)} points of damage!")

# Where to declare Functions

# does not work
# print(my_name)
# my_name = "Lane Wagner"

# it needs to be:
# my_name = "Lane Wagner"
# print(my_name)

# Order of Functions


# def main():
#     func2()


# def func2():
#     func3()


# def func3():
#     print("I'm function 3")


# call entry point last
# main()

# Function Practice-Degrees


def to_celcius(f):
    return round(5 / 9 * (f - 32))


def hours_to_seconds(h):
    return h * 60 * 60


# None return
# When no return value is specified in a function, it will return None.
def none_fuc():
    print("I do nothing")
    return None


# Multiple return values

# In python, we can return more than one value from a function.
# All we need to do is separate each value we are returning by a comma,
# and when we cal lthe function, we need to capture all the returned values
# in individual variables.


def get_user():
    return "name@domain.com", 21, "active"


def become_warrior(first_name, last_name, power):
    return f"{first_name} {last_name}", power


# Parameters vs Arguments
# Parameters are the names used for inputs when defining a function.
# Arguments are the names of the inputs supplied when a function is called.


# Default values for functions arguments in python


def get_greeting(email, name="there"):
    return f"Hello {name}, welcome! You've register your email: {email}"


# Local Scope
# When we create variables in a function, that data is not available outside of that function

# Global Scope
# When we define a variable or a function, that name is accessible in every
# other place in our program, even within other functions.


def level_up(level, xp_to_add):
    return level + (xp_to_add // 100)


def take_magic_damage(health, resist, amp, spell_power):
    maximum_damage = (spell_power * amp) - resist
    return health - maximum_damage


# def main():
#     run_cases = [
#         (1, 200, 3),
#         (2, 50, 2),
#     ] + [
#         (0, 0, 0),
#         (0, 200, 2),
#         (176, 350, 179),
#         (250, 100, 251),
#     ]

#     for run_case in run_cases:
#         inputs = run_case[:2]
#         expected_output = run_case[2]

#         print(inputs, expected_output)

#         result = level_up(*inputs)
#         assert result == expected_output


# if __name__ == "__main__":
#     main()

# def test(input1, input2, result):
#     total = input1 + input2

#     if total == result:
#         print("Pass")
#     else:
#         print("Fail")

# args = (1, 2, 3)
# test_cases = [
#     (1, 2, 3),
#     (4, 5, 6),
# ]

# for t in test_cases:
#     print(t)
#     test(*t)
