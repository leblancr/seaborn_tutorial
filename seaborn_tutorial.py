import matplotlib
#print(matplotlib.__version__)
matplotlib.use('TkAgg')  # Set the desired backend before importing pyplot
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt
import seaborn as sns
#print(sns.__version__)

cars = sns.load_dataset('mpg').dropna()
print(cars.shape)
print(cars.head())

# `shade_lowest` has been replaced by `thresh`
sns.kdeplot(x='horsepower', y='mpg', data=cars,
            fill=True,
            thresh=0.05,
            cbar=True)
# sns.kdeplot(cars.horsepower, fill=True, bw_method=.1, cumulative=True)
plt.show()

