

%M = randi([0 1], 50, 40);%
M = mushroom; %dataset

[m, n] = size(M);
indexes = 1:max(m,n);
A = M;
old = M;

% until the algorithm converge
while 1
    cost = zeros(size(A,1), 1); % barycenters
    
    % this can be easily vectorized for speed
    for i=1:size(A,1)
        cost(i) = sum(A(i,:) .* indexes(1:size(A,2))) / sum(A(i,:));
    end
    
    [~, perm] = sort(cost, 'ascend'); % check if direction plays a role
    B = A(perm,:);
    
    % if the result is not changig, stop
    if all(all(old==B))
        break;
    end
    
    A = B';
    old = A;
end

% plot results
figure
subplot(1,2,1);
imshow(~M);

subplot(1,2,2);
imshow(~A);

%%
figure
imshow(~A);