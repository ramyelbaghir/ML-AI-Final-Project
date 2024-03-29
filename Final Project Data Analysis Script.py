# Final Project Data Analysis

import pandas as pd
import numpy as np
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt

composers = pd.read_csv('classical_composers.csv', encoding='ISO-8859-1')
census_1790 = pd.read_csv('usa_household_census_1790.csv')
dating = pd.read_csv('Speed Dating Data.csv', encoding='ISO-8859-1')
music_mental = pd.read_csv('mxmh_survey_results.csv')

print(len(music_mental))
###
# Scope: Looking for correlations outside of music genre with lower self-reported mental health issues.
# Scope: What can people do with regards to their music listening habits to help alleviate feelings of OCD, insomnia, anxiety or depression?
# 1. Identify survey variables that are reasonably changeable by the participant (e.g. number of hours listened, playing an instrument, listening while working, etc.)
# 2. Look for correlations between these variables and reported levels of insomnia, anxiety, depression, and OCD.
# 3. Identify survey variables that are relatively FIXED in the participant (e.g., age, favorite genre, etc.)
# 4. Look for correlations between these variables and reported levels of insomnia, anxiety, depression, and OCD.
# 5. Report findings and draw conclusions.
# 6. Answer the question of the Scope.

print(music_mental.columns)
changeable_categorical = ['Primary streaming service', 'While working', 'Instrumentalist', 'Composer', 'Exploratory', 'Foreign languages']
changeable_numerical = ['Hours per day']
fixed_categorical = ['Fav genre']
fixed_numerical = ['Timestamp', 'BPM']

mental_outcomes = ['Anxiety', 'Insomnia', 'Depression', 'OCD']
print(music_mental.Age.describe())
#print(music_mental.Anxiety.describe())
#print(music_mental.Insomnia.describe())
#print(music_mental.Depression.describe())
#print(music_mental.OCD.describe())
"""
for outcome in mental_outcomes:
    for column in changeable_categorical:
        sns.boxplot(data=music_mental, x = column, y = outcome, palette='bright')
        #plt.show()
    for column in fixed_categorical:
        sns.boxplot(data=music_mental, x = column, y = outcome, palette='bright')
        #plt.show()
    for column in changeable_numerical:
        plt.scatter(x=music_mental[column], y=music_mental[outcome])
        plt.xlabel(column)
        plt.ylabel(outcome)
        #plt.show()
    for column in fixed_numerical:
        plt.scatter(x=music_mental[column], y=music_mental[outcome])
        plt.xlabel(column)
        plt.ylabel(outcome)
        #plt.show()

# Noticed very few statistically significant differences across all variables with mental heatlh outcomes. Gospel and Latin listeners had comparitively low rates of depression on average.
"""

"""
for column in changeable_categorical:
    sns.boxplot(data=music_mental, x = music_mental.Age, y = column, palette='bright')
    plt.show()
for column in fixed_categorical:
    sns.boxplot(data=music_mental, x = music_mental.Age, y = column, palette='bright')
    plt.show()
for column in changeable_numerical:
    plt.scatter(x=music_mental['Age'], y=music_mental[column])
    plt.xlabel('Age')
    plt.ylabel(column)
    plt.show()
for column in fixed_numerical:
    plt.scatter(x=music_mental['Age'], y=music_mental[column])
    plt.xlabel('Age')
    plt.ylabel(column)
    plt.show()
"""    

#print(music_mental[music_mental.isnull().any(axis=1)])

music_mental_nonnull = music_mental.dropna()

#print(music_mental_nonnull.info())
#corr_age_anxiety, p = stats.pearsonr(music_mental_nonnull.Age, music_mental_nonnull.Anxiety)
#corr_age_insomnia, p = stats.pearsonr(music_mental_nonnull.Age, music_mental_nonnull.Insomnia)
#corr_age_depression, p = stats.pearsonr(music_mental_nonnull.Age, music_mental_nonnull.Depression)
#corr_age_OCD, p = stats.pearsonr(music_mental_nonnull.Age, music_mental_nonnull.OCD)
#print(corr_age_anxiety)
#print(corr_age_insomnia)
#print(corr_age_depression)
#print(corr_age_OCD)

gospel = music_mental[music_mental['Fav genre'] == 'Gospel']

print(gospel['Age'].describe())
for outcome in mental_outcomes:
    print("Stats of gospel listeners' {0} scores:".format(outcome))
    print(gospel[outcome].describe())
    print("Stats of general sample's {0} scores:".format(outcome))
    print(music_mental[outcome].describe())

#TO DO: Create data viz comparing mental outcomes in gospel listeners compared with general sample.

for outcome in mental_outcomes:
    gospel_outcomes = gospel[outcome]
    general_outcomes = music_mental[outcome]

    plt.hist(gospel_outcomes, color='red', label=('Gospel {0} Scores'.format(outcome)), density=True, alpha=0.5)
    plt.hist(general_outcomes, color='blue', label=('General {0} Scores'.format(outcome)), density=True, alpha=0.5)
    plt.legend()
    plt.show()

# Very weak negative correlations between age and mental health outcomes.


# Standard error of gospel and latin listeners' average mental health outcomes?
# Standard error = population standard deviation / sqrt(sample size)

# Correlations with age as an independent variable and its potential effects on other variables?
# Mean age of gospel listeners is significantly higher than the sample mean.
# Mean age of Pandora users is significantly higher than ages of other music services.
    
# Conclusions:
# 1. According to the data, there are no strong correlations between the variables measured and reported levels of anxiety, insomnia, depression and OCD.
# 2. There seems to be some connection with favorite genre being gospel music, being much older than the average sample age, and comparatively lower reported
#    levels of anxiety and depression with comparatively higher reported levels of insomnia. However, these values are largely within one standard deviation of the corresponding
#    sample means.
# 3. The higher levels of insomnia may be more connected to being older in age than being connected to listening to gospel.
# 4. The lower levels of anxiety and depression may be connected to stronger religious faith or a sense of existential purpose that would make people more likely to prefer gospel music.