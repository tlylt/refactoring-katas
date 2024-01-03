# Thoughts

# The trigger for primitive obsession refactoring might come from
# primitives taken in from the constructor, and is later manipulated
# in different ways across multiple functions.

# The procedure for the refactoring is quite standard, by
# 1. encapsulate variable/field
# 2. Replace Primitive with Object
# 3. Move Function

# 1. encapsulate-field: no longer directly retrieve field, but via getter
# this is to faciliate changing out of the primitive with a class, while
# the getter can still be used to retrieve the primitive version if needed
# may need to rename getter

# 2. replace-primitive-with-object: first by creating a class that takes in
# the primitive field and storing it, then replace the original usage with
# instantiating of this new class and update the original getter to use the
# new class's getter. May need to move any primitive processing logic in 
# the original class to the constructor of the new class

# 3. move-function: the new class is a good place to store functions that work
# on the primitive value, hence move them from the original class over, and update
# the function call to indirectly call the new class's function. Note that it could
# become a code smell if there's over-delegation, meaning if the entire class just delegates
# all functions and do nothing


class PersonalNumber:
    def __init__(self, personal_number: str):
        personal_number = personal_number.replace("-", "")
        if personal_number.__len__() != 12:
            raise ValueError("invalid personal number " + personal_number)
        self.personal_number = personal_number
    def __str__(self) -> str:
        return self.personal_number
    def get_birth_year(self) -> int:
        # works for swedish PN
        year = self.personal_number[0:4]
        return int(year)


class PhoneNumber:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
    def __str__(self) -> str:
        return self.phone_number
    def get_country_code(self) -> str:
        code = ""
        if self.phone_number.startswith("00"):
            code = self.phone_number[2:4]
        elif self.phone_number.startswith("+"):
            code = self.phone_number[1:3]
        if code != "":
            return "+" + code
        return ""        


class Role:
    def __init__(self, role: int):
        if role < 0 or role > 4:
            raise ValueError("illegal role " + role)
        self.role = role
    def can_delete_users(self) -> bool:
        return self.role == Person.USER_ROLE_MANAGER or self.role == Person.USER_ROLE_ADMIN


class Person:
    USER_ROLE_ADMIN = 0
    USER_ROLE_ENGINEER = 1
    USER_ROLE_MANAGER = 2
    USER_ROLE_SALES = 3
    def __init__(self, role: int, swedish_personal_number: str, phone_number: str):
        self.role = Role(role)
        self.swedish_personal_number = PersonalNumber(swedish_personal_number)
        self.phone_number = PhoneNumber(phone_number)

    def get_swedish_personal_number_str(self) -> str:
        return str(self.swedish_personal_number)

    def get_phone_number_str(self) -> str:
        return str(self.phone_number)

    def birth_year(self) -> int:
        return self.swedish_personal_number.get_birth_year()

    def country_code(self) -> str:
        return self.phone_number.get_country_code()

    def can_delete_users(self) -> bool:
        return self.role.can_delete_users()