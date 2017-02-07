"""Prime numbers module."""


def prime_numbers(number):
    """Function to generate prime numbers within given range."""

    prime_nos = []

    if number in (0, 1):
        return "Zero and One are not prime numbers"

    if number < 2:
        return "Not possible to generate prime numbers for integers less than 2."

    if type(number) != int:
        return "Only integers are allowed."

    for i in range(2, number + 1):
        if i > 1:
            for x in range(2, i):
                if (i % x) == 0:
                    break
            else:
                prime_nos.append(i)
    return prime_nos
