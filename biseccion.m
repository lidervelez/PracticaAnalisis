f = @(x) nthroot(x, 3) - 2;

a = 0;
b = 10000;

tol = 0.0001;

iter = 0;
while (b - a) / 2 > tol
    iter = iter + 1;

    c = (a + b) / 2;

    fc = f(c);

    if fc == 0 || fc < tol
        break;
    endif

    if sign(fc) == sign(f(a))
        a = c;
    else
        b = c;
    endif
endwhile

fprintf('La raíz aproximada es: %.5f\n', c);
fprintf('Número de iteraciones: %d\n', iter);

