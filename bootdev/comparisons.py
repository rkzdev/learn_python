# Comparison Operators

# < "less than"
# > "greater than"
# <= "less than or equal to"
# >= "greater than or equal to"
# == "equal to"
# != "not equal to"


def player_1_wins(player_1_score, player_2_score):
    return player_1_score > player_2_score


def test_player_1_wins(p1_score, p2_socre):
    result = player_1_wins(p1_score, p2_socre)

    if result:
        print("Player1 Wins")
        return
    else:
        print("Player2 Wins")
        return


def check_sword_for_army(number_of_sword, number_of_soldier):
    if number_of_sword == number_of_soldier:
        print("corrent amount")
        return
    print("incorrect amount")


def player_status(health):
    if health <= 0:
        return "dead"

    if health <= 5:
        return "injured"
    else:
        return "healthy"
    # if health <= 0:
    #     return "dead"
    # elif health <= 5:
    #     return "injured"
    # else:
    #     return "healthy"


def check_high_score(
    current_player_name, high_scoring_player_name, low_scoring_player_name
):
    if current_player_name == high_scoring_player_name:
        return "high"
    elif current_player_name == low_scoring_player_name:
        return "low"

    return "neither"


def does_attack_hit(attack_roll: int, armor_class: int):
    return (attack_roll != 1 and attack_roll > armor_class) or attack_roll == 20


def boolean_quiz():
    is_tall = True
    is_fat = True
    is_skinny = False
    is_short = False

    result = (is_tall and is_fat) or (is_skinny and is_short)
    print(result)


def should_server_customer(age, on_break, time):
    return age >= 21 and on_break and (time > 5 and time < 10)


def check_parking_meter(time_parked, time_purchased):
    if time_parked >= time_purchased:
        return "overtime charged"
    else:
        return "no charges yet"


def combat_evaltuation(player_power: int, enemy_defense: int):
    advantage, disadvantage, evenly_matched = False, False, False

    advantage = player_power > enemy_defense

    disadvantage = player_power < enemy_defense

    evenly_matched = player_power == enemy_defense

    return advantage, disadvantage, evenly_matched


def test_combat_evaluation(
    input1, input2, expected_output1, expected_output2, expected_output3
):
    print("-" * 40)
    print(f"Inputs: {input1}, {input2}")
    print(f"Expecting: {expected_output1}, {expected_output2}, {expected_output3}")
    result = combat_evaltuation(input1, input2)
    print(f"Actual: {result}")
    if result == (expected_output1, expected_output2, expected_output3):
        print("Pass")
        return True
    print("Fail")
    return False


def has_enough_gas(gallons_in_car, miles_to_work, miles_per_gallon):
    return gallons_in_car >= ((miles_to_work * 2) // miles_per_gallon)


def test_has_enough_gas(input1, input2, input3, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}")
    print(f"Expecting: {expected_output}")
    result = has_enough_gas(input1, input2, input3)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    run_cases = [
        (8, 105, 22, True),
        (10, 105, 22, True),
        (3, 105, 22, False),
        (1, 1, 1, True),
        (2, 1, 1, True),
        (1, 2, 1, False),
    ]

    for case in run_cases:
        test_has_enough_gas(*case)

    # run_cases = [
    #     (101, 100, True, False, False),
    #     (50, 100, False, True, False),
    #     (100, 100, False, False, True),
    #     (150, 70, True, False, False),
    #     (80, 150, False, True, False),
    #     (0, 0, False, False, True),
    #     (1, 1, False, False, True),
    #     (1000, 500, True, False, False),
    #     (500, 1000, False, True, False),
    # ]

    # for case in run_cases:
    #     test_combat_evaluation(*case)

    # scores = [(5, 4), (7, 5), (3, 5)]
    # for score in scores:
    #     test_player_1_wins(*score)

    # check_sword_for_army(100, 99)

    # players_health = [0, 1, 5, 9, 7]
    # for health in players_health:
    #     print("Player is: ", player_status(health))

    # players = [
    #     ("raven", "raven", "iya"),
    #     ("kristine", "kristine", "elia"),
    #     ("raven", "iya", "raven"),
    #     ("iya", "elia", "kristine"),
    # ]

    # for player in players:
    #     print(check_high_score(*player))

    # attack_roll_and_armor = [(1, 15), (5, 3), (20, 10)]
    # for attack in attack_roll_and_armor:
    #     print(does_attack_hit(*attack))

    # boolean_quiz()

    # to_serve = [(21, True, 7), (18, True, 7)]

    # for serve in to_serve:
    #     print(should_server_customer(*serve))
    # run_cases = [
    #     (3, 4, "no charges yet"),
    #     (5, 2, "overtime charged"),
    #     (2, 2, "overtime charged"),
    #     (0, 1, "no charges yet"),
    #     (1, 1, "overtime charged"),
    #     (100, 2, "overtime charged"),
    #     (2500, 3, "overtime charged"),
    # ]

    # for run_case in run_cases:
    #     inputs = run_case[:2]
    #     expected_output = run_case[2]

    #     result = check_parking_meter(*inputs)

    #     if result == expected_output:
    #         print(result)
    #     else:
    #         print(result)


if __name__ == "__main__":
    main()
