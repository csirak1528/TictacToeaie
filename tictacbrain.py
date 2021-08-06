import random
import load_data_
import math
data = load_data_.data


w1=random.random()
w1_1=random.random()
w1_2=random.random()
w1_3=random.random()



w2=random.random()
w2_1=random.random()
w2_2=random.random()


w3=random.random()
w3_1=random.random()

w4=random.random()

b=random.random()
b1=random.random()
b2=random.random()
b3=random.random()
b4=random.random()

def sigmoid(x):
  return 8/(1+math.exp(-x))

def sigmoidp(x):
  return sigmoid(x) * (8-sigmoid(x))

learning_rate = .001
for i in range(250000):

  ri = random.randint(0,len(data)-1)
  point  = data[ri]
  target = point[len(point)-1]


  if len(point) == 1:
      z = b
      pred = sigmoid(z)
      cost = (pred - target)**2

      dcost_pred = 2*( pred - target)
      dpred_dz = sigmoidp(z)

      dz_b = 1


      dcost_dz = dcost_pred*dpred_dz
      dcost_db = dcost_dz * dz_b
      b = b - learning_rate*dcost_db


  if len(point) == 2:
      z = w1*point[0] + b1

      dz_w1 = point[0]
      pred = sigmoid(z)
      cost = (pred - target)**2

      dcost_pred = 2*( pred - target)
      dpred_dz = sigmoidp(z)

      dz_b = 1


      dcost_dz = dcost_pred*dpred_dz
      dcost_db = dcost_dz * dz_b
      b1 = b1 - learning_rate*dcost_db

      dcost_w1 = dcost_dz * dz_w1

      w1 = w1- learning_rate * dcost_w1
  if len(point) == 3:
      z = w1_1*point[0] + w2*point[1] + b2

      dz_w1 = point[0]
      dz_w2 = point[1]

      pred = sigmoid(z)
      cost = (pred - target)**2

      dcost_pred = 2*( pred - target)
      dpred_dz = sigmoidp(z)

      dz_b = 1


      dcost_dz = dcost_pred*dpred_dz
      dcost_db = dcost_dz * dz_b
      b2 = b2 - learning_rate*dcost_db

      dcost_w1 = dcost_dz * dz_w1
      dcost_w2 = dcost_dz * dz_w2

      w1_1 = w1_1- learning_rate * dcost_w1
      w2 = w2- learning_rate * dcost_w2

  if len(point) == 4:
      z = w1_2*point[0] + w2_1*point[1] + w3*point[2] + b3

      dz_w1 = point[0]
      dz_w2 = point[1]
      dz_w3 = point[2]

      pred = sigmoid(z)
      cost = (pred - target)**2

      dcost_pred = 2*( pred - target)
      dpred_dz = sigmoidp(z)

      dz_b = 1


      dcost_dz = dcost_pred*dpred_dz
      dcost_db = dcost_dz * dz_b
      b3 = b3 - learning_rate*dcost_db

      dcost_w1 = dcost_dz * dz_w1
      dcost_w2 = dcost_dz * dz_w2
      dcost_w3 = dcost_dz * dz_w3

      w1_2 = w1_2 - learning_rate * dcost_w1
      w2_1 = w2_1- learning_rate * dcost_w2
      w3 = w3- learning_rate * dcost_w3

  if len(point) == 5:
      z = w1_3*point[0] + w2_2*point[1] + w3_1*point[2] + w4*point[3] + b4

      dz_w1 = point[0]
      dz_w2 = point[1]
      dz_w3 = point[2]
      dz_w4 = point[3]


      pred = sigmoid(z)
      cost = (pred - target)**2

      dcost_pred = 2*( pred - target)
      dpred_dz = sigmoidp(z)

      dz_b = 1


      dcost_dz = dcost_pred*dpred_dz
      dcost_db = dcost_dz * dz_b
      b4 = b4 - learning_rate*dcost_db

      dcost_w1 = dcost_dz * dz_w1
      dcost_w2 = dcost_dz * dz_w2
      dcost_w3 = dcost_dz * dz_w3
      dcost_w4 = dcost_dz * dz_w4

      w1_3 = w1_3 - learning_rate * dcost_w1
      w2_2 = w2_2 - learning_rate * dcost_w2
      w3_1 = w3_1 - learning_rate * dcost_w3
      w4 = w4- learning_rate * dcost_w4




def first(x):
  return round(sigmoid(b))
def second(x):
  return round(sigmoid(w1*x[0] + b1))
def third(x):
  return round(sigmoid(w1_1*x[0]+w2*x[1] + b2))
def fourth(x):
  return round(sigmoid(w1_2*x[0] + w2_1*x[1] + w3*x[2] + b3))
def fifth(x):
  return round(sigmoid(w1_3*x[0] + w2_2*x[1] + w3_1*x[2] + w4*x[3] + b4))
