def my_model(x):
  m = 0.031
  b = 1.42
  return m*x+b

shoe_size = 13
print("A person with shoe size %i is probably around %f metres tall"%(shoe_size, my_model(shoe_size)))

print("Also, let's make some arbitrary changes now on the server side.")

print("Let's make some more arbitrary changes in order to create a merging situation")
