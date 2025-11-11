import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
data_set = pd.read_csv("Heart disease prediction.csv")
data_set["male"] = data_set["male"].replace({1: "MALE", 0: "FEMALE"})
data_set = data_set.rename(columns={'male': 'Gender'})
data_set["currentSmoker"] = data_set["currentSmoker"].replace({1: "smoker", 0: "not a smoker"})
data_set['glucose'] = data_set['glucose'].fillna(data_set['glucose'].median())
data_set["TenYearCHD"] = data_set["TenYearCHD"].replace({1: "heart disease", 0: "probably healthy"})

# Count the number of males and females
male_count = data_set["Gender"].value_counts().get("MALE")
female_count = data_set["Gender"].value_counts().get("FEMALE")
print(f"In our sheet we have: {male_count} MALES and {female_count} FEMALES")

# Calculate the total count and average glucose level
total_counts = female_count + male_count
glucose_level = data_set["glucose"].mean()
average_glucose_by_gender = data_set.groupby('Gender')['glucose'].mean()

# Count the number of individuals with heart disease by gender
ten_year_chd_counts = data_set.groupby('Gender')['TenYearCHD'].value_counts()

# Filter the DataFrame for smokers
smokers = data_set[data_set["currentSmoker"] == "smoker"]

# Group by Gender and calculate the average number of cigarettes per day for smokers
cigs_per_day_for_smokers = smokers.groupby("Gender")["cigsPerDay"].mean()

# Count the number of smokers by gender
smokers_count = data_set.groupby('Gender')["currentSmoker"].value_counts().loc[:, "smoker"]

print("_______________________________________________")
print(f"The average glucose level is {glucose_level}")
print("_______________________________________________")
print("Average glucose levels by gender:")
print(average_glucose_by_gender)
print("_______________________________________________")
print("Heart disease counts by gender:")
print(ten_year_chd_counts)
print("_______________________________________________")
print("Average cigarettes per day for smokers by gender:")
print(cigs_per_day_for_smokers)
print("_______________________________________________")
print("Number of smokers by gender:")
print(smokers_count)

# Plotting the combined chart
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar plot for the number of smokers
ax1.bar(smokers_count.index, smokers_count.values, color='blue', alpha=0.6, label='Number of Smokers')
ax1.set_xlabel('Gender')
ax1.set_ylabel('Number of Smokers', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Adding the second y-axis for the average cigarettes per day
ax2 = ax1.twinx()
ax2.plot(cigs_per_day_for_smokers.index, cigs_per_day_for_smokers.values, color='orange', marker='o', linestyle='-', linewidth=2, label='Avg Cigs Per Day')
ax2.set_ylabel('Average Cigarettes Per Day', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

# Adding the third y-axis for the ten-year CHD counts
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ten_year_chd_healthy = ten_year_chd_counts[:, 'probably healthy']
ten_year_chd_disease = ten_year_chd_counts[:, 'heart disease']
ax3.plot(ten_year_chd_healthy.index, ten_year_chd_healthy.values, color='green', marker='x', linestyle='--', linewidth=2, label='Probably Healthy')
ax3.plot(ten_year_chd_disease.index, ten_year_chd_disease.values, color='red', marker='x', linestyle='--', linewidth=2, label='Heart Disease')
ax3.set_ylabel('Ten-Year CHD Counts', color='green')
ax3.tick_params(axis='y', labelcolor='green')

# Adding a title and legend
fig.suptitle('Comparison of Smokers, Avg Cigarettes Per Day, and Ten-Year CHD by Gender')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax3.legend(loc='center right')

plt.show()
