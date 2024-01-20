import pandas as pd 

class preprocessing:
    def creation_data(self, path_csv):
        df = pd.read_csv(path_csv)
        return df
    
    def declaration_var(self, data, target):
        target_1 = data[target]
        features = data.drop(target, axis=1)
        return target_1, features
    
    
    

data = preprocessing().creation_data('Salary_Data.csv')
target, features = preprocessing().declaration_var(data, 'Salary')


print(target, features)

# print(data.info())
