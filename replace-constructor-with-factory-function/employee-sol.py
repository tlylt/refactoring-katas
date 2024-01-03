# Can create a generate factory method still, which is simply
# a replacement of the constructor in cases where a standard
# function is preferred.

# On top of the generic factory, create specialized factory
# methods for specific cases
class Employee:
    def __init__(self, name:str, type_code:str):
        self._name = name
        self._type_code = type_code
    def create(name:str, type_code:str):
        return Employee(name, type_code)
    def create_engineer(name:str):
        return Employee(name, "E")

candidate = Employee.create(document.name, document.empType)
engineer = Employee.create_engineer(document.name)