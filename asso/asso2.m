function [A,B] = asso2(M, k, tau, w_p, w_m)
% implements the Asso algorithm for BMF
% it utilizes R. Belohlavek's formalization of the Asso  

% init
[m, n] = size(M);
A = logical([]);
B = logical([]);
negM = ~M;

% association matrix
association_matrix = zeros(n,n);

for i=1:n
    for j=1:n
        if sum(M(:,i) .* M(:,j)) / sum(M(:,i)) > tau % warning: >= is not consitent with original Asso
            association_matrix(i, j) = 1;
        end
    end
end

% Asso algorithm 
for factor=1:k
    candidate_final_cover = zeros(1, m);
    final_column = cell(1,n);
    disp(factor);

    product = logical([A, false(m,1)] * [B; false(1, n)]);
    cover_base = w_p * sum(sum(M(product))) - w_m * sum(sum(negM(product)));
   
    % loop over all candidate (rows in association matrix)
    for j=1:size(association_matrix, 1)
        final_column{j} = false(m,1);
        candidate_row = association_matrix(j,:);
             
        % vectorized loop over all rows 
        changed = ~product & repmat(candidate_row, m, 1); % check only changed values
        %changed = bsxfun(@and, ~product, candidate_row); % quite slow

        covered_by_change = M & changed;
        overcovered_by_change = negM & changed;
        cover_aktualni = cover_base + w_p * sum(covered_by_change,2) - w_m * sum(overcovered_by_change,2);
        
        final_column{j}(cover_base < cover_aktualni) = 1;
              
        product_final = logical([A,final_column{j}] * [B; candidate_row]);
        candidate_final_cover(j) = w_p * sum(sum(M(product_final))) - w_m * sum(sum(negM(product_final)));
    end

    % find the best cadidate and add them to A and B
    [~, index] = max(candidate_final_cover);
    A = [A, final_column{index}];
    B = [B; association_matrix(index, :)];
end

end

