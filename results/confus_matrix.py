# import json
# import numpy as np
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# from sklearn.metrics import confusion_matrix

# # Path to the JSON file with prediction results
# results_file = "DIETClassifier_errors.json"

# # Load prediction results from JSON file
# with open(results_file, "r") as file:
#     results = json.load(file)

# # Extract true labels and predicted labels from results, handling unknown labels
# true_labels = []
# predicted_labels = []
# for example in results:
#     true_entities = [entity["entity"] for entity in example["entities"]]
#     predicted_entities = [entity["entity"] for entity in example["predicted_entities"]]
#     true_labels.extend(true_entities)
#     predicted_labels.extend(predicted_entities)

# # # Create confusion matrix
# # cm = confusion_matrix(true_labels, predicted_labels)

# # # Convert confusion matrix to pandas DataFrame for easier visualization
# # labels = np.unique(true_labels + predicted_labels)  # Combine true and predicted labels
# # df_cm = pd.DataFrame(cm, index=labels, columns=labels)

# # Add missing labels with value 'None'
# all_labels = np.unique(true_labels + predicted_labels)
# missing_labels = set(all_labels) - set(true_labels + predicted_labels)

# true_labels += list(missing_labels)
# predicted_labels += list(missing_labels)

# # Create confusion matrix
# cm = confusion_matrix(true_labels, predicted_labels, labels=all_labels)

# # Convert confusion matrix to pandas DataFrame for easier visualization
# df_cm = pd.DataFrame(cm, index=all_labels, columns=all_labels)


# # Plot confusion matrix
# plt.figure(figsize=(10, 7))
# sns.heatmap(df_cm, annot=True, fmt="d", cmap="Blues")
# plt.title("Confusion Matrix")
# plt.xlabel("Predicted")
# plt.ylabel("True")
# plt.savefig("confusion_matrix_entities.png")


import json
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# Path to the JSON file with prediction results
results_file = "DIETClassifier_errors.json"

# Load prediction results from JSON file
with open(results_file, "r") as file:
    results = json.load(file)

# Extract true labels and predicted labels from results, handling unknown labels
true_labels = []
predicted_labels = []
for example in results:
    true_entities = [entity["entity"] for entity in example["entities"]]
    predicted_entities = [entity["entity"] for entity in example["predicted_entities"]]
    true_labels.extend(true_entities)
    predicted_labels.extend(predicted_entities)

# Add missing labels with value 'None'
all_labels = np.unique(true_labels + predicted_labels)
missing_labels = set(all_labels) - set(true_labels + predicted_labels)

true_labels += list(missing_labels)
predicted_labels += list(missing_labels)

# Create confusion matrix
cm = confusion_matrix(true_labels, predicted_labels, labels=all_labels)

# Convert confusion matrix to pandas DataFrame for easier visualization
df_cm = pd.DataFrame(cm, index=all_labels, columns=all_labels)

# Plot confusion matrix
plt.figure(figsize=(10, 7))
sns.heatmap(df_cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.savefig("confusion_matrix_entities.png")
