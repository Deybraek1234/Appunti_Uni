# Funzione Gamma
Questa funzione dipende da due parametri $\alpha$ e $\beta$, dove $x \in \mathbb{R} > 0$. 
>[!def] La funzione gamma è definita come 
>$$
> f(x, \alpha, \beta) = \frac{1}{\beta^\alpha  \Gamma(\alpha)} x^{\alpha-1}e^{ \frac{-x}{\beta} }
>$$
>dove con la $\Gamma(\alpha)$ indichiamo
>$$
>\begin{gather}
> \Gamma(\alpha) = \int_{0}^\infty z^{\alpha-1} e^{ -z } \; dz \\ 
> \Gamma(1) = \int_{0}^\infty e^{ -z } \; = 1  \\
> \Gamma\left( \frac{1}{2} \right) = \int_{0}^\infty e^{ -z }z^{-\frac{1}{2}} \; dz = \sqrt{ \pi } \; \; \; \; \text{avendo posto} z=\frac{y^{2}}{2} \\
> \Gamma(\alpha+1) = \int_{0}^\infty z^{\alpha-1} z e^{ -z } \; dz = \int_{0}^\infty z^{\alpha} e^{ -z } \; dz  \\
> = [z-^{\alpha} e^{ -z }]_{0}^\infty + \alpha \int_{0}*\infty z^{\alpha-1} e^{ -z } \; dz  \\
> = \alpha \Gamma(\alpha)
> \end{gather}
>$$ 
>dove nel caso di un numero intero abbiamo che $\Gamma(n+1) = n!$

La distribuzione gamma è:
* normalizzata: $\int_{0}^\infty x^{\alpha-1} e^{ -\frac{x}{\beta} } \; dx = \beta^\alpha \Gamma(\alpha)$
* ha valore di aspettazione $\mathbb{E}[x]=\alpha\beta$
* ha varianza $\text{Var}(x) = \beta^{2}\alpha$

# Distribuzione di Erlang
È un caso particolare della funzione di gamma con $\alpha = k$, dove $k \in \mathbb{Z}$, e $\beta = 1$. 
>[!def] La distribuzione di Erlang
>La distribuzione di Erlang segue la funzione
>$$
> f(x, k) = \frac{1}{(k-1)!} x^{k-1} e^{ -x }
>$$

Ha valore di aspettazione 
$$
\mathbb{E}[x] = \frac{1}{(k-1)!} \underbrace{ \int_{0}^\infty x^k e^{ -x } \; dx }_{ \Gamma(k+1)=k! } = k
$$
e ha varianza 
$$
\text{Var}(x) = \mathbb{E}[x^2] - \mathbb{E}[x]^2 = k
$$
il che segue dal fatto che 
$$
\mathbb{E}[x^2] =\frac{1}{(k-1)!}\underbrace{ \int_{0}^\infty x^{k+1} e^{ -x } \; dx }_{ \Gamma(k+2) = (k+1)! } = k^2 + k
$$

# Distribuzione dei tempi d'attesa
