function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost and gradient of regularized linear 
%               regression for a particular choice of theta.
%
%               You should set J to the cost and grad to the gradient.
%

%perdicted values
h = X * theta;
ERROR = h-y;

%square error
SE = sum((ERROR) .^ 2);

% the regularization term to penalize high degree terms
regularization_term = lambda * sum(theta(2:end, 1) .^ 2);

% regularized cost function
J = 0.5/m * (SE + regularization_term);

% compute the gradients with the regularization term

for i = 1 : length(grad)
    grad(i) = 1/m * sum(ERROR .* X(:, i));
    
    %add regularization term. excluding theta0
    if i == 1
        continue
    end
    grad(i) = grad(i) + ( (lambda / m) * theta(i) ); 
end

% =========================================================================

grad = grad(:);

end
