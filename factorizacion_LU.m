function x = factorizacion_LU(A, b)

    n = size(A, 1);
    if size(A, 2) ~= n
        disp('La matriz A no es cuadrada.')
        return;
    end
    if length(b) ~= n
        disp('El vector b no tiene el mismo número de filas que la matriz A.')
        return;
    end

    for i = 1:n
        A(i, i) = A(i, i) - A(i, 1:i-1) * A(1:i-1, i);
        if A(i, i) == 0
            disp('La matriz A no admite factorización LU.')
            return;
        end
        for j = i+1:n
            A(i, j) = A(i, j) - A(i, 1:i-1) * A(1:i-1, j);
        end
        for j = i+1:n
            A(j, i) = 1/A(i, i) * (A(j, i) - A(j, 1:i-1) * A(1:i-1, i));
        end
    end

    y = solve_for_y(A, b);  % Resolver L * y = b
    x = solve_for_x(A, y);  % Resolver U * x = y

end

function y = solve_for_y(A, b)
    n = size(A, 1);
    y = zeros(n, 1);
    for i = 1:n
        y(i) = b(i);
        for j = 1:i-1
            y(i) = y(i) - A(i, j) * y(j);
        end
    end
end

function x = solve_for_x(A, y)
    n = size(A, 1);
    x = zeros(n, 1);
    for i = n:-1:1
        s = 0;
        for j = i+1:n
            s = s + A(i, j) * x(j);
        end
        x(i) = (y(i) - s) / A(i, i);
    end
end

