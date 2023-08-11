import matplotlib
#print(matplotlib.__version__)
matplotlib.use('TkAgg')  # Set the desired backend before importing pyplot
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt
import seaborn as sns
#print(sns.__version__)

# cars = sns.load_dataset('mpg').dropna()
# print(cars.shape)
# print(cars.head())
#
# # `shade_lowest` has been replaced by `thresh`
# sns.kdeplot(x='horsepower', y='mpg', data=cars,
#             fill=True,
#             thresh=0.05,
#             cbar=True)
# sns.kdeplot(cars.horsepower, fill=True, bw_method=.1, cumulative=True)

penguins = sns.load_dataset('penguins').dropna()
print(penguins.shape)
print(penguins.head())
sns.set_style('darkgrid')
# sns.histplot(penguins.bill_length_mm)
sns.histplot(x='bill_length_mm', data=penguins,
             kde=True, bins=10, hue='species', element='poly')
plt.show()

