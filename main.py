import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data: hours studied vs exam scores
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9]])
y = np.array([35, 50, 55, 65, 70, 75, 80, 85, 95])


# Predict score for 7.5 hours studied
predicted_score = model.predict(np.array([[7.5]]))
print(f"Predicted exam score for 7.5 study hours: {predicted_score[0]:.2f}")


# Plot data + regression line
plt.scatter(X, y, color="blue", label="Data")
plt.plot(X, model.predict(X), color="red", label="Regression Line")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.legend()
plt.show()
