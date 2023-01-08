# 20220926 - Python - Python Advanced - Functions Advanced


def equal_strings(string_a, string_b, case_sensitive=True):
    if case_sensitive:
        return string_a == string_b
    return string_a.lower() == string_b.lower()


print(equal_strings('peter', 'Peter'))
print(equal_strings('peter', 'PETER', False))
