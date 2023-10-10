from bootdev.functions import (
    to_celcius,
    hours_to_seconds,
    none_fuc,
    get_user,
    become_warrior,
    get_greeting,
    level_up,
    take_magic_damage,
)


def test_take_magic_damage():
    run_cases = [
        (100, 5, 2, 20, 65),
        (200, 10, 1, 25, 185),
        (0, 0, 0, 0, 0),
        (1, 1, 1, 1, 1),
        (100, 2, 3, 1, 99),
        (2500, 3, 2, 2, 2499),
    ]

    for run_case in run_cases:
        inputs = run_case[:4]
        expected_output = run_case[4]

        level = take_magic_damage(*inputs)
        assert level == expected_output


def test_level_up():
    run_cases = [
        (1, 200, 3),
        (2, 50, 2),
    ] + [
        (0, 0, 0),
        (0, 200, 2),
        (176, 350, 179),
        (250, 100, 251),
    ]

    for run_case in run_cases:
        inputs = run_case[:2]
        expected_output = run_case[2]

        result = level_up(*inputs)
        assert result == expected_output


def test_get_greeting():
    email = "rkz.phdev@gmail.com"
    name = "raven"
    greeting = f"Hello {name}, welcome! You've register your email: {email}"
    result = get_greeting(email, name)
    assert greeting == result

    email = ""
    greeting = f"Hello there, welcome! You've register your email: {email}"
    result = get_greeting(email)
    assert greeting == result


def test_become_warrior():
    first_name = "raven"
    last_name = "paragas"
    power = 100

    warrior_name, warrior_power = become_warrior(first_name, last_name, power)

    assert f"{first_name} {last_name}" == warrior_name
    assert power == warrior_power


def test_function_multiple_return():
    email, age, is_active = get_user()

    assert email == "name@domain.com"
    assert age == 21
    assert is_active


def test_none_func():
    assert none_fuc() is None


def test_hours_to_second():
    assert hours_to_seconds(1) == 3600
    assert hours_to_seconds(2) == 7200
    assert hours_to_seconds(24) == 86400
    assert hours_to_seconds(2.5) == 9000


def test_celcius():
    assert to_celcius(100) == 38


if __name__ == "__main__":
    test_celcius(100)
