%load data

% toy example 12x10
M = zeros(12,10);
M(1:4,1:4) = 1;
M(4:7,4:7) = 1;
M(7:11,7:10) = 1;

% some errors
%M(3,3) = 0;
%M(7,7) = 0;
M(12,1) = 1;

M = M(randperm(12),:);
M = M(:,randperm(10));

% real data
M = double(zoo);

A = M;
no_of_iterations = 20;

%% bidirectional fixed permutation (Algorithm 2)

for iter=1:no_of_iterations
    [m,n] = size(A);

    W = A;
    % weights drives 0->1 and 1->0 flipping
    W(W==1) = 1;
    W(W==0) = -1;
    tosort = [];

    % solution of maximum subarray problem for each row
    for i=1:m
        X = max_sub_array(W(i,:)); % Kadane s algorithm
        tosort(i,1) = X(1);
        tosort(i,2) = X(2);
    end

    [~,perm] = sortrows(tosort);
    A = A(perm,:);
    A = A';

end

%% plot results

figure
subplot(1,2,1);
imshow(~M);

subplot(1,2,2);
imshow(imresize(~A, [size(A,1), size(A,2)*1]));
