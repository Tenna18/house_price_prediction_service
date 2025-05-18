# imports 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# read data
df = pd.read_csv('../data/real_estate.csv')

# set variables
X = df.drop(columns=["No", "Y house price of unit area"])
y = df["Y house price of unit area"]

# train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train with regression
model = LinearRegression()
model.fit(X_train, y_train)

# save to disk
pickle.dump(model, open("house_price_model.pkl", "wb"))