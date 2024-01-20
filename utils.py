import pandas as pd 
# import sklearn.

class preprocessing:
    def creation_data(self, path_csv):
        df = pd.read_csv(path_csv)
        return df
    
    def declaration_var(self, data, target):
        target_1 = data[target]
        features = data.drop(target, axis=1)
        names_f = {name:set() for name in features}
        for i in features:
            for j in features[i]:
                names_f[i].add(j)
        for i in features:
            index_drop = features[i][features[i].isnull() == True].index
            features.drop(index_drop, inplace = True)
        
        return target_1, features
    

    
    
data = preprocessing().creation_data('Salary_Data.csv')
target, features = preprocessing().declaration_var(data, 'Salary')
# print(data.info())






print(features.isnull().sum())
print(len(features['Age']))
# print(data.info())
