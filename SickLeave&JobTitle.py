#What is the relationship between sick leave and Job Title (PersonType)? (vina)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"C:\Users\vinam\Desktop\Project Adventure Works 2019\SickLEave&JobTitleTable.csv")

print(df.head())

# I want to check the following:
# 1. does sick leave hours increase the higher the job title?
# 2. does males take more sick leave than females?
# 3. which jobtitles has more sick leave hours?
# 4. who has taken the most sick leave hours?
# 5. which persontype has the most sick leave?

#total employees using len() since its a string
total_employees = len(df["PersonType"]) 

#total sick leave hours using sum() since its an int
sickleave_total = df["SickLeaveHours"].sum()  

#average sick leave amongst employees
avg_sickleave = sickleave_total/total_employees 

#display result
print("Average sick leave hours: ",avg_sickleave)
print("Total Employees: ",total_employees)

#displaying the number of employees and their person type
em_employees = df[df["PersonType"]== "EM"]
other_employees = df[df["PersonType"]!= "EM"]
print("PersonType that is EM totals: ",len(em_employees))
print("PersonType that is not EM totals: ",len(other_employees))

# x = df["SickLeaveHours"]
# y = df["PersonType"]

# pearson = x.corr(y)
# print(pearson)

# spearmans = x.corr(y, method="spearman")
# print(spearmans)

# kendalls = x.corr(y, method="kendall")
# print(kendalls)

#the above code does not work as person type is a string - needs to be converted to int/float so using cat.codes to asign an int to each person type
df["PersonTypeEncoded"] = df["PersonType"].astype("category").cat.codes

#calculate correlation between PersonType (encoded) and SickLeaveHours
correlation = df["PersonTypeEncoded"].corr(df["SickLeaveHours"])

#display the correlation result
print("Correlation Matrix:")
print(correlation)
#results shows that there is a weak negative relationship between the two variables as the results is close to zero
#there could be other factors or non-linear relationship but in terms of correlation, it's weak
#visualising the data points on a scatter plot
plt.scatter(df["PersonTypeEncoded"], df["SickLeaveHours"], alpha=0.5)
plt.title("PersonType vs SickLeaveHours")
plt.xlabel("PersonType (Encoded)")
plt.ylabel("SickLeaveHours")
plt.show()
#still shows no linear relationship and it showcases that there are only 2 types of persontype which is why there is no correlation

#checking how many entries are above the average with corresponding job title instead
#filtering to group it by job title and have sick leave hours equal or above average
count_sickleave = df.groupby(["JobTitle"]) and df[df["SickLeaveHours"]>=avg_sickleave]
print("Total sick leave entries above average is:")

#using len() to get total entries for sick leave hours above average for job title
print(len(count_sickleave))

#sorting out the result in order with ascending values of sick leave hours with 80 being the highest
sickleave_sorted = count_sickleave.sort_values(by= "SickLeaveHours", ascending=False)

#displaying result in a barchart for better readability
plt.barh(sickleave_sorted["JobTitle"],sickleave_sorted["SickLeaveHours"],color = "cornflowerblue")
plt.title('Sick Leave Hours by Job Title')
plt.ylabel('Job Title')
plt.xlabel('Sick Leave Hours')
plt.show()
print(sickleave_sorted)

#using the same methods as persontype above, I want to see if there is a correlation between job title and sick leave
df["JobTitleEncoded"] = df["JobTitle"].astype("category").cat.codes

#calculate correlation between JobTitle (encoded) and SickLeaveHours
correlation_j = df["JobTitleEncoded"].corr(df["SickLeaveHours"])

#display the correlation result
print("Correlation Matrix:")
print(correlation_j)

#results shows that there is still a weak negative relationship between the two variables as the results is close to zero
#there could be other factors or non-linear relationship but in terms of correlation, it's weak
#visualising the data points on a scatter plot
plt.scatter(df["JobTitleEncoded"], df["SickLeaveHours"], alpha=0.5)
plt.title("JobTitle vs SickLeaveHours")
plt.xlabel("JobTitle (Encoded)")
plt.ylabel("SickLeaveHours")
plt.show()

#curious on the gender comparison for this as well
#gender analysis for above average sick leave entries 
male_count = count_sickleave["Gender"].value_counts()["M"]
female_count = count_sickleave["Gender"].value_counts()["F"]
print("Male count for sick leave entries:",male_count)
print("Female count for sick leave entries:",female_count)

#display analysis as bar chart
#creating a new DataFrame for plotting
gender_data = pd.DataFrame({
    "Gender": ["Male", "Female"],
    "Count": [male_count, female_count]
})
#create a bar plot using seaborn
sns.barplot(x="Gender", y="Count", data=gender_data, color = "pink")

#add titles and labels
plt.title("Gender Comparison for Sick Leave Entries")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()



