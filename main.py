from utils import preprocessing

data = preprocessing().creation_data('Salary_Data.csv')
target, features = preprocessing().declaration_var(data, 'Salary')
print(data.info())