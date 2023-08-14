import matplotlib
#print(matplotlib.__version__)
matplotlib.use('TkAgg')  # Set the desired backend before importing pyplot
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt
import seaborn as sns
#print(sns.__version__)
import pandas as pd

# lesson 2
cars = sns.load_dataset('mpg').dropna()
print(cars.shape)
print(cars.head())
#
# # `shade_lowest` has been replaced by `thresh`
# sns.kdeplot(x='horsepower', y='mpg', data=cars,
#             fill=True,
#             thresh=0.05,  # thresh =
#             cbar=True)
# sns.kdeplot(cars.horsepower, fill=True, bw_method=.1, cumulative=True)

# lesson 3
# penguins = sns.load_dataset('penguins').dropna()
# print(penguins.shape)
# print(penguins.head())
# sns.set_style('darkgrid')
# # sns.histplot(penguins.bill_length_mm)
# sns.histplot(x='bill_length_mm', data=penguins,
#              kde=True, bins=10, hue='species', element='poly')

# lesson 4 ecdfplot
# tips = sns.load_dataset('tips')
# print(tips.head())
# p = sns.ecdfplot(x='tip', data=tips, hue='day', stat='count', palette='summer')
# p.legend(['thursday', 'friday', 'saturday', 'sunday'], title='Day of week')
# plt.axvline(4, c='black')

# lesson 5 boxplot
sns.set_style('whitegrid')
cars = cars[cars.cylinders.isin([4, 6, 8])]
print(cars.cylinders.value_counts())  # how many of each value
# sns.boxplot(x=cars.origin, y=cars.mpg)
# cars['newer_model'] = cars.model_year > 76  # new user defined category
# sns.boxplot(x='horsepower', y='origin', hue='newer_model',
#             hue_order=[True, False],
#             color='g',  # box color
#             width=0.5,  # box width
#             linewidth=0.5,  # whisker width
#             whis=1,  # whisker length
#             fliersize=2,  # outlier diamonds
#             showcaps=False,  # caps on top of whiskers
#             data=cars)
# print(cars.mpg.describe())

# # lesson 6 violinplot
# sns.violinplot(y='displacement', x='cylinders', hue='origin',
#                split=True,
#                inner='quartiles',
#                scale='count',
#                scale_hue=False,
#                data=cars[cars.origin.isin(['japan', 'europe'])]),
#
# print(cars[cars.origin.isin(['japan', 'europe'])].
#       groupby('cylinders').origin.value_counts())

# lesson 7 swarmplot
usa = cars[cars.origin == 'usa']

# Define a custom color palette to match Set2 colors
custom_palette = sns.color_palette("Set2", n_colors=len(cars["cylinders"].unique()))

# Create a boxplot with the custom palette
# sns.boxplot(x='cylinders', y='horsepower', data=cars, palette=custom_palette)
sns.violinplot(x='cylinders', y='horsepower', data=cars,
               inner=None,  # turns off box plot
               scale='width',
               palette=custom_palette)

# # Create a swarmplot with the same custom palette
# sns.swarmplot(x='cylinders', y='horsepower', data=cars, palette=custom_palette)
#

# Create a swarmplot with black dots to see them better
sns.swarmplot(x='cylinders', y='horsepower',
              # color='black',
              linewidth=1,  # black line around each dot
              edgecolor='black',  # color of line around dot, default = gray
              marker='*',  # matplot marker styles
              alpha=.25,  # transparency
              data=cars)


plt.show()

