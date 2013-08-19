
k0 = 1.0;
kp = 0.8;
l  = 1.0;
A0 = 1.0;

function val = scattering_functional(A, B, C, D, mu, ll, lr)

val =   (A^2 + B^2) * (k0^2 * l / 4.0) \
      + (C^2 + D^2) * (kp^2 * l / 4.0 + (k0^2 + kp^2) / 2) \
      - mu * (A^2 + B^2 + C^2 + D^2 -1.0) \
      + ll * (A^2 - A0^2) + lr * D^2;

end

