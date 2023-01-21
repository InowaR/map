import numpy as np

def train(X, Y):
  w1 = np.random.random((9,5))
  w2 = np.random.random((5,2))
  for i in range(60000):
    S1 = 1 / (1 + np.exp(-(np.dot(X, w1))))
    S2 = 1 / (1 + np.exp(-(np.dot(S1, w2))))
    S2_delta = (Y - S2) * (S2 * (1 - S2))
    S1_delta = S2_delta.dot(w2.T) * (S1 * (1 - S1))
    w1 += X.T.dot(S1_delta)
    w2 += S1.T.dot(S2_delta)
  return w1, w2

def predict(test, w1, w2):
  S1 = 1 / (1 + np.exp(-(np.dot(test, w1))))
  S2 = 1 / (1 + np.exp(-(np.dot(S1, w2))))
  return S2

def main():
  a = train(X, Y)
  w1, w2 = a
  b = predict(test, w1, w2)
  print(b)

if __name__ == "__main__":
  X = np.array([[1,0,1,1,0,1,1,0,1], [0,0,1,0,1,1,1,1,1], [1,0,0,1,0,0,1,1,1], [1,0,0,1,1,0,1,1,1], [0,0,1,0,0,1,1,1,1], [0,0,1,1,1,1,1,1,1], [1,0,0,1,1,1,1,1,1]])
  Y = np.array([[1, 1], [0.5, 1], [1, 0.5], [1, 0.5], [0.5, 1], [0, 1], [1, 0]])
  test = np.array([[0,0,1,1,1,1,1,1,1]])
  main()
