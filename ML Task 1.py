

!wget https://raw.githubusercontent.com/alexjolly28/entri_DSML/main/resources/insurance.csv

"""##STEP-1: Importing Libraries & Data Set"""

#import basic libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets

#Read the Data
df=pd.read_csv("/content/insurance.csv")
df

"""##STEP-2:Exploratory Data Analysis (EDA)"""

# Descriptive stats
df.describe()

# Null check
df.isnull()

"""Visulizations"""

# Age vs Charges
# the more the age the more will be insurance charge
plt.scatter(df.age,df.charges)
plt.xlabel("Age")
plt.ylabel("Charges")
plt.title("Age v/s Charges")
plt.show()

# sex vs charges
# males insurance charges more than females.
plt.scatter(df.sex,df.charges)
plt.xlabel("Sex")
plt.ylabel("Charges")
plt.title("Sex v/s Charges")
plt.show()

# smoker vs charges
# smokers have more insurance charges than the non smokers
plt.scatter(df.smoker,df.charges)
plt.xlabel("Smoker")
plt.ylabel("Charges")
plt.title("Smoker v/s Charges")
plt.show()

# region vs charges
# region actually does not play any role in determining the insurance charges
plt.scatter(df.region,df.charges)
plt.xlabel("Region")
plt.ylabel("Charges")
plt.title("Region v/s Charges")
plt.show()

# plotting the correlation plot for the dataset
sns.pairplot(df)

"""##STEP-3:Data Preprocessing / Clean the Data

"""

# removing unnecassary columns from the dataset

# Label Encoding for sex and smoker
from sklearn.preprocessing import LabelEncoder
import pandas as pd
df=pd.read_csv("/content/insurance.csv")
print("Unique values in sex column before encoding:",df['sex'].unique())
print("Unique values in smoker column before encoding:",df['smoker'].unique())
label_encoder=LabelEncoder()
df["sex1"]=label_encoder.fit_transform(df["sex"])
df["smoker1"]=label_encoder.fit_transform(df["smoker"])
print("Unique values in sex_encoded column after encoding:",df['sex1'].unique())
print("Unique values in smoker_encoded column after encoding:",df['smoker1'].unique())
print(df.head())

#Selecting Independent (Features) & Dependent(Target) variables
import pandas as pd
df=pd.read_csv("/content/insurance.csv")
print('Columns in the dataset:')
print(df.columns)
features=df[['age','sex','bmi','children','smoker','region']]
target=df['charges']
print(features.head())
print(target.head())

"""Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
import pandas as pd
df=pd.read_csv("/content/insurance.csv")
features=df[['age','sex','bmi','children','smoker','region']]
target=df['charges']
X_train, X_test, y_train, y_test=train_test_split(features,target,test_size=0.2,random_state=42)
print("Shape of X_train:",X_train.shape)
print("Shape of X_test:",X_test.shape)
print("Shape of y_train:",y_train.shape)
print("Shape of y_test:",y_test.shape)

"""##STEP-4 : Fit the Model & Predict , check the Accuracy

##Linear Regression
"""

# creating the model
# feeding the training data to the model
# predicting the test set results
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
import numpy as np
import pandas as pd
df=pd.read_csv('/content/insurance.csv')
features=df[['age','sex','bmi','children','smoker','region']]
target=df['charges']
features=pd.get_dummies(features,drop_first=True)
X_train, X_test, y_train, y_test=train_test_split(features,target,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
# calculating the mean squared error
mse=mean_squared_error(y_test,y_pred)
# Calculating the root mean squared error
rmse=np.sqrt(mse)
# Calculating the r2 score
r2=r2_score(y_test,y_pred)
print("Mean squared error :",mse)
print("Root mean squared error:",rmse)
print("r2 score:",r2)

"""##Support Vector Machine"""

# creating the model
# feeding the training data to the model
# predicting the test set results
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error,r2_score
import numpy as np
import pandas as pd
df=pd.read_csv('/content/insurance.csv')
features=df[['age','sex','bmi','children','smoker','region']]
target=df['charges']
features=pd.get_dummies(features,drop_first=True)
X_train, X_test, y_train, y_test=train_test_split(features,target,test_size=0.2,random_state=42)
model=SVR(kernel='linear')
model.fit(X_train, y_train)
y_pred=model.predict(X_test)
# calculating the mean squared error
mse=mean_squared_error(y_test,y_pred)
# Calculating the root mean squared
rmse=np.sqrt(mse)
# Calculating the r2 score
r2=r2_score(y_test,y_pred)
print("Mean squared error :",mse)
print("Root mean squared error:",rmse)
print("r2 score:",r2)

"""##Decision Tree"""

# creating the model
# feeding the training data to the model
# predicting the test set results
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error,r2_score
import numpy as np
import pandas as pd
df=pd.read_csv('/content/insurance.csv')
features=df[['age','sex','bmi','children','smoker','region']]
target=df['charges']
features=pd.get_dummies(features,drop_first=True)
X_train, X_test, y_train, y_test=train_test_split(features,target,test_size=0.2,random_state=42)
model=DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)
y_pred=model.predict(X_test)
# calculating the mean squared error
mse=mean_squared_error(y_test,y_pred)
# Calculating the root mean squared error
rmse=np.sqrt(mse)
# Calculating the r2 score
r2=r2_score(y_test,y_pred)
print("Mean squared error :",mse)
print("Root mean squared error:",rmse)
print("r2 score:",r2)

"""##Random Forest"""

# creating the model
# feeding the training data to the model
# predicting the test set results
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error,r2_score
import numpy as np
import pandas as pd
df=pd.read_csv('/content/insurance.csv')
features=df[['age','sex','bmi','children','smoker','region']]
target=df['charges']
features=pd.get_dummies(features,drop_first=True)
X_train, X_test, y_train, y_test=train_test_split(features,target,test_size=0.2,random_state=42)
model=RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)
y_pred=model.predict(X_test)
# calculating the mean squared error
mse=mean_squared_error(y_test,y_pred)
# Calculating the root mean squared error
rmse=np.sqrt(mse)
# Calculating the r2 score
r2=r2_score(y_test,y_pred)
print("Mean squared error :",mse)
print("Root mean squared error:",rmse)
print("r2 score:",r2)

"""Compare and evaluate the Model results and find the best model"""

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
df=pd.read_csv('/content/insurance.csv')
features=df[['age','sex','bmi','children','smoker','region']]
target=df['charges']
features=pd.get_dummies(features,drop_first=True)
X_train, X_test, y_train, y_test=train_test_split(features,target,test_size=0.2,random_state=42)
models=[("Linear Regression",LinearRegression()),("Decision Tree",DecisionTreeRegressor(random_state=42)),
       ("Support Vector Machine",SVR(kernel='linear')),("Random Forest",RandomForestRegressor(random_state=42))]
results = []
for name, model in models:
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    results.append([name, mse, rmse, r2])
results_df = pd.DataFrame(results, columns=['Model', 'MSE', 'RMSE', 'R-squared'])
print("Model Comparison:")
print(results_df)
best_mse = results_df['MSE'].idxmin()
best_rmse = results_df['RMSE'].idxmin()
best_r2 = results_df['R-squared'].idxmax()
best_model = results_df.loc[[best_mse, best_rmse, best_r2]].iloc[0]
print("\nBest performing models based on metrics:")
print(best_model)



