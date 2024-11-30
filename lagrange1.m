
X = [1, 2, 3, 4, 5, 6, 7];
Y = [1.0000, 1.2599, 1.4422, 1.5874, 1.7100, 1.8171, 1.9129];
x_interp = 3.5;

function L = lagrange(X, Y, x_interp)
    n = length(X);
    L = 0;
    for i = 1:n
        term = Y(i);
        for j = 1:n
            if i != j
                term = term * (x_interp - X(j)) / (X(i) - X(j));
            end
        end
        L = L + term;
    end
end

resultado = lagrange(X, Y, x_interp);
fprintf('El valor interpolado en x = %.1f es: %.4f\n', x_interp, resultado);

