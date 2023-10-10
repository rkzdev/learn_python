# Scientific notation

# If you're not familiar with scientific notation.
# In a nutshell, the number following the e specifies how many places
# to move the decimal to the right for a positive number, or to the left
# for a negative number

print(16e3)  # Prints 16000.0
print(7.1e-2)  # Prints 0.071


# Underscores for readability
num = 16_000
print(num)  # Prints 16000

num = 16_000_000
print(num)  # Prints 16000000


def calculate_damage(sword, arrow, spear, dagger, fire):
    total_damage = sword + arrow + spear + dagger + fire
    average_damage = total_damage / 5

    return total_damage, average_damage


def test(sword, arrow, spear, dagger, fire):
    total, average = calculate_damage(sword, arrow, spear, dagger, fire)
    print(f"total damage is: {total}")
    print(f"average damage is: {average}")
    print("===================================")


def max_players_on_server():
    small = 1.024e18
    medium = 10.24e17
    large = 102.4e16

    return small, medium, large


def test_max_players_on_server():
    small, medium, large = max_players_on_server()
    print(f"{small:0f}")
    print(f"{medium:0f}")
    print(f"{large:0f}")


# Logical Operators
# You're probably familiar with the logical operators AND and OR.


def logical_operators():
    print(True and True)
    print(True and False)
    print(False and False)

    print(True or True)
    print(True or False)
    print(False or False)

    # Nesting with Parentheses
    print((True or False) and False)


# Binary Numbers
# Binary numbers are just "base 2" numbers.
def binary_numbers():
    # 0001 = 1
    # 0010 = 2
    # 0011 = 3
    # 0100 = 4
    # 0101 = 5
    # 0110 = 6
    # 0111 = 7
    # 1000 = 8
    print(0b0001)  # Prints 1
    print(0b0101)  # Prints 5


# Bitwise & Operator
def bitwise_end_operator():
    value1 = 0b0101
    value2 = 0b0111

    # 0101 = 5
    # &
    # 0111 = 7
    # ---------
    # 0101 = 5
    value3 = value1 & value2
    print(value3)

    val1 = 5
    val2 = 7
    val3 = val1 & val2
    print(val3)


def permission_using_binary():
    can_create_guild = 0b1000
    can_review_guild = 0b0100
    can_delete_guild = 0b0010
    can_edit_guild = 0b0001

    user_permission = 0b1111

    # 1111
    # &
    # 1000
    # ------
    # 1000
    user_can_create_guild = user_permission & can_create_guild

    # 1111
    # &
    # 0100
    # ------
    # 0100
    user_can_review_guild = user_permission & can_review_guild
    user_can_delete_guild = user_permission & can_delete_guild
    user_can_edit_guild = user_permission & can_edit_guild

    print(user_can_create_guild)
    print(user_can_review_guild)
    print(user_can_delete_guild)
    print(user_can_edit_guild)


def main():
    test(3, 5, 2, 1, 4)
    test(5, 5, 5, 5, 5)
    test(1, 2, 3, 4, 5)
    test(0, 0, 0, 0, 10)

    test_max_players_on_server()

    logical_operators()

    binary_numbers()

    bitwise_end_operator()

    permission_using_binary()


if __name__ == "__main__":
    main()
