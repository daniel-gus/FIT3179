import pandas as pd


employed = pd.read_csv("C:/Users/user/Desktop/FIT3179/FIT3179/Visualisation 2 Datasets/Employed person by sex and state 1982 to 2020 Malay.csv")

#Group by two keys and then summarize each group
employed_population =  employed.groupby(['State/Country'],as_index=False).agg(sum_employed=('Employed (\'000)', 'sum'))
print(employed_population)

employed_population.to_csv(r"C:\Users\user\Desktop\FIT3179\FIT3179\Homework Week 9\Week 9 Homework Choropleth Map\cleaned Employed person by sex and state 1982 to 2020 Malay.csv", index = False)
