
class Phone:

    def __init__(self, brand, model, issue_year):

        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def receive_call(self, caller_name):

        self.caller_name = caller_name
        print(f'<{self.brand}-{self.model}> - Звонит {caller_name} ')


    def get_info(self):

        return (self.brand, self.model, self.issue_year)

    def __str__(self):

        print(f'Бренд: {self.brand}')
        print(f'Модель: {self.model}')
        print(f'Год выпуска: {self.issue_year}')



my_phone = Phone('Apple', 'iPhone 16 Pro', 2024)

my_phone.receive_call('Лера и Юля')
my_phone.__str__()

print(my_phone.get_info())
