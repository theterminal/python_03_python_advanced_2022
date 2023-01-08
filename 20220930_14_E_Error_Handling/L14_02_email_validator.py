# 20220930 - Python - Python Advanced - Error Handling
# 02 - Email Validator - judge: No judge for this problem


# _______________ version 1 _________________


from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


# class for additional test 2
class MoreThanOneAtSymbolError(Exception):
    pass


# class for additional test 1
class InvalidNameError(Exception):
    pass


pattern_name = r'[\w+\.]+'
pattern_domain = r'\.[a-z]+'
valid_domains = ['.com', '.bg', '.org', '.net']

email = input()
while email != 'End':

    try:
        # additional test 1
        if email.count('@') > 1:
            raise MoreThanOneAtSymbolError('Email must contain only one "@" symbol!')

        elif len(findall(pattern_name, email.split('@')[0])[0]) <= 4:
            raise NameTooShortError('Name must be more than 4 characters')

        # additional test 2
        elif len(findall(pattern_name, email.split('@')[0])[0]) != len(email.split('@')[0]):
            raise InvalidNameError('Email name must contain only letter, numbers, underscores and dots!')

        elif '@' not in email:
            raise MustContainAtSymbolError('Email must contain @')

        elif findall(pattern_domain, email.split('@')[1])[0] not in valid_domains:
            raise InvalidDomainError(f'Domain must be one of the following: {", ".join(valid_domains)}')

        print('Email is valid!')

    except IndexError:
        print('Invalid email')

    email = input()
