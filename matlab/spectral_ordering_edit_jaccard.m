%load data

% toy example 12x10
%M = zeros(12,10);
%M(1:4,1:4) = 1;
%M(4:7,4:7) = 1;
%M(7:12,7:10) = 1;

% some errors
%M(3,3) = 0;
%M(7,7) = 0;

%M = M(randperm(12),:);
%M = M(:,randperm(10));

% real data
M = double(zoo);

%%
[m, n] = size(M);

%%

%Q = M'; % only if spectralcluster is used
%[~, V, D] = spectralcluster(Q, 2, 'Distance', 'jaccard');

%% START - direct implementation of spectralcluster()
% first we compute a similarity matrix S via (symetric) similarity measure
for i = 1:n

    for j = i:n
        % jaccard coef.
        inter = 0;
        x = M(:, i);
        y = M(:, j);

        for k = 1:m

            if x(k) && y(k)
                inter = inter + 1;
            end

        end

        un = sum(M(:, i)) + sum(M(:, j)) - inter;
        S(i, j) = inter / un;
        S(j, i) = inter / un;
        %S(i,j) = (1 + corr(M(:,i), M(:,j)))/2; % for now Pearson's coef.
        %S(j,i) = (1 + corr(M(:,i), M(:,j)))/2; % for now Pearson's coef.
    end

end

% then we compute Laplacian matrix from S
L = diag(diag(S)) - S;

% then we compute an Eigenvalues and Eigenvectors
[V, D] = eig(L);

% then we choose the second smallest Eigenvalue and the coresponding
% Eigenvector (i.e. Fiedler's vector)
[~, perm] = sort(diag(D), 'ascend');
column = V(:, perm(2));
%% END - direct implementation of spectralcluster()

% the column permutation is obtained via (nondecreasing) sorting of Fiedler's vector
column = V(:, 2); % only if spectralcluster is used

[~, perm] = sort(column, 'descend');
A = M(:, perm); % now, the comlums are sort, we need sort rows

disp(V);
disp(D);

%%
% simple sorting of rows, works goog on simple examples
% tosort = [];
% for i=1:m
%     tosort(i, 1) = find(A(i,:), 1, 'first');
%     tosort(i, 2) = find(A(i,:), 1, 'last');
% end
%
% [~,perm] = sortrows(tosort);

%% bidirectional fixed permutation (Algorithm 2)

W = A;
% weights drives 0->1 and 1->0 flipping
W(W == 1) = 1;
W(W == 0) = -1;
tosort = [];

% solution of maximum subarray problem for each row
for i = 1:m
    X = max_sub_array(W(i, :)); % Kadane s algorithm
    tosort(i, 1) = X(1);
    tosort(i, 2) = X(2);
end

[~, perm] = sortrows(tosort);

%% plot results
figure
subplot(1, 2, 1);
imshow(~M);

subplot(1, 2, 2);
C = ~A(perm, :);
imshow(imresize(C, [size(C, 1), size(C, 2) * 1]));
