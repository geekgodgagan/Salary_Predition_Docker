import joblib
def prediction():
    model = joblib.load("salary.pk1")
    exp = int(input())
    predict = model.predict([[exp]])
    print("Salary is "+ str(predict))
prediction()
