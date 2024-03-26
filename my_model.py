def my_model(x):
  m = 0.03
  b = 1.4
  return m*x+b

shoe_size = 13
print("A person with shoe size %i is probably around %f metres tall"%(shoe_size, my_model(shoe_size)))
