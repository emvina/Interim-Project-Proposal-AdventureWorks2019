#What is the relationship between store trading duration and revenue? (together)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

df = pd.read_csv(r"C:\Users\vinam\Desktop\Project Adventure Works 2019\StoreDemographicsTable.csv")

print(df.head())

# I want to check the following:
# 1. is there a relationship with store trading duration and revenue via pearson correlation?
# 2. which store has the longest trading duration
# 3. which store has the highest annual revenue

#calculate the store duration first i.e.current date - year opened
#function to calculate store duration
def year_duration(year_opened):
    
    #get the current year
    current_year = datetime.now().year
    
    #calculate the duration by subtracting the store opening year from the current year
    duration = current_year - year_opened
    return duration

#get the year in data
year_opened = df["YearOpened"] 

#replace with the actual year the store opened
print(f"Store duration: {year_duration(year_opened)} years")

#now adding result to a new column for better readability and easier calculations
df["Store_duration"] = df["YearOpened"].apply(year_duration)

#checking result
print(df)

#now I want to check whether high store duration equals to high annual revenue
#calculate correlation between Year Opened and Annual Revenue
correlation = df["Store_duration"].corr(df["AnnualRevenue"])

#display the correlation result
print("Correlation Matrix:")
print(correlation)

#check if the correlation is positive or negative and analyze the relationship
if correlation > 0:
    print("There is a positive correlation between Store Duration and Annual Revenue.")
elif correlation < 0:
    print("There is a negative correlation between Store Duration and Annual Revenue.")
else:
    print("There is no linear correlation between Store Duration and Annual Revenue.")
#results shows that there is a negative relationship between the two variables
#there could be other factors or non-linear relationship but in terms of correlation, it's negative
#visualising the data points on a scatter plot
plt.scatter(df["Store_duration"], df["AnnualRevenue"], alpha=0.5)
plt.title("Store Duration VS Annual Revenue")
plt.xlabel("Store Duration in Years Count")
plt.ylabel("Annual Revenue")
plt.show()


#finding the longest store duration
longest_duration = df["Store_duration"].max()

#finding the row(s) with the longest store duration
longest_store = df[df["Store_duration"] == longest_duration]

#showcasing other relevant details of the store with the longest duration
detail = longest_store[["Name", "AnnualRevenue","Store_duration","YearOpened"]]
sorted_details = detail.sort_values(by = "AnnualRevenue", ascending=False)

#displaying the results
print("Longest Duration:", longest_duration)
#displaying results in a list
print("Details of the Store with Longest Duration:")
print(detail)

#displaying as a bar
plt.barh(sorted_details["Name"],sorted_details["AnnualRevenue"],color = "cornflowerblue")
plt.title("Stores with the Highest Year Duration and Annual Revenue")
plt.ylabel("Annual Revenue")
plt.xlabel("Stores with the Highest Duration")
plt.xticks(rotation=90)
plt.show()

#curious to see the overall graph for store duration and annual revenue
#using group by to group the years of duration and sum the annual revenue for each duration year
count_store = df.groupby("Store_duration")["AnnualRevenue"].sum()
#using line plot this time to get a clearer insight
#.index will show unique store duration values
#.values contains the summed annual revenue for each store duration
plt.plot(count_store.index, count_store.values, color = "red", marker = "o")
plt.title("Stores with Year Duration and Annual Revenue")
plt.ylabel("Annual Revenue")
plt.xlabel("Stores with the Year Duration")
plt.show()

#output shows that stores with store duration of 25/26 years have the highest revenues
#it also showed that every 5-7 years onwards, there is a bit of jump in revenues