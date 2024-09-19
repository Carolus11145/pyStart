import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult_data.csv')

    # Panda series with race names as the index labels:
    race_count = df['race'].value_counts()

    # The average age of men in the data set:
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Percentage of people in the data set who have a Bachelor's Degree:
    percentage_bachelors = round(df[df['education'] == 'Bachelors'].shape[0] / df .shape[0] * 100, 1)

    # Percentage of people with advanced education who make more than 50K:
    # Percentage of people without advanced education who make more than 50K:

    query1 = df['education'].isin(['Bachelors', 'Masters', 'Doctorate']) # Records those people who have an advanced education
    query2 = df['salary'] == '>50k' # Records those people who do not have an advanaced education

    higher_education_rich = round((query1 & query2).sum() / query1.sum() * 100, 1)
    lower_education_rich = round((~query1 & query2).sum() / (~query1).sum() * 100, 1)

    # Minimum number of hours a person works per week:
    min_work_hours = df['hours-per-week'].min()

    # Percentage of people who work the minimum number of hours per week and have a salary of >50K:
    query3 = df['hours-per-week'] == min_work_hours # Tracks people in the data set that 

    rich_percentage = round((query3 & query2).sum() / query3.sum() * 100, 1)

    # Country with the highest percentage of people that earn >50K:
    query4 = (df[query2]['native-country'].value_counts() \
              / df['native-country'].value_counts() * 100).sort_values(ascending=False)
    highest_earning_country = query4.index[0]
    highest_earning_country_percentage = round(query4.iloc[0], 1)

    # Most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & query2] \
                                    ['occupation'].value_counts().index[0]

    # Lines of code below this must not be modified

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
