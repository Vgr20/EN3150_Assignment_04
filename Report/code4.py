from sklearn.model_selection import train_test_split
import sklearn.svm as svm
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create an instance of the LinearSVC class and fit it to the training data
svm_classifier = svm.SVC(kernel='linear')
svm_classifier.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = svm_classifier.predict(X_test)

# Evaluate the performance of the model using metrics such as accuracy, precision, recall, and F1 score
print("Accuracy:", accuracy_score(y_test, y_pred))
print("F1 score:", f1_score(y_test, y_pred))

plt.scatter (X [:, 0], X [:, 1], c=y, cmap=plt.cm.Paired)


xx = np.linspace(X.min(), X.max(), 50)
yy = (svm_classifier.intercept_ - svm_classifier.coef_[0][0] * xx)
plt.plot(xx, yy, alpha=0.3, color='Black')
