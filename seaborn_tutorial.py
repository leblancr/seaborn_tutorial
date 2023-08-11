import matplotlib
#print(matplotlib.__version__)
matplotlib.use('TkAgg')  # Set the desired backend before importing pyplot
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt
import seaborn as sns
#print(sns.__version__)

# x = [10, 20, 30, 40]
# y = [0, 15, 10, 25]
# sns.set_style("ticks")
# plt.plot(x, y)
# plt.show()

cars = sns.load_dataset('mpg')
print(type(cars))  # panda.core.frame.DataFrame
cars.dropna(inplace=True)
print(cars.shape)
print(cars.head())

sns.relplot(x='model_year', y='mpg', col='origin', hue='cylinders', data=cars)
plt.show()

