Supponiamo di avere due grandezze $(x,y)$ e due set di dati $\{x_{i}, y_{i}\}$ a cui ad $y_{i}$ è associata un certo $\sigma_{i}$, mentre per $x_{i}$ non abbiamo $\sigma$. Supponiamo che esiste una legge che lega le due grandezze fisiche t.c. $y=f(x)$. Supponiamo che le y seguono una densità di probabilità t.c.
$$
P(y_{i};\theta) = \frac{1}{\sigma_{i} \sqrt{ 2\pi }} \exp\left[ -\frac{y_{i}-f(x_{i})^{2}}{2\sigma_{i}^{2}} \right]
$$
$$
\begin{gather}
\mathcal{L}(\vec{y}, \theta) = \prod_{i} P(y_{i}; \theta) \\
\ln\mathcal{L}(\vec{y},\theta) = -\sum_i \ln(\sigma_{i}\sqrt{ 2\pi }) = \frac{1}{2 \sum_i} \frac{(y_{i}-f(x_{i},\theta))^{2}}{\sigma_{i}^{2}} \\
\chi^{2} = \sum_i \frac{(y_{i}-f(x_{i},\theta))^{2}}{\sigma_{i}^{2}}  \\
\widehat{\theta} = \max \mathcal{L}  \\
\widehat{\theta} = \min \chi^{2}  \\
\implies \frac{d\chi^{2}}{d\theta} = 0 \implies \widehat{\theta}
\end{gather}
$$

Quindi arrivo ad avere un sistema da risolvere, ovvero 
$$
\begin{cases}
\frac{ \partial \chi^{2} }{ \partial \theta_{1} } = 0 \\
\frac{ \partial \chi^{2} }{ \partial \theta_{2} } =0 \\
\vdots
\end{cases}
$$
Ci apettiamo che se $y_{i} = f(x_{i}, \theta) + \epsilon_{i}, \text{ con } \epsilon_{i} \sim \mathcal{N}0, \sigma_{i}^{2}$, e quindi ho che $r_{i} = \frac{y_{i} - f(x_{i}, \theta)}{\sigma_{i}} \implies \mathcal{N}(0,1)$, dove quetsi $r_{i}$ sono i residui e mi dicono quanto un buon fit i miei parametri sono???????

Consideriamo il caso più semplice, dove $y=mx+q$, ovvero $f(x) = mx+q$. Assumiamo che $\sigma_{i} = \sigma$ Allora il mio $$
\chi^{2} = \sum_{i=1}^{N} (\frac{y_{i} - mx_{i} - q}{\sigma})^{2}
$$
Per il metodo dei minimi quadrati, avrò il sistema 
$$
\begin{gather}
\begin{cases}
\frac{ \partial \chi^{2} }{ \partial m } = 0 \\
\frac{ \partial \chi^{2} }{ \partial q } = 0
\end{cases}
\implies 
\begin{cases}
\sum_i  \frac{ \partial  }{ \partial m } (y_{i}-mx_{i}-q)^{2} = 0 \\
\sum_i \frac{ \partial  }{ \partial q } (y_{i} - mx_{i} - q)^{2} = 0
\end{cases} \\
\begin{cases}
\sum_i 2(-x_{1})(y_{i - mx_{i} - q}) = 0 \quad (1) \\
\sum_i 2(-1)(y_{i}-mx_{i} - q  ) = 0  \quad (2)
\end{cases} \\
(2) \implies \sum_i i_{i} - m\sum_i x_{i} - Nq = 0 \implies q = \overline{y} - m \overline{x} \\
\implies (\overline{x}, \overline{y})  \\
(1) \implies \overline{xy} - m \overline{x^{2}} - q \overline{x} = 0 \implies \overline{xy} - m \overline{x^{2}} - \overline{x}(\overline{y} - m\overline{x} ) = 0 \\
\implies \overline{xy} - m \overline{x^{2}} -\overline{x} \overline{y} + m(\overline{x}^{2}) = 0 \implies \widehat{m} = \frac{\overline{xy} - \overline{x} \overline{y}}{\overline{x^{2}} - \overline{x}^{2}} 
\end{gather}
$$
E una volta che ho la mia stima, posso risostituire nella $(2)$ e avrò 
$$
q = \overline{x} - \frac{\overline{xy} - \overline{x} \overline{y} }{\overline{x^{2}} - \overline{x}^{2}}\overline{x} = \frac{\overline{y} frac\overline{x^{2}} - \overline{y} \overline{x}^{2}+\overline{xy} \overline{x} - \overline{x}^{2} \overline{y}}{\overline{x^{2}} - \overline{x}^{2}} = \frac{\overline{y} \overline{x^{2}} - \overline{xy} \overline{x} }{\overline{x^{2}} - \overline{x}^{2}} = \widehat{q} 
$$

Definisco delle variabili intermedie $S_{xy} = \sum_i x_{i} y_{i}, S_{x} = \sum_i x_{i}, S_{y} = \sum_{i} y_{i}, S_{\times} \sum_i x_{i}^{2}$
Quindi avrò che 
$$
\begin{gather}
\widehat{m} = \frac{\frac{S_{xy}}{N} - \frac{S_{x}S_{y}}{N}}{\frac{S_{XX}}{N} - \frac{S_{x^{2}}}{N^{2}}} = \frac{N(S_{xy} - S_{x}, S_{y})}{N(S_{x x} - S_{x}^{2})} = \frac{N S_{xy} - S_{x} S_{y}}{D} \quad D = NS_{ x x }- S_{x}^{2} \\
\widehat{q} = \frac{S_{x x } S_{y} - S_{x} S_{xy}}{D} 
\end{gather}
$$
Questo è anche il modo che si ricava la propagazione degli errori 
