import pickle

model = pickle.load(open('model/house_model.pkl', 'rb'))

area = int(input("Enter house area: "))
price = model.predict([[area]])

print("Predicted Price:", price[0])
