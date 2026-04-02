from typing import Any, Sized


def assert_status_code(actual: int, expected: int):
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


def assert_is_true(actual: Any, name: str):
    """
    Проверяет, что фактическое значение является истинным.

    :param actual: Фактическое значение
    :param name: Название проверяемого значения.
    :raises AssertionError: Если фактическое значение ложно.
    """
    assert actual, f"Incorrect value {name}." f"Expected true value but got {actual}"


def assert_length(actual: Sized, expected: Sized, name: str):
    """
    Проверяет, что длины двух объектов совпадают.

    :param name: Название проверяемого объекта.
    :param actual: Фактический объект.
    :param expected: Ожидаемый объект.
    :raises AssertionError: Если длины не совпадают.
    """
    assert len(actual) == len(expected), (
        f'Incorrect object length: "{name}". '
        f"Expected length: {len(expected)}. "
        f"Actual length: {len(actual)}"
    )
