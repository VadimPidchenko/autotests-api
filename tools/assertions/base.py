from typing import Any


def assert_status_code(actual: Any, expected: Any):
    """
    Проверяет, что фактический статус код соответствует ожидаемому

    :param actual: актуальный статус код.
    :param expected: ожидаемый статус код.
    :raise AssertionError: Если статус коды не совпадают.
    """
    assert actual == expected, (
        f"Incorrect status code."
        f"Expected status code {expected}."
        f"Actual status code {actual}."
    )


def assert_equal(actual: Any, expected: Any, name: str):
    """
    Проверяет, что фактическое значение равно ожидаемому.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :param expected: Ожидаемое значение.
    :raises AssertionError: Если фактическое значение не равно ожидаемому.
    """
    assert actual == expected, (
        f"Incorrected value {name}."
        f"Actual value {actual}."
        f"Expected value {expected}."
    )