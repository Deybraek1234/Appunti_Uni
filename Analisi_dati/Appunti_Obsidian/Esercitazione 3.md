Supponiamo di avere due variabili $L_{1}, L_{2}$ e conosco i valori veri $v_{1}, v_{2}$. Supponiamo di ripetere tante volte queste misure, e così genero un errore casuale. La mia misura, sarà 
$$
\begin{gather}
L_{1} = L_{1, v} + e_{1} \\
L_{2} = L_{2, v} + e_{2}
\end{gather}
$$
Supponiamo che questi errori $e_{1}, e_{2}$ seguono una normale 
$$
\begin{gather}
e_{1} = \mathcal{N}(0,\sigma^{2}) \\
e_{2} = N(0,\sigma^{2})
\end{gather}
$$
Inoltre, avremo che 
$$
\begin{gather}
L_{1} \sim \mathcal{N}(L_{1,v}, \sigma^{2}) \\
L_{2} \sim \mathcal{N}(L_{2,v},\sigma^{2})
\end{gather}
$$

Se invece le faccio correlare, si aggiunge un errore sistematico in entrambi i casi e quindi diventa 
$$
\begin{gather}
L_{1} = L_{1,v} + e_{1} + s \\
L_{2} = L_{2,v} + e_{2} + s
\end{gather}
$$
Le due misure cambiano allo stesso modo e quindi aggiunge un errore sistematico. Questo si simula facendo 
$$
S \sim \mathcal{N}(0, \sigma_{s}^{2})
$$
Quando andrò a prendere la $\text{cov}(L_{1,s}, L_{2,s}) \neq 0$. Avremo che $L_{1,s} = x+s$ e $L_{2,s} = y+s$ e allora 
$$
\begin{gather}
\text{cov}(L_{1,s}, L_{2,s}) = \text{cov}[(x+s)(y+s)] = \mathbb{E}[(x+s)(y+s)] - \mathbb{E}[x+s]\mathbb{E}[y+s] \\
=\mathbb{E}[xy] + \mathbb{E}[xs] + \mathbb{E}[sy] + \mathbb{E}[ss] - \mathbb{E}[x] \mathbb{E}[y] - \mathbb{E}[x] \mathbb{E}[s] - \mathbb{E}[s]\mathbb{E}[y] - \mathbb{E}[s] \mathbb{E}[s] \\
= \underbrace{ \text{cov}(x,y) }_{ 0 } + \underbrace{ \text{cov}(x,s) }_{ =0 } + \underbrace{ \text{cov}(y,s) }_{ =0 } + \text{cov}(s,s) \\
= \text{cov}(s,s) = \text{Var}(s)
\end{gather}
$$
Se facciamo un conto, vediamo che 
$$
L_{2,s} - L_{1,s} = L_{2,v} + e_{2} + s-L_{1,s} - e_{1} - s = L_{2,v} + e_{2} - (L_{1,v} + e_{2})
$$
Preso la media di queste misure, avrò che 
$$
m = \frac{L_{1,s} + L_{2,s}}{2} = \frac{L_{1,v} + L_{2,v}}{2} + \frac{e_{1} + e_{2}}{2} + s

$$
$$
\widehat{s} = \frac{L_{1,s} + L_{2,s}}{2} - \frac{\mu_{1} + \mu_{2}}{2}  
$$
