from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


#Uniform Distribution
x = random.uniform(low=2, high=10, size=(100, 2))     #low (lower bound) default 0.0, high (upper bound) default 1.0
print(x)
sns.displot(x, kind='kde')
plt.show()


#Logistic Distribution
x = random.logistic(loc=1, scale=2, size=(50))    #loc (mean) default 0, scale (standard deviation) default 1
print(x)
sns.displot(x, kind="kde")
plt.show()

data = {
  "normal": random.normal(scale=2, size=1000),
  "logistic": random.logistic(size=1000)
}
sns.displot(data, kind="kde")
plt.show()


#Multinomial Distribution  (like binomial but binomial has success and fail only, this can have multiple result (like dice) and use diff color to represent)
x = random.multinomial(n=12, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], size=(6000))
print(x)
sns.displot(x, kind="kde")
plt.show()


#Exponential Distribution (https://youtu.be/WKFk0NXyO50?si=zFCp_gD9IKxTSiyn&t=136)
sns.displot(random.exponential(scale=2, size=1000), kind="kde")      #scale (lambda, interval between two events) default 1.0
plt.show()


#Chi Square Distribution (x square, x: randomly selecting a single value from a standard normal distribution (follow probability of normal distribution))
x = random.chisquare(df=2, size=(100, 3))      #df (degree of freedom): if 3 means sum of square of three randomly selected value from three standard normal distribution
sns.displot(x, kind="kde")
plt.show()

data = {
  "df1": random.chisquare(df=1, size=(1000)),
  "df2": random.chisquare(df=2, size=(1000)),
  "df3": random.chisquare(df=3, size=(1000))
}
sns.displot(data, kind="kde")
plt.show()


#Rayleigh Distribution
x = random.rayleigh(scale=2, size=(100, 2))       #scale (standard deviation) default 1.0
print(x)
sns.displot(x, kind="kde")
plt.show()


#Pareto Distribution
sns.displot(random.pareto(a=3, size=1000))     #a change the percentage (1.16 for 20% factors cause 80% outcome)
plt.show()

#Zipf Distribution    (pareto continuous, zipf discrete)
'''
Zipf's Law: In a collection, the nth common term is 1/n times of the most common term.
E.g. the 5th most common word in English occurs nearly 1/5 times as often as the most common word.
linear line when log
nth term is 1/(n power a) times of the most common term
'''
x = random.zipf(a=1.01, size=1000)       #a (distribution parameter) (a must be greater than 1)
sns.displot(x[x<10])
plt.show()

'''
x[x<10]
Step 1:The Condition (x < 10)
When you type x < 10, NumPy looks at every single one of your 1,000 generated numbers and asks, "Is this less than 10?"
It creates a hidden list of True and False answers. (e.g., [True, True, False, True...])

Step 2: The Filter (x[...])
When you wrap that condition in brackets next to your original array x, NumPy applies that True/False list like a mask.
It throws away all the numbers that got a "False" (anything 10 or higher) and only plots the numbers that got a "True".
'''









