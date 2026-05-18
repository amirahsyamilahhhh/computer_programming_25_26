flower1 = {
    "id": "flower1",
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2,
    "species": "setosa"
}

# Task 1: Create a dictionary for second flower
flower2 = {
    "id": "flower2",
    "sepal_length": 4.9,
    "sepal_width": 3.0,
    "petal_length": 1.4,
    "petal_width": 0.2,
    "species": "setosa"
}

print(flower1["id"])

# Task 2: Create list of dictionaries
dataset = [flower1, flower2]

# Define classification variables
threshold = 2.0
positive_label = "setosa"
negative_label = "not_setosa"
total = 0
correct = 0
wrong = 0

# Task 3 and Task 4: Process and classify the dataset
y_pred_list = []

for sample in dataset:
    print(sample["id"], sample["petal_length"], sample["species"])

    total += 1

    if sample["petal_length"] < threshold:
        y_pred = positive_label
    else:
        y_pred = negative_label

    y_pred_list.append(y_pred)

    # Check correct or wrong
    if y_pred == sample["species"]:
        correct += 1
    else:
        wrong += 1

print("Correct:", correct)
print("Wrong:", wrong)
print("Total:", total)
print("Predictions:", y_pred_list)