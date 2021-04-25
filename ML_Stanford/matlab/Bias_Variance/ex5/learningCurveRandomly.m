function [error_train, error_val] = ...
    learningCurveRandomly(X, y, Xval, yval, lambda)
%%LEARNINGCURVERandomly Generates the train and cross validation set errors needed 
%to plot a learning curve
%   [error_train, error_val] = ...
%       LEARNINGCURVE(X, y, Xval, yval, lambda) returns the train and
%       cross validation set errors for a learning curve. In particular, 
%       it returns two vectors of the same length - error_train and 
%       error_val. Then, error_train(i) contains the training error for
%       i examples (and similarly for error_val(i)).
%
%for i examples, we pick i examples from the training set and compute the
%train error and cross validation error of i examples we make this process
%for i examples K times then we set the ith training error and corss
%validation error to the average.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
K = 50;
M = numel(y);
CV = numel(yval);

% the computed vectors
error_train = zeros(M, 1);
error_val   = zeros(M, 1);

for i = 1 : M
    %select i random elements from X to train the model compute the
    %training error and cv error. repeat this process K times with random
    %i examples then set train_error(i), cv_error(i) with the average value
    for j = 1:K
        r = randi([1 M], 1, i);
   
        %train the model on data from 1 to i
        theta = trainLinearReg(X(r, :), y(r), lambda);

        %compute training error
        error_train(i) = error_train(i) + 0.5/i * sum((X(r, :) * theta - y(r)) .^ 2);

        %compute cross validation error
        error_val(i) = error_val(i) + 0.5/CV * sum((Xval(r, :) * theta - yval(r)) .^ 2);

    end
    
    %average of train_error(i) and cross_validation_error(i)
    error_train(i) = error_train(i) ./ K;
    error_val(i)   = error_val(i)   ./ K;
end