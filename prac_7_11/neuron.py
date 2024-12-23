from numpy import exp, array, random, dot

training_set_inputs = array([[0, 0], [0, 1], [1, 0], [1, 1]])

training_set_outputs = array([[0, 1, 1, 0]]).T
weights = [[0.5], [0.5]]
# Можно задать случайные веса   2* random.random((3, 1)) - 1
for iteration in range(100000):
    output = 1 / (1 + exp(-(dot(training_set_inputs, weights))))
    weights += dot(
        training_set_inputs.T, (training_set_outputs - output) * output * (1 - output)
    )
    if iteration % 25000 == 0:
        print(weights)

print("результат на обучающем наборе")
print(output)

data_to_analise = [[0, 0], [0, 1], [1, 0], [1, 1]]
for data in data_to_analise:
    print("предсказание для  ", data)
    print(1 / (1 + exp(-(dot(array(data), weights)))))
