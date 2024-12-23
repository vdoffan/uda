import numpy as np


# Функция активации (сигмоида) и её производная
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


# Входные данные для XOR
training_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Выходные данные для XOR
training_outputs = np.array([[0], [1], [1], [0]])

# Инициализация весов
# Добавляем bias, поэтому добавляем дополнительный нейрон
# Входной слой имеет 2 входа + 1 bias
input_layer_size = 2
hidden_layer_size = 2
output_layer_size = 1

# Весовые матрицы инициализируются случайными значениями
# Вес для скрытого слоя (включая bias)
hidden_weights = 2 * np.random.random((input_layer_size + 1, hidden_layer_size)) - 1
# Вес для выходного слоя (включая bias)
output_weights = 2 * np.random.random((hidden_layer_size + 1, output_layer_size)) - 1

# Параметры обучения
learning_rate = 0.1
epochs = 10001

for epoch in range(epochs):
    # Прямое распространение
    # Добавляем bias к входным данным
    input_with_bias = np.hstack(
        (training_inputs, np.ones((training_inputs.shape[0], 1)))
    )

    # Скрытый слой
    hidden_layer_input = np.dot(input_with_bias, hidden_weights)
    hidden_layer_output = sigmoid(hidden_layer_input)

    # Добавляем bias к скрытому слою
    hidden_with_bias = np.hstack(
        (hidden_layer_output, np.ones((hidden_layer_output.shape[0], 1)))
    )

    # Выходной слой
    output_layer_input = np.dot(hidden_with_bias, output_weights)
    predicted_output = sigmoid(output_layer_input)

    # Вычисление ошибки
    error = training_outputs - predicted_output
    if epoch % 1000 == 0:
        mse = np.mean(np.square(error))
        print(f"Эпоха {epoch}, Среднеквадратичная ошибка: {mse}")

    # Обратное распространение ошибки
    d_predicted_output = error * sigmoid_derivative(predicted_output)

    # Ошибка скрытого слоя
    error_hidden_layer = d_predicted_output.dot(
        output_weights[:-1].T
    )  # Исключаем bias весы
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    # Обновление весов
    output_weights += hidden_with_bias.T.dot(d_predicted_output) * learning_rate
    hidden_weights += input_with_bias.T.dot(d_hidden_layer) * learning_rate

# Тестирование сети
print("\nРезультаты после обучения:")
for x, y in zip(training_inputs, training_outputs):
    # Добавляем bias к входу
    x_with_bias = np.append(x, 1)
    hidden_input = np.dot(x_with_bias, hidden_weights)
    hidden_output = sigmoid(hidden_input)

    # Добавляем bias к скрытому слою
    hidden_with_bias = np.append(hidden_output, 1)
    output_input = np.dot(hidden_with_bias, output_weights)
    predicted = sigmoid(output_input)

    print(f"Вход: {x} -> Выход: {predicted[0]:.4f} (Ожидание: {y[0]})")

# Проверка точности
predictions = []
for x in training_inputs:
    x_with_bias = np.append(x, 1)
    hidden_output = sigmoid(np.dot(x_with_bias, hidden_weights))
    hidden_with_bias = np.append(hidden_output, 1)
    output = sigmoid(np.dot(hidden_with_bias, output_weights))
    predictions.append(round(output[0]))

correct = sum([1 for p, y in zip(predictions, training_outputs.flatten()) if p == y])
accuracy = correct / len(training_outputs) * 100
print(f"\nТочность: {accuracy}%")
