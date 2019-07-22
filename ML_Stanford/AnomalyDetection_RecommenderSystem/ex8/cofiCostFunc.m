function [J, grad] = cofiCostFunc(params, Y, R, num_users, num_movies, ...
                                  num_features, lambda)
%COFICOSTFUNC Collaborative filtering cost function
%   [J, grad] = COFICOSTFUNC(params, Y, R, num_users, num_movies, ...
%   num_features, lambda) returns the cost and gradient for the
%   collaborative filtering problem.
%

% Unfold the U and W matrices from params
X = reshape(params(1:num_movies*num_features), num_movies, num_features);
Theta = reshape(params(num_movies*num_features+1:end), ...
                num_users, num_features);

R = logical(R);

% You need to return the following values correctly
J = 0;
X_grad = zeros(size(X));
Theta_grad = zeros(size(Theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost function and gradient for collaborative
%               filtering. Concretely, you should first implement the cost
%               function (without regularization) and make sure it is
%               matches our costs. After that, you should implement the 
%               gradient and use the checkCostFunction routine to check
%               that the gradient is correct. Finally, you should implement
%               regularization.
%
% Notes: X - num_movies  x num_features matrix of movie features
%        Theta - num_users  x num_features matrix of user features
%        Y - num_movies x num_users matrix of user ratings of movies
%        R - num_movies x num_users matrix, where R(i, j) = 1 if the 
%            i-th movie was rated by the j-th user
%
% You should set the following variables correctly:
%
%        X_grad - num_movies x num_features matrix, containing the 
%                 partial derivatives w.r.t. to each element of X
%        Theta_grad - num_users x num_features matrix, containing the 
%                     partial derivatives w.r.t. to each element of Theta
%

% we can compute the gradients of x during computing J as a cost function
for movie = 1:num_movies
    % parameters of users rate this movie
    rateUsrs = Theta(R(movie, :), :);
    
    % features of this movie
    movieFeatures = X(movie, :);
    
    % actual rate of users to this movie
    movieActualRate = Y(movie, R(movie, :));
    
    % error between predicted rate and the actual rate
    err = (movieFeatures * rateUsrs' - movieActualRate);
    
    % add to cost function error of current movie rates
    J = J + sum(err .^  2);
    
    % gradient of movie features
    X_grad(movie, :) = err * rateUsrs + lambda * movieFeatures;
end

%divide J by 2
J = J / 2; 

% compute user parameters gradients
for user = 1 : num_users
    %features of movies rated by this user
    ratedMoviesFeatures = X(R(:, user), :);
    
    % user parameters
    userParams = Theta(user, :);
    
    %predicted rates given those movies by the current user
    predictedRates = ratedMoviesFeatures * userParams';
    
    % actual rate of users to this movie
    movieActualRate = Y(R(:, user), user);
    
    % error between predicted rate and the actual rate
    err = (predictedRates - movieActualRate);
    
    % gradient of user parameters
    Theta_grad(user, :) = err' * ratedMoviesFeatures + lambda * userParams;
end


% add the regularization term to J function
J = J + (lambda/2) * ( sum(Theta(:) .^ 2) + sum( X(:) .^ 2));

% =============================================================

grad = [X_grad(:); Theta_grad(:)];

end
