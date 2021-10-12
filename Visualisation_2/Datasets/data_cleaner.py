import pandas as pd

employed = pd.read_csv("C:/Users/user/Desktop/FIT3179/FIT3179/Visualisation_2/Datasets/Employed_person_by_sex_and_state_1982_to_2020_Malaysia.csv")

employed.loc[(employed["state"] == "Pulau Pinang"), "state"] = "Penang"
print(employed)

x = employed[employed['state']=='Penang']
print(x)

employed.to_csv(r"C:\Users\user\Desktop\FIT3179\FIT3179\Visualisation_2\Datasets\Employed_person_by_sex_and_state_1982_to_2020_Malaysia.csv", index = False)
