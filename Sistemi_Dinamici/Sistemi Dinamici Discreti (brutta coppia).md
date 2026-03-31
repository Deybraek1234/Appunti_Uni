Sono determinate da iterazioni di mappe. Prendiamo una funzione 
$f: \mathbb{R} \rightarrow \mathbb{R}$, e indichiamo con $f^n = f \circ \underbrace{ \dots }_{ \text{n volte} } \circ f$, con una data configurazione iniziale $x_{0}$. Definiamo:
$$
\begin{gather}
x_{1} &= f(x_{0}) \\
x_{2}  &= f(x_{1}) &= f^2(x_{0}) \\
\vdots \\
x_{n} &= f^n(x_{0})
\end{gather}
$$
e chiamiamo orbita del sistema dinamico $O^+ = \{x_{n}\}_{n\in\mathbb{N}}$ se ha tempi positivi mentre lo indichiamo con $O = \{ x_{n}\}_{n \in \mathbb{Z}}$ (esiste l'inverso) se ha sia tempi positivi sia negativi. 

>[!ex] Invertibile
>Preso il sistema $f(x) = x^{2}+1$ con un seed $x_{0} = 0$, avrò che $x_{1} = 1, x_{2} = 2, x_{3} = 5, x_{4} = 26, \dots$. 

Come per il caso continuo, esistono i punti fissi $x^*$. 
>[!def] Punti fissi
>Un punto $x^*$ per un sistema dinamico discreto si dice punto fisso se $f(x^*) = x^*$. Ovvero che l'orbita $O_{x^*} = \{x^*, x^*, x^*, \dots \}$. 

I sistemi dinamici discreti hanno una altra possibilità, ovvero abbiamo che un punto non sia fissato dalla mappa, ma che la mappa ritorna dopo un certo numero di iterazioni. 

>[!ex] 
>Dato una mappa $f(x_{1}) = x_{2}, f(x_{2}) = x_{1}$ avremo che è ciclico

>[!def] Punto Periodico
>Un punto periodico si dice di periodo n/n-ciclo se dopo n iterazioni il valore della mappa torna lo stesso valore. 
>Queste sono l'analogo discreto delle orbite periodiche. 

>[!def] Orbita Periodica
> Se $x_{1}, \dots, x_{n}$ si ripete, allora si parla di un orbita periodica. 

I sistemi dinamici continui, sull'asse periodica non potevano essere periodiche.
>[!ex] g(x) = -x^3
>Questa funzione ha un punto fisso $g(0)=0$
>Preso $g(\pm 1) = \mp 1$ $\rightarrow$ sono punti periodici di periodo 2
>$g^2(\pm 1) = \pm 1$

Ora proviamo a darli un interpretazione grafica a questi sistemi dinamici discreti. Consiste nel disegnare il piano x-f(x) e su questo sovrapponiamo la diagonale y=x. Per iterare la mappa, andiamo a vedere cosa succede ad un punto $x_{0}$ di partenza. 
![[Pasted image 20260319134905.png]]
Come vediamo in figura, usiamo la retta $x=y$ per visualizzare come si comporterà la soluzione. 
Possiamo avere casi più complessi come 
![[Pasted image 20260319135117.png]]
o potremmo semplicemente avere orbite chiuse 

Quindi preso un punto fisso, possiamo o parlare di punto fisso attrattivo, o repulsivo. Un punto fisso è detto un pozzo (attrattivo), se esiste un intorno di $x^*_{0}$ t.c. $\forall y_{0} \in U, f^n(y_{0}) \in U$ e $f^n(y_{0}) \xrightarrow{n  -> \infty} x^*_{0}$. 

>[!thm] 
>Dato una funzione $f: \mathbb{R} \rightarrow \mathbb{R}$, con $x_{0}$ un punto fisso allora 
>1. Se $|f'(x_{0})| < 1$ allora $x_{0}$ è un punto fisso attrattivo
>2. Se $|f'(x_{0})| > 1$ allora è repulsivo
>3. Se $|f'(x_{0})| = 1$ allora non possiamo dire niente
>>[!prf] 
>>1. Preso $|f'(x_{0})| = \nu < 1$ scegliamo k t.c. $\nu<k<1$. Se $f'$ è continua, allora esiste $\delta$ t.c. $|f'(x_{0})| < k \forall x \in I=[x_{0}-\delta, x_{0}+\delta]$. Allora per il teorema del valor medio, preso $x \in I$, troviamo $c \in [x, x_{0}]$ t.c. $f'(c) = \frac{f(x)-f(x_{0})}{x-x_{0}} = \frac{f(x)-x_{0}}{x-x_{0}}$ e siccome $c \in I$, allora $|f'(c)|<k$. Allora se prendo $|f(x)-x_{0}| < k|x-x_{0}|$, ma $k<1$ per ipotesi $\rightarrow f(x) \in I$. Iteriamo partendo da f(x), e arriviamo alla seconda iterazione, che dovrà ancora appartenere ad $I$, allora iterando n volte trovo che $|f^n(x)-x_{0}| < k^n|x-x_{0}|$ che per $n \rightarrow 0 f^n(x) \rightarrow x_{0}$.  Allora per $f^n(x) \xrightarrow{n  -> \infty} x_{0}$. 
>>2. In modo analogo
>>3. Preso $f(x) = x+x^3$ $g(x) = x-x^3$ e $h(x) = x+ x^2$ e vediamo che questi hanno andamenti diversi usando il metodo grafico. 

# Biforcazioni
Esistono anche le biforcazioni per quelli discreti. 

>[!thm]
>Preso una famiglia di sistemi dinamici dipendenti da un parametro $f_{\lambda}$, t.c. $f_{\lambda_{0}} = x_{0}$ ha un punto fisso, e supponiamo che $f'_{\lambda_{0}}(x_{0}) \neq 1$ e quindi esiste un intervallo $x_{0} \in I, \lambda_{0} \in J$, t.c. $p: J \rightarrow I$, t.c. $p(\lambda_{0})=x_{0}$, $f_{\lambda_{0}}(p(\lambda)) = p(\lambda)$. 

>[!prf] 
>Introduciamo la funzione $G(x, \lambda) = f_{\lambda}(x) -x \rightarrow G(x_{0}, \lambda_{0}) = f_{\lambda_{0}}(x_{0}) -x_{0} = 0$, t.c.
>$$
> \left.\frac{ \partial G }{ \partial x } \right \vert_{x_{0}, \lambda_{0}} = \left.\frac{\partial f_{\lambda}}{\partial x} \right |_{x_{0}, \lambda_{0}} -1 \neq 0
>$$ 
> Applico il teorema della funzione implicita a G e quindi esiste una funzione $p$ t.c. $G(p(x), \lambda) = 0$. 

Questo teorema ci dimostra perché per sistemi dinamici continui, valgono tanti dei teoremi, ma invece di 0 si sostituisce con 1. 

>[!ex] Cosa succede se prendo la seguente funzione
>Preso la funzione $f_{\lambda} (x) = x^2 + \lambda$. I punti fissi li trovo quando $f_{\lambda} = x^{2} + \lambda = x$, e quindi quando $x_{\pm} = \frac{1}{2} \pm \frac{\sqrt{ 1-4\lambda }}{2}$. 
>* se $\lambda > \frac{1}{4}$, non abbiamo punti fissi perché siamo in $\mathbb{R}$. 
>* se $\lambda = \frac{1}{4}$ ho un punto fisso
>* se $\lambda < \frac{1}{4}$ ho due punti fissi
>

le biforcazioni funzionano nello stesso modo che nel caso analogo. 

>[!ex] 
>Prendiamo la funzione $f_{\mu}(x) = -x -\mu x + x^{3} = x(x^{2}-(1+\mu))$. In questo modo abbiamo che $x_{n+1} = -x_{n} - \mu x_{n}+x^{3}_{n}$. I punti fissi sono quando $x=0, x^{2} =2+\mu$. Si può verificare che la stabilità di questi oggetti dipende dal valore di $\mu$. Questo si fa prendendo la derivata di $f' = -1 -\mu + 3x^{2}$ e prendendo il modulo si vede se è maggiore o minore di 1.  
>Se andiamo a vedere l'iterata seconda 
> questa è la mappa che $x \mapsto f^{2}_{\mu}(x) = f(f(x)) =  x + \mu(2+\mu)x - 2x^{3} + O(x^4)$. I punti fissi risultano essere $f^2 -x = \mu(2+\mu)x - 2x^{3}= 0$. Questi punti fissi sono sia i punti fissi di $f(x)$ sia punti di ciclo. 


>[!rmk] Un punto fisso per f(x), lo è anche per f(f(x)). 

>[!def] Periodic Doubling
>Un periodic-doubling biforcazione accade quando al crescere di r il sistema diventa sempre più instabile. 

# Mappa Logistica
>[!def] Mappa Logistica
>La mappa logistica si definisce come 
>$$
>\begin{align}
> x_{n+1} &= \lambda x_{n}(1-x_{n}) \\
> f(x) &=\lambda x(1-x)  &  &  \lambda > 0
> \end{align}
>$$

il che ha punti fissi per $\lambda x(1-x)=x$, e quindi per $x=0, x= \frac{\lambda -1}{\lambda}$. 
La funzione ha derivata $f'(x) = \lambda(1-2x)$ e quindi per $x=0, |f(0) = \lambda(1)|$ è attrattivo per $0 < \lambda < 1$, e repulsivo per $\lambda >1$. 
Per il secondo punto fisso, è attrattivo per $1<\lambda <3$ e repulsivo per $\lambda >3$. 

Prendiamo $\lambda= 4$, avremo che $f_{\lambda=4}\left( \frac{1}{2} \right) = 1$, iterata 2 volte, $f^2_{\lambda=4}\left( \frac{1}{2} \right)=f_{\lambda=4}(1)=0$, $f_{\lambda=4}(0)=0$, e allora questa mappa $f_{\lambda=4}\left( \left[0, \frac{1}{2} \right] \right) = f_{\lambda=4}\left( \left[ \frac{1}{2},1 \right] \right) = I$. Siccome manda tutti gli intervalli in $I$, allora devono esistere $y_{0}, y_{1}$, dove $y_{0} \in \left[ 0, \frac{1}{2} \right], y_{1} \in \left[ \frac{1}{2}, 1 \right]$ ma $f_{4}\left( \frac{1}{2} \right) = 1 \rightarrow f^2_{4}(y_{0})=f^2_{4}(y_{1})=1$. Abbiamo che $f^2_{4}([0,y_{0}]) = f^2_{4}\left( \left[ y_{0}, \frac{1}{2} \right] \right)= I$. e $f^2_{4}\left( \left[  \frac{1}{2}, y_{1} \right] \right) = f_{4}^2([y_{1}, 1]) = I$. Allora abbiamo che $f^n_{4}$ mappa $2^n$ intervalli in $I$. 

I punti fissi di $f^n$ sono n-cicli di f. $f^n$ ha n cicli, di cui qualcuno sarà ereditato da f, iterati n volte. 

>[!def] Funzione Caotica
>Una funzione f definita su $[\alpha, \beta], f: I \rightarrow I$ si dice caotica se valgono le seguenti: 
>1. Punti periodici di $f$ sono densi in I
>2. f è transitiva ($U_{1}, U_{2} \subset I, \exists x_{0} \in U_{1}$ e $n>0$ t.c. $f^n(x_{0}) \in U_{2}$). 
>3. f è sensibile alle condizioni iniziali ($\exists \beta \; t.c.\;  \forall x_{0} \in U \subset I, \; \exists y_{0} \in U, n>0, \; t.c. \; |f^n(x_{0}) - f^n(y_{0})| > \beta$. 

# Mappa a Tenda
>[!def] Mappa a Tenda
>La mappa a tenda è definita come 
>$$
> T(x) = 
> \begin{cases}
\begin{align}
> 2x  & &  0\leq x \leq \frac{1}{2} \\
> -2x+2  & &   \frac{1}{2} \leq x \leq 1
\end{align}
\end{cases}
>$$
![[Pasted image 20260319164213.png]]

Questa mappa ha la stesse proprietà della mappa logistica, ma essendo fatta di rette è più facile da analizzare. 
Andiamo a trovare i punti fissi, ovvero quando $T(x) = x$. Per $x \in [0, \frac{1}{2}], 2x = x \rightarrow x=0$. E per $x \in \left[  \frac{1}{2}, 1 \right], -2x+2 = x \rightarrow x = \frac{2}{3}$ 

Come è fatto l'iterato $T^2 (x) = T(T(x))$?
$$
T^2(x) = T(T(x)) = 
\begin{cases}
\begin{align}
2(2x)   &    &  0\leq 2x < \frac{1}{2} \\
2(1-2x)  &   &  \frac{1}{2} \leq 2x < 1 \\
2 \cdot 2(1-x)  &   &  0 < 2(1-x) < \frac{1}{2} \\
2 \cdot -2(2-2x) &  & \frac{1}{2} \leq 2(1-x) \leq 1 \\
\end{align}
\end{cases} 
= 
\begin{cases} 
4x &  & 0\leq x \frac{1}{4} \\
2-4x  &   &  \frac{1}{4} \leq x \leq \frac{1}{2}  \\
-2 + 4x  &   &  \frac{1}{2} \leq x \leq \frac{3}{4} \\
4 - 4x  &   &  \frac{3}{4} \leq x \leq 1
\end{cases}
$$
In questo modo possiamo andare a vedere i punti fissi dell'iterata 2 volte, ovvero $T^2(x) = x$. I punti fissi in questo modo risultano essere $x=0, x=\frac{2}{5}, x=\frac{2}{3}, x = \frac{4}{5}$. 
![[Pasted image 20260319165509.png]]
I punti 2/3 e 4/5 sono punti periodici di T con periodo 2. 

>[!rmk] $T^n$ ha $2^n$ punti fissi. 

>[!thm] T è caotica 
>Dim: 
>1. I punti periodici sono densi:
>Possiamo vedere che $T^n$ manda intervalli del tipo $\left[ \frac{k}{2^n}, k+\frac{1}{2^n} \right] \quad k \in \mathbb{N}$ in tutto $I=[0,1]$. Graficamente, $T^n$ interseca la diagonale 1 volta in ogni intervallo. Allora ogni $\left[ \frac{k}{2^n}, k+\frac{1}{2^n} \right]$ contiene un punto periodico per T. I punti periodici di T sono densi. 
>2. Transitività:
>Prendo $U_{1} \neq U_{2}$, t.c. $U_{1} = [\frac{k}{2^n}, \frac{k+1}{2^n}]$ $T^n$ per n grande manda $\left[ \frac{k}{2^n}, \frac{k+1}{2^n} \right]$ in tutto I. 
>3. Dipendenza dati iniziali:
>Preso $x_{0} \in U$, posso anche scegliere un $x_{k} \in [\frac{k}{2^n}, \frac{k+1}{2^n}$ che viene mandato in tutto $I$, e esiste un $y_{0} \in U$ t.c. $|T^n(y_{0}) - T^n(x_{0})| > \frac{1}{2} = \beta$
>
> Visto che valgono i tre punti, T è caotica. 

Consideriamo due intervalli, $I, J$ e due sistemi dinamici, $f:I \rightarrow I$ e $g: J \rightarrow J$, due sistemi dinamici. 
>[!def] Sistemi Dinamici Coniugate
>Diciamo che f e g sono due sistemi dinamici coniugate se esiste h omeomorfismo (continua, biunivoca, inversa continua), $h: I \rightarrow J$ t.c. il diagramma commuta 
>$$
> \begin{matrix}
> I & \xrightarrow{f}  & I \\
> {h}\downarrow  &  & {h}\downarrow \\
> J & \xrightarrow{g}  & J
\end{matrix}
>$$
>ovvero se ($h \circ f = g \circ h$).

>[!thm] Se due sistemi dinamici sono coniugati, abbiamo che h porta orbite di f in orbite di g. 
>Ho che $h(f^n(x)) = g^n(h(x))$ 
>Questo è evidente dalla iterazione del diagramma
>$$
> \begin{matrix} \\
> I  & \rightarrow  & I  & \rightarrow  & \dots & \rightarrow  & I \\
> \downarrow  &  & \downarrow &  & \dots &  & \downarrow \\
> J & \rightarrow & J & \rightarrow & \dots & \rightarrow & J \\
\end{matrix}
>$$
> e come vedo, non importa in che direzione percorro il diagramma, comunque arrivo allo stesso risultato. 

>[!thm] H porta sistemi caotici in sistemi caotici. 
>Dato $f:I \rightarrow I$ e $g: J \rightarrow J$ coniugate da $h: I \rightarrow J$, allora $f$ caotica $\implies g$ caotica

>[!prf] 
>Preso $U \subset J$ e consideriamo $h^{-1}(U) \subset I$,  
>1. se f caotica $\implies$ punti periodici sono densi. Posso trovare un $x\in h^{-1}(U)$ punto periodico di periodo n. Posso prendere $h(f^n(x)) = g^n(h(x))$, ma visto che x è un punto periodico, $f^n(x) = x$. Allora $h(x)$ è un punto periodico di periodo n e i punti periodici di g sono densi. 
>2. Presi $U, V \subset J$ per la transitività di f, esiste $x = \in h^{-1}(U)$ e m t.c. $f^m(x) \in h^{-1} (V)$. Ma se $h(x) \in U$, abbiamo anche che $g^m(h(x)) = h(f^m(x)) \in V$. Questo vuol dire che dato due intorni ho un elemento che viene mandato dal primo al secondo per qualsiasi coppia di intorni, e quindi g è transitiva. 
>3. (sketch) Preso $I=[\alpha_{0}, \alpha_{1}]$, sia $\beta$ la costante di sensibilità di $f$ t.c. $\beta < \alpha_{1} - \alpha_{0}$. Per ogni $x\in [\alpha_{0}, \alpha_{1} - \beta]$ andiamo a vedere $|h(x+\beta) - h(x)|$ il che risulta continua in $[\alpha_{0}, \alpha_{1}-\beta]$ ed è positiva $\implies$ ha un valore minimo: $\beta'$. Quindi $h$ prende intervalli di lunghezza $\beta$ in $I$ e li manda in intervalli di lunghezza almeno $\beta'$ in $J$. Allora prendo $\beta'$ come costante di sensibilità. 

Non è necessario che $h$ sia biunivoca (1 a 1), ma può essere suriettiva (N a 1), che soddisfa le stesse proprietà. In questo caso parliamo di una semi-coniugazione. 
Una semi-coniugazione manda sistemi caotici in sistemi caotici ma non preserva il periodo. 

>[!thm] $f_{4}(x) = 4x(1-x)$ è caotica
>

>[!prf] 
>Preso la coniugazione $h(x) = \frac{1}{2}(1-\cos 2\pi x)$, è 2 ad 1 su $[0,1]$ tranne che in $\frac{1}{2}$. È continua perché è un coseno e abbiamo che 
>$$
> h(T(x)) = 
> \begin{cases}
> \frac{1}{2} \left( 1 - \cos 4\pi x \right) &  & 0 \leq x \leq \frac{1}{2} \\
> \frac{1}{2}(1- \cos[2\pi (-2x+2)])  &   &  \frac{1}{2} \leq x \leq 1
\end{cases}
>$$
> il che è uguale a 
>$$
>\begin{align}
> h(T(x)) &= \frac{1}{2}(1-\cos 4\pi x)  \\
& = \frac{1}{2} - \frac{1}{2}(2\cos ^{2} (2\pi x) -1)  \\
& = 1 - \cos ^{2}(2\pi x)  \\
& = 4\left( \frac{1}{2} - \frac{1}{2}\cos(2\pi x) \right)\left( \frac{1}{2}+\frac{1}{2}\cos(2\pi x) \right) \\
> & = f_{4}(h(x))
> \end{align}
>$$
>il che è una coniugazione, e quindi per questo valore la mappa logistica è caotica. 

# Esponente di Liapunov
Questo ci da una misura qualitativa del caos. Se succede questa cosa, allora mi posso aspettare che sia caotico. L'Idea è che possiamo andare a vedere se il tasso di repulsione/attrazione di due traiettorie vicine è esponenziale. 
Prendiamo $x_{n+1} = f(x_{n})$ e $x_{0}, x_{0+\varepsilon}$. Definiamo 
$$
\lambda = \lim_{ 
\begin{gather}
N \to \infty  \\
\varepsilon \rightarrow 0
\end{gather}
} 
\frac{1}{N} \ln \frac{|f^N(x_{0}+\varepsilon)- f^N(x_{0}))}{\varepsilon}
$$
l'Idea è di scrivere 
$$
\lambda = \lim_{ 
\begin{gather}
n \to \infty  \\
\varepsilon \rightarrow 0 \\
\end{gather}
} e^{ \lambda N }= \lim_{ n \to \infty, \varepsilon \rightarrow 0 } \frac{|f^N(x_{0}+\varepsilon )- f^N(x_{0})|}{\varepsilon} 
= \lim_{ N \to \infty} \frac{1}{N} \log \left.\frac{df^n}{dx}\right \vert_{x_{0}} 
= \lim_{ N \to \infty } \log|(f^{(n)})'(x_{0})|
$$

E quindi così abbiamo che 
$$
\lambda = \lim_{ N \to \infty } \log |(f^{(n)})'(x_{0})|
$$
Studio il logaritmo perché voglio pensare a $\lambda$ come qualcosa che misura asintoticamente quanto le traiettorie $f^n(x_{0}+\varepsilon) - f^n(x_{0})$ si distaccano in maniera esponenziale. 
Riscriviamo il termine trovato prima facendo dei conti:

>[!prf] 
>$$
>\begin{align}
> (f^n)(x_{0})  & = [f(f^{N -1})]'(x_{0}) = [f'(f^{N-1})](x_{0}) \cdot (f^{N-1})'(x_{0}) \\
> & = [f'(f^{N-1})](x_{0}) \cdot [f'(f^{N-1})]{x_{0}} \cdot [f^{N-2}]'(x_{0}) \\
>  & \vdots \\
>  & =[f'(f^{N-1})](x_{0}) \cdot [f'(f^{N-2})](x_{0}) \cdot \; \dots \; \cdot [f'(f(x_{0}))]\cdot f'(x_{0})
> \end{align}
>$$
>dove abbiamo usato la derivata della funzione composta e ci abbiamo iterato su. 
> Ma, sappiamo che $f(x_{0}) = x_{1}$ visto che è la prima iterazione. Così via, ripetendo avremo che $f^{N-3}(x_{0}) = x_{N-3}$, etc, etc. Quindi, possiamo scrivere che 
> $$
> (f^n)(x_{0}) = \prod_{i=0}^{n-1}f'(x_{i})
> $$
> E allora avremo che 
>$$
> \begin{align}
> \lambda  & = \lim_{ N \to \infty } \log|f(^n)'(x_{0})|  \\
> & = \frac{1}{N} \lim_{ N \to \infty } \log \left.\vert\prod_{i=0}^{N-1} f'(x_{i}) \right.\vert \\
> & = \lim_{ N \to \infty } \frac{1}{N} \sum_{i=0}^{N-1} \log |f'(x_{i})|
\end{align}
>$$ 

>[!def] k-ciclo stabile
>Se abbiamo un punto fisso $x_{0}$, sappiamo che un punto fisso è stabile se
>$$
> |f'(x_{0})| < 1
>$$
>Quindi, possiamo dire che un k-ciclo è stabile se 
>$$
> |(f^k)'(x_{0})| < 1
>$$
>Se $|(f^k)'(x_{0})| = 0$, allora il ciclo si dice superstabile. (è la condizione più stabile che può avere un ciclo). Avremo che 
>$$
> \lambda = \frac{1}{n} \log 0 = -\infty
>$$


>[!ex] k-ciclo
>Prendiamo un k-ciclo stabile, ovvero che 
>$$
> \log |(f^k)'(x_{0})| < \log 1 = 0
>$$
> Per definizione, e usando il fatto che abbiamo un k-ciclo abbiamo che 
>$$
>\begin{align}
> \lambda  & = \lim_{ N \to \infty } \frac{1}{N} \sum_{i=0}^{N-1} \ln | f'(x_{i})| \\
>  & = \frac{1}{k} \sum_{i=1}^{k-1} \ln | f'(x_{i})|
> \end{align}
>$$
>(questo si può fare perché stiamo prendendo il limite per $n \rightarrow \infty$ per una somma di oggetti, che però si continuano a ripetersi (k-ciclo). Quindi avremmo un pezzo costante $\frac{1}{p}$ che è costante, e un'altra correzione che va a zero (sommatoria)). 
>Si può verificare 
>$$
>\begin{align}
 \\
> \bar{x}  & = \frac{1}{n} \sum_{i=1}^{n} x_{i}  \\
 & = \frac{1}{n} \left( \left[ \frac{n}{p} \right] \sum_{i=1}^{p_{i}} x_{i} + \sum_{j=1}^{n \text{ mod } p} x_{i} \right) \\
 & = \frac{\frac{n}{p}}{\frac{n}{p}} \sum_{i=1}^{p} \frac{x_{i}}{p} + \frac{1}{n} \sum_{j=1}^{n \text{ mod } p} x_{i} \\
 & \xrightarrow{n  -> \infty} \sum_{i=1}^{p} \frac{x_{i}}{p} + 0
\end{align}
>$$
(i termini ripetuti sopravvivono, mentre quelli non ripetuti vengono uccisi dal fattore $\frac{1}{N}$ e abbiamo preso la parte intera di $\frac{n}{p}$). 
> Quindi l'esponente si può scrivere 
>$$
> \begin{align}
> \lambda  & = \frac{1}{k} \ln |(f^k)'(x_{0})| < 0
\end{align}
>$$
>quindi se abbiamo un k-ciclo stabile, le orbite hanno esponente di Liapunov negativo e quindi le traiettorie tendono a convergere. 

>[!ex] Mappa Tenda
>Verifichiamo che per la mappa tenda, che è caotica, l'esponente di Liapunov è positivo. 
>Generalizziamo la mappa ulteriormente sotto la forma 
>$$
> T(x) = 
> \begin{cases}
> \begin{align}
> 2rx  &   &  0 \leq x \leq \frac{1}{2} \\
> 2r(1-x)  &   &  \frac{1}{2} \leq x \leq 1
\end{align}
\end{cases}
>$$
>Abbiamo che 
>$$
> |T(x)| = 2r \quad \forall x \in [0,1], \; x \neq \frac{1}{2}
>$$
Per $x \neq \frac{1}{2}$, avremo che 
>$$
>\begin{align}
>\lambda  & = \lim_{ N \to \infty } \frac{1}{N} \sum_{i=0}^{N-1} \log|T'(x_{i})| \\
>  & = \lim_{ N \to \infty } \frac{1}{N} \sum_{i=0}^{N-1} \log 2r  \\
>  & = \lim_{ N \to \infty } \log 2r \frac{1}{N} \underbrace{ \sum_{i=0}^{N-1} 1 }_{ = N } \\
>  &  = \log 2r ( > 0 \text{ per r > 1/2})
>\end{align}
>$$
> e quindi come ci aspettavamo, la mappa quando è caotica ha traiettorie che divergono esponenzialmente. 

Quindi abbiamo che l'esponente di Liapunov non è un se solo se, ma è un test qualitativo del se la mappa potrebbe essere caotica. 

# $\lambda > 4$
Consideriamo ora il caso $\lambda > 4$. 
Quando $\lambda > 4$, abbiamo che il massimo della campana supera 1. 2
![[Pasted image 20260324150302.png]]
quindi l'intervallo $I = [0,1]$ non è più invariante. Se $\lambda > 4 \implies \exists \; \text{intervallo  }\;  A_{0}  \; t.c. \; f_{\lambda}(x) = \lambda x(1-x) > 1$.  Quindi, abbiamo che alcuni punti quando vanno a toccare la bisettrice, scende giù e tocca la campana quando è minore di uno e viene mandato ad infinito. Gli estremi di $A_{0}$ (quando $f_{\lambda}(x) = 1$) vanno in $f_{\lambda}(1) = 0$ (0 è punto fisso). 
Vogliamo capire l'insieme
$$
\begin{gather}
\Lambda = \{ \text{Tutti i punti di }I=[0,1] \text{ t.c. le orbite non escono da I}\} \\
\Lambda = \{\text{ Tutti i x che non escono}\}
\end{gather}
$$
L'unico problema è che possiamo avere certi punti fuori da $A_{0}$ che dopo una certa iterata ci entrano dentro e quindi vengono mandati fuori dall'intervallo. 

Definiamo $A_{1}$ la preimmagine di $A_{0}$ (l'inseme dei punti che va in $A_{0}$). $A_{1}$ è formato da 2 intervalli, e gli estremi vengono mandati negli estremi di $A_{0}$ e quindi in 0. Similmente, se si va prendere le preimmagini di $A_{1}$ si trova che è fatto da altri 4 intervalli. Quindi, $A_{2}$ è costituito da 4 intervalli e iterando, avremo che $A_{n}$ è costituito da $2^n$ intervalli. 
Usando questo, vogliamo rispendere alla domanda: come è fatta $\Lambda$?
Prendiamo $I \; \backslash \;  A_{0} = I_{0} \cup I_{1}$ allora se $x \in \Lambda$, l'orbita di $x$ sta dentro $I_{0} \cup I_{1}$. Ad x, associo una sequenza  $S(x) = (s_{0}, s_{1}, s_{2}, s_{3}, \dots)$, dove $S_{j} = k, \; k = 0,1 \iff f^j_{ \lambda}(x) \in I_{k}$. Ad esempio: 
* $S(0) = (0, 0, 0, \dots)$ (punto fisso)
* $S(x^*) = (1, 1, 1, \dots)$ (punto fisso)
* $S(1) = (1, 0, 0, ...)$ 

>[!def] L'insieme delle sequenze
>Definiamo $\Sigma$ l'insieme di tutte le sequenze di 0 e 1
>$$
> S \in \Sigma, \; S = (s_{0}, s_{1}, s_{2}, \dots)
>$$
> Possiamo dotare $\Sigma$ di una distanza, così $\Sigma$ è uno spazio metrico, allora esiste una distanza con le proprietà
>$$
> \exists s, t \in \Sigma, d(s,t) \text{ t.c}
>$$
> 1. $d(s,t) \geq 0, d(s,t) = 0 \iff s=t$
> 2. $d(s,t) = d(t,s)$
> 3. $d(s,u) \leq d(s,t) + d(t,u)$ (disuguaglianza triangolare)
> Definisco la distanza fra $s,t$ come 
>$$
> d(s,t) = \sum_{i=0}^{\infty} \frac{\left.\vert s_{i} - t_{i}\right.\vert}{2^i}
>$$
>in questo modo ho che la mia distanza è limitato superiormente da (essendo s,t o 0 o 1) 
>$$
> d(s,t) \leq \sum_{i=0}^{\infty} \frac{1}{2^i} = \frac{1}{1-\frac{1}{2}} = 2
>$$
>dove si è usato il fatto che la serie era una geometrica

>[!ex] 
>$d((\bar{01}), (\bar{10})) = \sum_{i=0}^{\infty} \frac{1}{2^i} = 2$
>Ho che le sequenze sono 
>$$
> \begin{align}
> 0 1 0 1 0 1 \dots \\
> 1 0 1 0 1 0 \dots \\
> 1 1 1 1 1 1 \dots
\end{align}
> = d((\bar{01}, \bar{10})) = \sum_{i=0}^{\infty} \frac{1}{4^i}= \frac{1}{1- \frac{1}{4}} = \frac{4}{3}
>$$

Non so come è fatta $\Lambda$ ma so che a tutti i punti ci posso associare una sequenza infinita. 

>[!thm] 
>Prendiamo $s,t \in \Sigma$, allora 
>1. se $s_{i} = t_{i}, \; i = 0, \dots, n \implies d(s,t) \leq \frac{1}{2^n}$  
>2. se $d(s,t) < \frac{1}{2^n} \implies s_{i} = t_{i}, \; i = 0, \dots, n$

>[!prf] 
>Preso la distanza 
>$$
> d(s,t) = \sum_{i=0}^{\infty} \frac{|s_{i} - t_{i}|}{2^i}
>$$
>1. 
>$$
> d(s,t) = \sum_{i=0}^{n} \frac{s_{i} - s_{i}}{i^2} + \sum_{i=n+1}^{\infty} \frac{|s_{i}-t_{i}|}{2^i} \underbrace{ \leq }_{ i = j + n + 1 } 0 + \frac{1}{2^{n+1}} \underbrace{ \sum_{j=0}^{\infty} \frac{1}{2^j} }_{ =2 } = \frac{1}{2^n}
>$$
>2. Se  $d(s,t) < \frac{1}{2^n}$, deve essere che $s_{j} = t_{j}$ per ogni $j\leq n$, altrimenti $d(s,t) \geq \frac{s_{j}- t_{j}}{2^j} = \frac{1}{2^j} \underbrace{ \geq }_{ \text{perché } j \leq n } \frac{1}{2^n}$ 
>Viceversa 
>$$
> d(s,t) < \frac{1}{2^n} \implies s_{i} = t_{i} \; i = 0, \dots, n
>$$

>[!thm] 
>La funzione $\begin{align}S:  & \Lambda \rightarrow \Sigma \\  & S \mapsto (s_{0}, s_{1}, \dots)\end{align}$ itinerario è un omeomorfismo (mappa continua con inversa continua). 

>[!prf] (Sketch)
>Per semplicità assumiamo $\Lambda$ "grande". Quindi, assumiamo 
>$$
> |f_{\lambda}'(x)| > k > 1 \; \; \forall x \in I_{0} \cup I_{1}
>$$
>*Dimostriamo che è 1 ad 1 (Iniettività):*
>Preso $x, y \in \Lambda$ e supponiamo che $S(x) = S(y)$ (stesso itinerario). Allora, abbiamo che $\forall n, f_{\lambda}^n(x) e f_{\lambda}^n(y)$ stanno dallo stesso lato di $\frac{1}{2}$ (ovvero che $\forall n$ stanno o in $I_{0}$ o $I_{1}$.) Siccome stanno nello stesso lato, $f_{\lambda}$ è monotona nell'intervallo tra $f_{\lambda}^n(x)$ e $f_{\lambda}^n(y)$. Ma $f$ ha la proprietà che $|f_{\lambda}^n(x)| > k > 1$. Ad ogni iterazione, l'intervallo tra $f_{\lambda}^n(x)$ e $f_{\lambda}^n(y)$ viene espanso di k. Ad ogni iterazione, la distanza cresce ed eventualmente si troveranno da due lati diversi rispetto al punto medio ($x=\frac{1}{2}$), in contraddizione con il fatto che $S(x) = S(y)$. 
>
>*Suriettività:*
>Preso $S = (s_{0}, s_{1}, \dots)$ troviamo $x \in \Lambda$ t.c. $S(x) = s$. Possiamo prendere 
>$$
>\begin{align}
> I_{{s_{0}, s_{1}, \dots, s_{n}}}  & = \{ x \in I  | x \in I_{s_{0}}, f(x) \in I_{{s_{1}}}, \dots, f^n(x) \in I_{s_{n}} \} \\
> & = I_{s_{0}} \cap f_{\lambda}^{-1}(I_{s_{1}}) \cap f^{-2}_{\lambda}(I_{s_{2}})\cap \dots \cap \dots f^{-n}_{\lambda}(I_{s_{n}})  \\
> & = I_{s_{0}} \cap f^{-1}_{\lambda}(I_{s_{1}, \dots, s_{n}})
\end{align}
>$$
> Per induzione, $I_{s_{1}, \dots, s_{n}}$è non vuoto, e $f^{-1}_{\lambda}(I_{s_{1}, \dots, s_{n}})$ sono 2 intervalli, uno in $I_{0}$ e uno in $I_{1}$. $\implies$ $I_{s_{0}} \cap f^{-1}_{\lambda}(I_{s_{1}}, \dots, s_{n})$ è un intervallo singolo. Quindi abbiamo che 
>$$
>\begin{align}
> I_{s_{0}, \dots, s_{n}} = I_{s_{0}, \dots, s_{n}} \cap f^{-1}_{\lambda}(Is_{n}) \subset I_{s_{0}, \dots, s_{n-1}}
>\end{align}
>$$
> Quindi 
> $$
> \bigcap^\infty_{n=1}I_{s_{0}, \dots, s_{n}} \text{non vuoto}
> $$
> E avremo che $x \in \bigcap^\infty_{n=1}I_{s_{0}, \dots, s_{n}}$ è t.c. $x \in I_{s_{0}}, f_{\lambda}(x) \in I_{s_{1}}, f_{\lambda}^2(x)\in I_{s_{2}}, \dots$ con $S(x) = (s_{0}, s_{1}, \dots)$. 
> *Continuità:*
> Preso $x \in \Lambda, S(x) = (s_{0}, s_{1}, s_{2} \dots)$. Prendiamo $\varepsilon>0$ e $n$ t.c. $\frac{1}{2^n} < \varepsilon \forall$ combinazione $t, t_{1},\dots, t_{n}, I_{t_{0}, t_{1}, \dots, t_{n}}$. Così abbiamo $2^{n+1}$ intervalli $I_{s_{0}, \dots, s_{n}}$ è uno di questi. Sapendo che $\Lambda \subset \bigcup I_{t_{0}, \dots, t_{n}}$ posso scegliere $\delta$ t.c. $|x-y| < \delta$ con $y \in \Lambda \implies y \in I_{s_{0}, \dots, s_{n}}$. Visto che $y$ appartiene a questo intervallo, vuoldire che i primi $n+1$ termini di $S(y)$ coincidono con quelli di $S(x)$ e quindi 
>$$
> d(S(x), S(y)) \leq \frac{1}{2^n} < \varepsilon
>$$
>e quindi la funzione S è continua. 
>*Inversa è continua*:
>Si dimostra in maniera analoga

>[!def] Mappa Shift
>Definiamo la mappa shift
>$$
>\begin{align}
> \sigma :  & \Sigma \rightarrow \Sigma \\
>  & \sigma(s_{0},s_{1},s_{2},\dots) \mapsto (s_{1}, s_{2}, s_{3}, \dots)
> \end{align}
>$$
>E questa mappa risulta essere
>1. caotica
>2. coniugata a $f_{\lambda}$
>3. facile
>La mappa è 2->1, perché si mangia la prima entrata, quindi 
>$$
> \begin{align}
> \sigma(0,s_{1},s_{2},s_{3},\dots)  & = \sigma(1,s_{1},s_{2},s_{3},\dots) \\
 & = (s_{1},s_{2},s_{3},\dots)
\end{align}
>$$

Quali sono i punti periodici di $\sigma$:
* $(\bar{0})$,  $(\bar{1})$ - fissi
* $\bar{(0,1)}$,  $(\bar{1,0})$ - 2 cicli
* $(\bar{s_{0}, \dots, s_{n-1}})$

>[!thm] La Mappa Shift è una mappa continua (nell'insieme in cui è definita), rispetto alla metrica definita in precedenza. 

>[!prf] 
>Prendiamo una sequenza $S = (s_{0}, s_{1}, s_{2}, \dots) \in \Sigma$. Sia $\varepsilon> 0$ e $n$ t.c. $\frac{1}{2^n} < \varepsilon$. Poniamo $\delta = \frac{1}{2^{n+1}}$.  Se $t = (t_{0}, t_{1}, t_{2}, \dots)$ t.c. $d(s,t) < \delta \implies s_{i} = t_{i} \; \forall i = 0, \dots, n+1$.  Applicando la mappa shift, abbiamo che $\sigma(s) = (s_{1}, s_{2}, s_{3}, \dots), \; \sigma(t) = (s_{1}, s_{2}, s_{3}, \dots, s_{n}, s_{n+1}, t_{n+2}, ..)$ $\implies d(\sigma(s),\sigma(t))\leq \frac{1}{2^n} < \varepsilon$. 
(Dimostrazione si fa usando il teorema precedente )

>[!thm] $S: \Lambda \rightarrow \Sigma$ è una coniugazione tra $f_{\lambda}$ e $\sigma$. 

>[!prf] 
>Sappiamo che $S$ è un omeomorfismo, allora dobbiamo dimostrare che $S \circ f_{\lambda} = \sigma \circ S$. Sia $x_{0} \in \Lambda$,  $S(x_{0}) = (s_{0}, s_{1}, s_{2}, \dots)$ quindi $x_{0} \in I_{s_{0}}$, $x_{1} = f_{\lambda}(x_{0}) \in I_{s_{1}}, x_{2} = f^2_{\lambda} \in I_{s_{2}}$. Vado a prendere $S(\underbrace{ f_{\lambda}(x_{0} }_{ =x_{1} })) = (s_{1}, s_{2}, s_{3}, \dots) = \sigma(S(x_{0}))$ così dimostrando il teorema.
>Questo è perché facendo $f_{\lambda}(x_{0}) = x_{1}$ e quindi mi fa saltare il primo elemento dell'orbita. Questo è equivalente a cosa fa $\sigma$. 

>[!thm] La mappa $\sigma$ è caotica in $\Sigma$. Quindi $f_{\lambda}$ è caotica in $\Lambda$ per $\lambda > 4$

>[!prf] 
>Per dimostrare questo, voglio costruire un'orbita densa. Innanzitutto, cosa vuoldire un orbita densa? È un orbita che va arbitrariamente vicino a qualsiasi punto. Costruisco questa orbita in questo modo 
>$$
>S^* = (\underbrace{ 0, 1| }_{ \text{Primo Blocco} } \underbrace{ 0 0, 0 1, 10, 11,| }_{ \text{secondo blocco} } 000, 001, 010, 011, \dots | \dots)
>$$
>Questa è densa perché presso $t = (t_{0}, t_{1}, t_{2}, \dots) \in \Sigma$ e da questa sequenza guardo i primi $n+1$ termini $t_{0}, \dots, t_{n}$. Questi termini li vado a cercare dentro $S^*$, nella quale ci saranno sicuramente per il fatto che $S^*$ becca tutte le sequenze, $\implies \exists k \; \text{t.c.} \; \sigma^k(s^*) = (t_{0}, t_{1}, \dots, t_{n} s_{n+1}, s_{n+2})$. Questo vuoldire che $d(\sigma^k(s^*), t) \leq \frac{1}{2^n}$ e quindi l'orbita di $s^*$ sotto $\sigma$ passa arbitrariamente vicino ad ogni punto di $\Sigma$, ovvero è densa, e la mappa è transitiva. Non abbiamo trovato solo un punto con un orbita densa, ma infinita punti. 
>Inoltre i punti periodici sono densi: 
>$$
>\begin{gather}
>t = (t_{0}, t_{1}, t_{2}, \dots) \\
>s = (t_{0}, t_{1}, t_{2}, \dots, t_{i})
>\end{gather} \implies d(s,t) \leq \frac{1}{2^i}
>$$
>e $\lim_{ i \to \infty }d(s,t) = 0$. Quindi, dato un punto qualsiasi posso trovare un orbita periodica arbitrariamente vicino e quindi i punti periodici sono densi. 
> Lo stesso risultato per la mappa logistica è difficile vederlo. 
>Sensibilità ai dati iniziali: 
>Preso $S = (s_{0}, s_{1}, \dots, s_{n}, s_{n+1}, \dots)$ e $S' = (s_{0}, s_{1}, \dots, s_{n}, \hat{S}_{n+1}, \hat{S}_{n+2}, \hat{\dots})$ abbiamo che $d(s, s') \leq \frac{1}{2^n}$ e $d(\sigma^{n+1}(s), \sigma^{n+1}(s')) = 2$. Quindi dato due punti arbitrariamente vicino, trovo che ho due punti che vengono mandati in due posti completamente opposti, e quindi massimizzando la distanza
>

Quindi, abbiamo che $\sigma$ caotica ma calcolabile e $f_{\lambda} \; \lambda > 4$ è caotica. 

# L'insieme di Cantor
$\Lambda$ definito in precedenza è un esempio di un insieme chiamato un insieme di Cantor. 

>[!def] Insieme di Cantor C
>Definisco l'insieme C in questo modo:
>Definisco l'intervallo $[0,1]$ e applico la seguente regola:
>Prendo un intervallo chiuso, lo divido in tre, e tolgo l'intervallo aperto in mezzo. 
>![[Pasted image 20260326150528.png]]

Al passo n troviamo $2^n$ intervalli chiusi di lunghezza $\frac{1}{3^n}$. 
$C \xrightarrow{n  -> \infty}S_{n}$. 

>[!def] Indirizzo
>Per ogni punto di C, definisco il suo indirizzo nel seguente modo:
>* ad ogni passo, un punto di C si trova in uno degli intervalli a destra (R), o a sinistra (L) dei pezzi rimosso. In questo modo, gli associamo una stringa: (RRLLRLRLL...). 

Esempi:
* indirizzo di 0: LLLLL...
* indirizzo di 1: RRRRR...
* Indirizzo di $\frac{1}{3}$: LRRRR...
* Indirizzo $\frac{7}{9}$: RLRRRR...

>[!thm] C non è numerabile

>[!prf] 
>Assumiamo per assurdo che C sia numerabile. Quindi, possiamo associare ad ogni numero un indirizzo. Costruisco un indirizzo che non è in questa lista: è l'indirizzo che al posto i-esimo ha la negazione dell'entrata i-esima dell'elemento i-esimo della lista. (prendo la prima lista, primo elemento e nego, prendo seconda lista, secondo elemento e nego, etc.). Per costruzione, questo elemento non lo trovo nella lista di sequenze il che è un assurdo. 

Descriviamo C in come:
Prendo l'intervallo tra $[0,1]$ e al primo associo un 0, secondo 1, terzo 2. Prendo questi due intervalli, e faccio la stessa cosa. 
___
Scriviamo ogni $x \in [0,1]$ in base 3, $x = \sum_{i=1}^{\infty} \frac{a_{i}}{3^i}$ con $a_{i} = 0,1,2$ a seconda che si trovi nel primo, secondo o ultimo terzo dell'intervallo i-esimo (espansione ternaria). Quindi i punti $x\in C$ sono i punti di $[0,1]$ che possono essere scritti nell'espansione in base 3 senza che appaia 1, ad esempio $\frac{1}{3} = 0.1000 \dots = 0.022222\dots$ Non importa se ha altre rappresentazioni, basta che esiste una rappresentazione senza 1, e in questo modo avremo che $x \in C$. 
$$
\begin{align}
\frac{1}{3} = \frac{1}{3} + \frac{0}{3^2} + \frac{0}{3^3} + \dots = \frac{0}{3} + \frac{2}{3^2} + \frac{2}{3^3} = \frac{2}{9} \left( \sum_{n=0}^{\infty} \frac{1}{3^n} \right)  &  = \frac{2}{9}\left( \frac{1}{1-\frac{1}{3}} \right) \\
 & = \frac{2}{9}\frac{3}{2} = \frac{1}{3}
\end{align}
$$

___

>[!thm] C ha tanti punti quanti $[0,1]$. 

>[!prf] 
>Se $x \in C$ allora $x = \sum_{i=1}^{\infty} \frac{a_{i}}{3^i}$, con $a_{i} = 0.2$. Se sostituiamo ad ogni 2 un 1, possiamo pensare alla stringa di $a_{i}$ come all'espansione binaria di un numero qualsiasi in $[0,1]$.  Adesso la stringa $a_{i}$ è l'espansione binaria di numeri in $[0,1]$

>[!thm] C ha misura nulla
>>[!prf] 
>>La lunghezza di C è minore della lunghezza di $S_{n} \; \forall n$. Calcoliamo la lunghezza degli intervalli che abbiamo rimosso:  
>>$$
>>\frac{1}{3} + 2 \frac{1}{9} + 4 \frac{1}{27} + \dots = \frac{1}{3} \sum_n \left(\frac{2}{3} \right)^n = \frac{1}{3} \frac{1}{1-\frac{1}{3}}=1
>>$$

