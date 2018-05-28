"""Introduction to pandas library

Requires:
    pandas
    matplotlib
    numpy

https://colab.research.google.com/notebooks/mlcc/intro_to_pandas.ipynb
"""

import pandas as pd
import numpy as np


city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

cities = pd.DataFrame({'City name': city_names, 'Population': population})
print(cities)

# california_housing_dataframe = pd.read_csv(
#     "https://storage.googleapis.com/mledu-datasets/"
#     "california_housing_train.csv", sep=",")

# print(california_housing_dataframe.describe())
# print(california_housing_dataframe.head())

# print(california_housing_dataframe.hist('housing_median_age'))

print(type(cities['City name']))
print(cities['City name'])

print(type(cities['City name'][1]))
print(cities['City name'][1])

print(type(cities[0:2]))
print(cities[0:2])

print(population / 1000)

print(np.log(population))

print(population.apply(lambda val: val > 1000000))

cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = (cities['Population'] /
                                cities['Area square miles'])
print(cities)


# Exercise #1:
#
#    Modify the cities table by adding a new boolean column that is True if
#    and only if both of the following are True:
#
#        * The city is named after a saint.
#        * The city has an area greater than 50 square miles.
#
#    Note: Boolean Series are combined using the bitwise, rather than the
#          traditional boolean, operators. For example, when performing
#          logical and, use & instead of and.
#
#    Hint: "San" in Spanish means "saint."

cities['Is large and saint named'] = (
    (cities['Area square miles'] > 50) &
    (cities['City name'].apply(lambda name: name.startswith('San')))
)
print(cities)

# End Exercise #1

print(city_names.index)
print(cities.index)

print(cities.reindex([2, 0, 1]))

print(cities.reindex(np.random.permutation(cities.index)))

# Exercise #2
#
#   The reindex method allows index values that are not in the original
#   DataFrame's index values. Try it and see what happens if you use such
#   values! Why do you think this is allowed?

print(cities.reindex([0, 4, 5, 2]))

# End Exercise #2
