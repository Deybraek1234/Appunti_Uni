## Trattazione Generale
Vediamo ora qualche esempio più generali. Prendiamo un'equazione differenziale nella forma 
$$
\dot{x}= f(x, \mu)
$$
e supponiamo di avere un punto fisso iperbolico (quindi $f'(x^*, r_c) \neq 0$) $f(x^*, \mu^*) = 0$ per il punto $(x^*, \mu^*)$. Per capire la stabilità di $(x^*, \mu^*)$ possiamo linearizzare 
$$
\dot{\eta} = \left.\frac{\partial f}{\partial x} \right |_{(x^*, \mu^*)}\eta 
$$
e siccome 
$$
f(x^*, \mu^*) = 0 \; \; \; \; \; \text{e}   \; \; \; \; \left.\frac{\partial f}{\partial x} \right |_{(x^*, \mu^*)} \neq 0
$$
per il teorema della funzione implicita esiste un'unica funzione $x(\mu)$ t.c. $f(x(\mu), \mu) =0$ per $\mu$ abbastanza vicini a $\mu^*$ e $x(\mu^*)= x^*$. Per la continuità rispetto ai parametri, per $\mu$ vicini a $\mu^*$ $\frac{d }{d x}f(x(\mu),\mu) \neq 0$, quindi i punti fissi iperbolici rimangono iperbolici per piccole variazioni di $\mu$ e il carattere della stabilità non cambia. 

>[!rmk] I punti di biforcazione iperbolici hanno "stabilità" strutturale, quindi finché la derivata è diverso da zero non succede nulla.  (Conseguenza teorema della funzione implicita).

Se invece supponiamo che 
$$
\left.\frac{\partial f}{\partial x} \right |_{(x^*, \mu^*)} =0
$$
non possiamo più applicare il teorema della funzione implicita visto che la derivata parziale è zero e quindi la stabilità non è più garantita. Inoltre, abbiamo la definizione 
>[!def] Punto di biforcazionizione
>Un punto fisso $(x, \mu) = (0,0)$ di una famiglia a un parametro di campi vettoriali unidimensionali è detto avere una biforcazione se variando $\mu$ attorno lo zero il flusso cambia in modo qualitativo. 