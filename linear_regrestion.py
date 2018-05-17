from math import sqrt
global B0,B1
def rmse_metric(actual, predicted):
	sum_error = 0.0
	for i in range(len(actual)):
		prediction_error = predicted[i] - actual[i]
		sum_error += (prediction_error ** 2)
	mean_error = sum_error / float(len(actual))
	return sqrt(mean_error)


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

def evaluate_slope_constant(dataset):
    test_set=[]
    predicted=0
    for row1 in dataset:
        row_cp=list(row1)
        print(row_cp)
        row_cp[-1]=None
        test_set.append(row_cp)
    prvalu,b0,b1=simple_lin_reg(dataset, test_set)
    print(prvalu)
    actual=[row[-1] for row in dataset]
    rmse=rmse_metric(actual, prvalu)
    return [rmse,b0,b1]

def simple_lin_reg(train,test):
    predictions=list()
    b0,b1=coefficients(train)
    B0,B1=b0,b1
    print(str(b0)+" b0 and b1    "+str(b1))
    for row in test:
        yhat=b0+b1*row[0]
        predictions.append(yhat)
    return [predictions,b0,b1]
