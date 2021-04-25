function [J] = costFunction(X, y, theta)
%compute the cost function of predicted values and actual value
% using mean square error method
m = numel(y);
J = 0.5/m * sum((X *theta - y) .^ 2);
end