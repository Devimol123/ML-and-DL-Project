# -*- coding: utf-8 -*-
"""ML Task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P_SkfeE3PASCN3n5Jl3TJ4ntRJhwlISy
"""

!wget -O drug200.csv https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/drug200.csv

#import basic libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets

data=pd.read_csv("/content/drug200.csv")
data

#Encoding categorical variables
from sklearn.preprocessing import LabelEncoder
import pandas as pd
data=pd.read_csv("/content/drug200.csv")
data.fillna(data.mean(),inplace=True)
label_encoder=LabelEncoder()
data['Sex']=label_encoder.fit_transform(data['Sex'])
print(data.head())

import pandas as pd
from sklearn.model_selection import train_test_split
data=pd.read_csv("/content/drug200.csv")
#Split the data into features (X) and target variable (y)
X=data[['Age','Sex','BP','Cholesterol']]
y=data['Drug']
#split into training and testing test
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print("X_train shape:",X_train.shape)
print("X_test shape:",X_test.shape)
print("y_train shape:",y_train.shape)
print("y_test shape:",y_test.shape)

#Logistic Regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score,classification_report
import numpy as np
import pandas as pd
df=pd.read_csv('/content/drug200.csv')
features=df[['Age','Sex','BP','Cholesterol']]
target=df['Drug']
features=pd.get_dummies(features,drop_first=True)
X_train, X_test, y_train, y_test=train_test_split(features,target,test_size=0.2,random_state=42)
model=LogisticRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
report=classification_report(y_test,y_pred)
print("Logistic Regression Model Evaluation:")
print(f"Accuracy: {accuracy:.4f}")
print("Classification Report:")
print(report)

#Decision Tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score,classification_report
import numpy as np
import pandas as pd
df=pd.read_csv('/content/drug200.csv')
features=df[['Age','Sex','BP','Cholesterol']]
target=df['Drug']
features=pd.get_dummies(features,drop_first=True)
X_train, X_test, y_train, y_test=train_test_split(features,target,test_size=0.2,random_state=42)
model=DecisionTreeClassifier()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
report=classification_report(y_test,y_pred)
print("Decision Tree Model Evaluation:")
print(f"Accuracy: {accuracy:.4f}")
print("Classification Report:")
print(report)

#Random Forest
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score,classification_report
import numpy as np
import pandas as pd
df=pd.read_csv('/content/drug200.csv')
features=df[['Age','Sex','BP','Cholesterol']]
target=df['Drug']
features=pd.get_dummies(features,drop_first=True)
X_train, X_test, y_train, y_test=train_test_split(features,target,test_size=0.2,random_state=42)
model=RandomForestClassifier()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
report=classification_report(y_test,y_pred)
print("Random Forest Model Evaluation:")
print(f"Accuracy: {accuracy:.4f}")
print("Classification Report:")
print(report)

#K-Nearest Neighbors (KNN)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score,classification_report
import numpy as np
import pandas as pd
df=pd.read_csv('/content/drug200.csv')
features=df[['Age','Sex','BP','Cholesterol']]
target=df['Drug']
features=pd.get_dummies(features,drop_first=True)
X_train, X_test, y_train, y_test=train_test_split(features,target,test_size=0.2,random_state=42)
model=KNeighborsClassifier()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
report=classification_report(y_test,y_pred)
print("K-Nearest Neighbors Model Evaluation:")
print(f"Accuracy: {accuracy:.4f}")
print("Classification Report:")
print(report)

#Support Vector Machine
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score,classification_report
import numpy as np
import pandas as pd
df=pd.read_csv('/content/drug200.csv')
features=df[['Age','Sex','BP','Cholesterol']]
target=df['Drug']
features=pd.get_dummies(features,drop_first=True)
X_train, X_test, y_train, y_test=train_test_split(features,target,test_size=0.2,random_state=42)
model=SVC()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
report=classification_report(y_test,y_pred)
print("Support Vector Machine Model Evaluation:")
print(f"Accuracy: {accuracy:.4f}")
print("Classification Report:")
print(report)

#Naive Bayes Classifier
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score,classification_report
import numpy as np
import pandas as pd
df=pd.read_csv('/content/drug200.csv')
features=df[['Age','Sex','BP','Cholesterol']]
target=df['Drug']
features=pd.get_dummies(features,drop_first=True)
X_train, X_test, y_train, y_test=train_test_split(features,target,test_size=0.2,random_state=42)
model=GaussianNB()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
report=classification_report(y_test,y_pred)
print("Naive Bayes Classifier Model Evaluation:")
print(f"Accuracy: {accuracy:.4f}")
print("Classification Report:")
print(report)