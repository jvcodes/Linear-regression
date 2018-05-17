# Standalone simple linear regression example
from math import sqrt

# Calculate root mean squared error
def rmse_metric(actual, predicted):
	sum_error = 0.0
	for i in range(len(actual)):
		prediction_error = predicted[i] - actual[i]
		sum_error += (prediction_error ** 2)
	mean_error = sum_error / float(len(actual))
	return sqrt(mean_error)

# Evaluate regression algorithm on training dataset
def evaluate_algorithm(dataset):
	test_set = list()
	for row in dataset:
		row_copy = list(row)
        #print(type(row_copy))
		row_copy[-1] = None
		test_set.append(row_copy)

    #print(test_set)
	predicted = simple_linear_regression(dataset, test_set)
	print(predicted)
	actual = [row[-1] for row in dataset]
	rmse = rmse_metric(actual, predicted)
	return rmse

# Calculate the mean value of a list of numbers
def mean(values):
	return sum(values) / float(len(values))

# Calculate covariance between x and y
def covariance(x, mean_x, y, mean_y):
	covar = 0.0
	for i in range(len(x)):
		covar += (x[i] - mean_x) * (y[i] - mean_y)
	return covar

# Calculate the variance of a list of numbers
def variance(values, mean):
	return sum([(x-mean)**2 for x in values])

# Calculate coefficients
def coefficients(dataset):
	x = [row[0] for row in dataset]
	y = [row[1] for row in dataset]
	x_mean, y_mean = mean(x), mean(y)
	b1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
	b0 = y_mean - b1 * x_mean
	return [b0, b1]

# Simple linear regression algorithm
def simple_linear_regression(train, test):
	predictions = list()
    #a=0
	b0, b1 = coefficients(train)
	for row in test:
		yhat = b0 + b1 * row[0]
        #a=2+1
		predictions.append(yhat)
    #print(list(predictions))
	return predictions

# Test simple linear regression
'''
dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
r_error = evaluate_algorithm(dataset, simple_linear_regression)
print('RMSE: %.3f' % (r_error))'''
