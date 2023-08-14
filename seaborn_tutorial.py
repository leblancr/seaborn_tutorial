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
#             thresh=0.05,
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
cars['newer_model'] = cars.model_year > 76
sns.boxplot(x='horsepower', y='origin', hue='newer_model',
            hue_order=[True, False],
            color='g',  # box color
            width=0.5,  # box width
            linewidth=0.5,  # whisker width
            whis=1,  # whisker length
            fliersize=2,  # outlier diamonds
            showcaps=False,  # caps on top of whiskers
            data=cars)
print(cars.mpg.describe())
plt.show()

