class DataScientist:
    def __init__(self, name, skills):
        self.name = name
        self.skills=skills

    def show_info(self):
        print(f"{self.name} knows {','.join(self.skills)}.")

import pandas as pd

class Dataset: 
    def __init__(self, filepath):
        self.df=pd.read_csv(filepath)

    def summary(self):
        return self.df.describe()
    
    def missing_values(self):
        return self.df.isnull().sum()

ds1= DataScientist("Aditya",["python","pandas","Machine Learning"])

# Using a custom index (labels)
scores = pd.Series([0.85, 0.90, 0.78], index=['Model A', 'Model B', 'Model C'])
print(scores['Model B'])  # Access value by label


data = Dataset("C:/Users/91749/Downloads/fortune1000.csv")
print(data.summary())
print(data.missing_values())
ds1.show_info()

    