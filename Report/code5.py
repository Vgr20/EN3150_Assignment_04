from sklearn.svm import SVC
from mpl_toolkits.mplot3d import Axes3D

# Create a linear SVM
svm_classifier = SVC(kernel='linear')

# Use the mapped 3-dimensional data
mapped_data = np.column_stack((mappedx_1, mappedy_1, mappedz_1))

# Split the test and training data sets.

X_train, X_test, y_train, y_test = train_test_split(mapped_data, y, test_size=0.2)

# Fit the SVM model
svm_classifier.fit(X_train,y_train)

# Make predictions using the model

y_pred = svm_classifier.predict(X_test)

# Visualize the decision boundary
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the points
ax.scatter(mappedx_1[y == 0], mappedy_1[y == 0], mappedz_1[y == 0], color='r', marker='o', label='Class 0')
ax.scatter(mappedx_1[y == 1], mappedy_1[y == 1], mappedz_1[y == 1], color='b', marker='^', label='Class 1')

# Plot the decision boundary
xx, yy = np.meshgrid(np.linspace(mappedx_1.min(), mappedx_1.max(), 50),
                     np.linspace(mappedy_1.min(), mappedy_1.max(), 50))
zz = (-svm_classifier.intercept_[0] - svm_classifier.coef_[0][0] * xx - svm_classifier.coef_[0][1] * yy) / svm_classifier.coef_[0][2]
ax.plot_surface(xx, yy, zz, alpha=0.3, color='gray')

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Show the plot
plt.show()


# Evaluate the performance of the model using metrics such as accuracy, precision, recall, and F1 score
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 score:", f1_score(y_test, y_pred))

