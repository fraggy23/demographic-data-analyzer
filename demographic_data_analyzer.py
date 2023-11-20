import pandas as pd


def calculate_demographic_data(print_data=True):
  # Read data from file
  df = pd.read_csv('adult.data.csv')

  # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  race_count = df['race'].value_counts()

  # What is the average age of men?
  filt1 = df['sex'] == 'Male'
  df_male_age = df['age'].where(filt1)
  average_age_men = round(float(df_male_age.mean()), 1)

  # What is the percentage of people who have a Bachelor's degree?
  filt2 = df['education'] == 'Bachelors'
  percentage_bachelors = round(
      df['education'].where(filt2).count() / df['education'].count() * 100, 1)

  # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
  # What percentage of people without advanced education make more than 50K?

  filt3 = df['salary'] == '>50K'
  filt3a = (df['education'] == 'Bachelors') | (
      df['education'] == 'Masters') | (df['education'] == 'Doctorate')

  # with and without `Bachelors`, `Masters`, or `Doctorate`
  higher_education = df['education'].where(filt3a).count()
  lower_education = df['education'].where(~filt3a).count()
  total = len(df.index)
  # percentage with salary >50K
  higher_education_rich = round(
      df['education'].where(filt3 & filt3a).count() / higher_education * 100,
      1)
  lower_education_rich = round(
      df['education'].where(filt3 & ~filt3a).count() / lower_education * 100,
      1)

  # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = df['hours-per-week'].min()

  # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  num_min_workers = df[(df['hours-per-week'] == min_work_hours) & filt3]

  rich_percentage = round(
      len(num_min_workers.index) /
      len(df[(df['hours-per-week'] == min_work_hours)].index) * 100, 1)

  # What country has the highest percentage of people that earn >50K?

  highest_country = round(
      df.loc[df['salary'] == '>50K'].value_counts('native-country') /
      df.value_counts('native-country') * 100, 1)

  highest_earning_country = highest_country.idxmax()
  highest_earning_country_percentage = highest_country.max()

  # Identify the most popular occupation for those who earn >50K in India.
  highest_india = df.loc[(df['salary'] == '>50K')
                        & (df['native-country'] == 'India')]
  top_IN_occupation = highest_india['occupation'].value_counts().idxmax()

  # DO NOT MODIFY BELOW THIS LINE

  if print_data:
    print("Number of each race:\n", race_count)
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print("higher education", higher_education)
    print("lower education", lower_education)
    print("total", total)
    print(
        f"Percentage with higher education that earn >50K: {higher_education_rich}%"
    )
    print(
        f"Percentage without higher education that earn >50K: {lower_education_rich}%"
    )
    print(f"Min work time: {min_work_hours} hours/week")
    print(
        f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
    )
    print("Country with highest percentage of rich:", highest_earning_country)
    print("highest_country", highest_country)
    print(
        f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
    )
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
      'highest_earning_country_percentage': highest_earning_country_percentage,
      'top_IN_occupation': top_IN_occupation
  }
