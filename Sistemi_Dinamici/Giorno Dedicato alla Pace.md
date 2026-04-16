# Teoria dei Giochi
Questo è un modo per formalizzare situazioni in cui più agenti integariscono tra di loro e prendono delle decisioni in maniera indipendente fra di loro. 

## Storia
Tanto di questa teoria è dovuta al matematico John von Neumann, che nel 1928, individua il teoria dei giochi e individua un formalisom matematico per descrivere interazioni fra agenti. In seguito, in collaborazione con Morgenstein nel 1944, ideò le prime applicazioni all'economia. Finalmente, John Nash nel 1950 da una descrizione matematica del problema con applicazioni che vanno al di là dei semplici giochi. Il concetto più importante introdotto da lui è di *equilibiro di Nash*, per la quale vince il premio nobel dell'economia. 
Di più recente, 1960, John Maynard Smith descrive la dinamica evolutiva, che si applica sia a biologia con l'evoluzione, ma anche all'economia, dove l'evoluzione è intesa come processo di apprendimento di una strategia più ottimale. La strategia non è più fissata dalle condizioni iniziali, ma gli agenti possono apprendere nuove informazioni. Getta le base del machine learning. 

## Introduzione
La formulazione della teoria dei giochi si basa sul seguente concetto:
Molte situazioni di conflitto non devono essere compese tramite categorie morali, ma sono una consequenza della struttura degli incentivi. Ovvero che gli agenti si comportano in un modo o l'altro a causa di motivazione che gli danno un guadagno se si comportano in questo modo. Secondo questa prospettiva, le situazioni di conflitto non seguono da agenti irrzionali, che si comportano in maniera irrazionale, ma da delle interazioni determinate da una strategia. 

Diamo una trattazione più matimatica. 
Consideriamo due stati (due giocatori), questi due stati hanno due strategie a disposizione:
1. A - armarsi (sviluppo economico attraverso attività belliche)
2. N -non armarsi (sviluppo economico in altri modi)
Quindi possiamo definire uno spazio delle strategie nel seguente modo
$$
\begin{gather}
S_{1} = \{ A, N\} \\
S_{2} =  \{ A, N \}
\end{gather}
$$
che coincide per entrambi i giocatori in questo caso. 

Possiamo definire il payoff come:
>[!def] Guadagno Previsto (payoff)
>Il guadagno previsto (payoff) è una funzione che alle strategie possibili associa un numero. 
>$$
> u_{i}: S_{1} \times S_{2} \rightarrow \mathbb{R} 
>$$

e ci sarà un guadagno previsto per il prmio, e il secondo giocatore 
$$
\begin{gather}
u_{1} : S_{1} \times S_{2} \rightarrow \mathbb{R} \\
u_{2}: s_{1} \times S_{2} \rightarrow \mathbb{R}
\end{gather}
$$
Possiamo creare la seguente tabela, con le stratgie del secondo giocatore in orizzontale e quella del primo in verticale

| \   | N     | A     |
| --- | ----- | ----- |
| N   | (3,3) | (1,4) |
| A   | (4,1) | (2,2) |
Quindi, se il primo giocatore decide di armarsi, e il secondo no, il primo guadagna 4, e il secondo guadagna solo 1. Il valore numerico non ha importanza, indica solo una situazione favorevole/sfavorevole. Possiamo avere le seguenti situazioni:
1. (N,N) - Situazione di pace, entrambi hanno un guadagno di 3
2. (N, A) oppure (A,N) -  uno si arma, l'altro no, uno dei giocatori ha un guadagno rispetto ad un altro
3. (A,A) - Situazione di Conflitto, porta vantaggio ad entrambi, ma è minore rispetto a quella di una situazione di pace 
4. 
Diciamo che la strategia A è dominante
>[!def] Strategia Dominante
>Una strategia si dice dominante se il giocatore, quando gioca questa strategia, ha un vantaggio rispetto ad un giocatore che decide di non seguire la strategia A. 

Per il primo giocatore, avremo che 
$$
\begin{gather}
u_{1} (A,N) = 4 > u_{1}(N,N) = 3 \\
u_{1}(A,A) = 2 > u_{1}( N, A) = 1
\end{gather}
$$
quindi il primo giocatore ha un guadagno maggiore a scegliere di armarsi indipendentemente da quello che fa il secondo. 

La stessa cosa è vero per il secondo giocatore, e quindi per entrambi i giocatori, armarsi è la scelta che da un guadagno maggiore. La scelta di giocare strategie $(A,A)$ in cui tutti i giocatori si armano è la scelta che da un guadagno maggiore rispetto a qualsiasi scelta che fa l'avversario. 

Tuttavia, il guadagno per $(A, A)$ è minore di quello per $(N,N)$. Entrambi i giocatori starebbero meglio se optassero entrambi per la pace, eppure per la struttura degli incentivi, forza entrambi di scegliere la strategia di armamenti, questo perché è la strategia migliore, indipendentemente da quello che fa l'altro giocatore. Se entrambi i giocatori si possono communicare, allora la scelta migliore sarebbe $(N,N)$. 

>[!def] Equilibrio di Nash
>Una scelta di strategie la chiamiamo equilibrio di Nash, se fissate le scelte degli altri giocatori, nessuno può aumentare il proprio guadagno cambiando startegia. 
>In termini matematici, è una strategia $s^*, \; \text{t.c.} \; u_{i}(s_{1}^*, s_{2}^*) \geq u_{i}(s_{1}, s_{2}^*) \; \; \forall s$ . 

In questo caso, la startegia di armarsi è un equilibrio di Nash. La configurazione ottimale, ha la proprietà di essere un equilibrio instabile, perché ogni giocatore ha la possibilità di aumentare il proprio guadagno, "buttando giù" l'altro giocatore. 

## Giochi Ripetuti
Adesso, guardiamo cosa succede se i giocatori hanno la possibilità di cambiare le proprie scelte. 
Supponiamo il tempo sia discreto e il gioco viene ripetuto per $t \in \mathbb{N}$. Ad ogni istanti, i stati possono scegliere una loro strategia. Ad ogni istante, i giocatori hanno un certo payoff. Introduciamo il concetto di:

>[!def] Fattore di Sconto
>Il fattore di sconto $\delta \in (0,1)$, è un numero che uso per definire il payoff del giocatore i-esimo come 
>$$
>U_{i} = \sum_{t=0}^{\infty} \delta^t u_{i}(s(t))
>$$
>dove $S \in \{ A, N\}$

Questo vuoldire che i giocatori ripetono il gioco ad ogni istante, e ad ogni istante guadagnano un payoff, ma il guadagno complessivo è pesata con un certo numero, che determina quanta importanza diamo alle scelte successive. 

Consideriamo il primo giocatore e supponiamo che entrabmi i giocatori scelgono la strategia di non armamento. Avremo che il guadagno del primo giocatore rispetto a questa strategia è
$$
 U^N = \sum_{t=0}^{\infty} \delta^t 3 = \frac{3}{1-\delta}
$$
usando il fatto che questa somma risulta essere una serie geometrica. 

Adesso supponiamo che il primo giocatore, invece di scegliere la strategia di non armarsi decide di armarsi. Avremo che, al tempo $t=0$
$$
U^{\text{deviazione}} = \delta^0 4 + \sum_{i=1}^{\infty} \delta^t 2 = 4 + \frac{\delta}{1-\delta}
$$
dove il secondo passaggio viene dal fatto che all'istante successivo, il giocatore 2 anche lui reagirrà e si arma. 

In quale delle due situazioni il suo payoff è magiore?
Vediamo che il primo giocatore ha interesse a cooperare solo quando $U^n > U^{\text{deviazione}}$, ovvero quando 
$$
\begin{align}
\frac{3}{3-\delta} \geq 4 + \frac{2\delta}{1-\delta} \implies \delta \geq \frac{1}{2}
\end{align}
$$
Questo valore $\delta$ rappresenta l'importanza che i giocatori danno al loro futuro. 
Cioè, abbiamo che quando  $\delta^{t=0}=1$, questo è un guadagno immediato. Il guadagno futuro ha peso $\delta^{t}, t \in \mathbb{N}$, in particolare 
$$
\delta = \frac{\text{peso al tempo t +1}}{\text{peso al tempo t}}
$$
Quindi, se entrambi i giocatori danno al futuro una forte importanza allora, $(N,N)$ è la strategia migliore. Se invece entrambi danno un peso più forte ad un guadagno immediato, allora si torna all'equilibrio di Nash. La condizione per la rottura della cooperazione è $\delta \geq \frac{1}{2}$, ovvero quando il costo di una rottura delle cooperazione supera il beneficio immediato. 
___
>[!def] Repplicatore
>Consideriamo n entità che hanno possibilità di repplicarsi. Ogni entità la chiamiamo specie (senso biologico oppure senso più generale). 
>Denotiamo con $P_{i}(t)$ la popolazione della specie i-esima al tempo t. 
>Quindi, assumiamo che l'evoluzione della popolazione segue una equazione differenziale del tipo:
>$$
> \frac{dP_{i}}{dt} = f_{i}(P_{i}, \dots, P_{i})P_{i}
>$$
>dove la funzione f, viene chiamato fitness. 
>Introduciamo 
>$$
> p_{i} = \frac{P_{i}}{\sum_{i=1}^{N} P_{i}}
>$$
dove p è la probabilità che un replicatore appartenga alla specie i-esima. 
>Quindi, abbiamo che
>$$
>\begin{align}
>\frac{d}{dt}p_{i}  & = \frac{1}{\left( \sum_{i=1}^{n} p_{i} \right)^{2}}\left[ \frac{dP_{i}}{dt} \sum_j P_{j} - P_{i}\sum_j \frac{dP_{j}}{dt} \right] \\
>  & = \frac{1}{\left( \sum_{i=1}^{N} P_{i} \right)^{2}} \left[ f_{i}(\vec{P})P_{i} \sum_j P_{j} - P_{i} \left( \sum_{j} f_{j}(\vec{P}) P_{j}  \right) \right] \\
>  & = f_{i}(\vec{P}) p_{i}  - p_{i} \left( \sum_{i=1}^{n} f_{j}(\vec{P}) p_{j} \right)
>\end{align}
>$$

Quindi se conosciamo la funzione che governa l'andamento della popolazione i-esima, sappaimo anche l'andamento della probabilità che il repplicatore appartiene a questo. 

Introduciamo il fitness medio
>[!def] Fitness Medio
>Il fitness medio è 
>$$
> <f(\vec{P})> = \sum_{j=1}^{n} f_{j}(\vec{P}) p_{j}
>$$

In questo modo posso riscrivere 
>[!def] Repplicatore pt. 2
>$$
>\frac{d}{dt} p_{i} = (f_{i}(\vec{P}) \;- <f(\vec{P})>) p_{i} \qquad i = 1, \dots, N
>$$

Quindi, abbiamo che la frazione di replicatori (entità che sono in grado di riprodursi), della specie i-esima aumenta quando la sua fitness è maggiore del valor medio. 

>[!def] "Divergenza"
>Date due distribuzioni di probabilità 
>$$
\begin{align}
> q = (q_{1}, \dots, q_{n}) \\
> p = (p_{1}, \dots, p_{n})
> \end{align}
> $$
> definiamo 
>$$
> I(q || p) = \sum_i q_{i} \log \frac{q_{i}}{p_{i}}
>$$
>che è la informazione di p relativa a q. 
>Questo oggetto misura l'informazione che guadagnamo quando partiamo dall'ipotesi q e invece scopriamo p. 

>[!ex] Prendiamo una moneta
>Prendiamo una moneta e assumiamo che la moneta non sia biased, quindi abbiamo che a priore
>$$
> p (\text{testa}) = \frac{1}{2} \quad p(\text{croce}) = \frac{1}{2}
>$$
>e a posteriori in realtà la moneta è truccata, quindi le probabilità in realtà sono:
>$$
> q(testa) = 1 \qquad q(croce) = 0
>$$
>Allora avremo che 
>$$
> \begin{align}
> I = 1 \cdot \log \frac{1}{\frac{1}{2}} + 0 \log\left( \frac{0}{\frac{1}{2}} \right)  = \log 2\\
> I = \frac{1}{2} \log\left( \frac{\frac{1}{2}}{1} \right) + \frac{1}{2} \log\left( \frac{\frac{1}{2}}{0} \right) = \infty
\end{align}
>$$
>dove quando si ha un $0 \log(0)$ si intende con il limite. Questa misura la quantità di informazione che troviamo supponendo che la moneta sia non truccata e scoprendo che è truccata, o viceversa, pensando che sia truccata e poi scoprendo che non lo è. 

Questa funzione "divergenza" ha varie proprietà che ci interessano: 
* $I(q||p) \geq 0$
* $I(q||p) = 0 \iff q =p$
Quindi è una distanza, per la quale non è simmetrica e non vale la disuguaglianza triangolare. 
Abbiamo che partendo dal fatto che
$$
I(q||p) \geq 0 \implies \log x \leq x-1
$$
e definito 
$$
x = \frac{p_{i}}{q_{i}} \implies \log \frac{p_{i}}{q_{i}} \leq \frac{p_{i}}{q_{i}} - 1 \implies q_{i} \log \frac{p_{i}}{q_{i}} \leq p_{i} - q_{i} \implies q_{i} \log \frac{q_{i}}{p_{i}} \geq q_{i} - p_{i}
$$
Quindi, sommando su i
$$
I(q||p) = \sum_i q_{i} \log \frac{q_{i}}{p_{i}} \geq \sum_i (q_{i} - p_{i}) = 0
$$
Assumiamo che $q$ sia indipendente dal tempo, e andiamo a vedere cosa fa 
$$
\frac{d}{dt} I(q||p) = - \sum_i \frac{\dot{p}_{i}}{p_{i}} q_{i}
$$
e usando il fatto che $\dot{p}_{i}$ è il nostro sistemo dinamico, 
$$
\begin{align}
\frac{d}{dt} I(q||p)  & = - \sum_i (f_{i}(\vec{P}) - <f(\vec{P})>)q_{i} \\ \\
 &  = -\sum_i f_{i}(\vec{P})q_{i} + \sum_i <f(\vec{P})> q_{i} \\ 
  & = -\sum_i f_{i}(\vec{P}) q_{i} + <f(\vec{P})> \underbrace{ \sum_i q_{i} }_{ =1 } \\
 & = -\sum_i f_{i}(\vec{P})q_{i} - \sum_i f_{i}(\vec{P})p_{i}
\end{align}
$$
dove si è usato la definizione di $<f>$ e il fatto che $\sum_i q_{i} = 1$ . Abbiamo quindi che 
$$
\begin{align}
\frac{d}{dt} I(q||p) &  = \sum_i f_{i}(\vec{P}) (p_{i} - q_{i}) \\
 &  = \overrightarrow{f(P(t))} \cdot (\overrightarrow{P(t)-q})
\end{align}
$$
riscrivenod con notazione vettoriale 

# Teoria dei Giochi Evolutivi
Quindi, possiamo scrivere 
$$
f_{i} (\vec{P}) = \sum_{j=1}^{n} A_{ij} p_{j} \qquad \forall i = 1, \dots, n
$$
dove $A_{ij}$ è la matrice di fitness. 
Questo si lega alla teoria dei giochi nel seguente modo:
Supponiamo di avere 2 giocatori che giocano sullo stesso insieme di strategie. Allora $A_{ij}$ è la matrice dei payoff, che mi determina il guadagno quando il primo giocatore sceglie la strategia i-esima e il secondo sceglie la strategie j-esima. 

Possiamo definire due strategie:
>[!def] Strategia Pura
>Una strategia pura la definiamo come un elemento di X, lo spazio delle strategie. 

>[!def] Strategia mista
>Una strategia mista la definiamo come una distribuzione di probabilità su X, lo spazio delle startegie. 

Quindi, i payoff del primo giocatore risulta essere 
$$
p = A q \implies 
\begin{pmatrix}
p_{1} &  \dots &  p_{n} 
\end{pmatrix}
=
\begin{pmatrix}
\dots  & \dots & \dots \\
\dots & \dots & \dots \\
\dots  & \dots & \dots
\end{pmatrix}
\begin{pmatrix}
q_{1} \\
\vdots \\
q_{n}
\end{pmatrix}
$$
Allora i replicatori, si riproducono con un tasso determinato dai loro guadagni aspetttai, con un tasso determinato dai loro payoff. Le strategie pure corrisponono alle specie $P_{i}$ mentre le strategie miste alle $p_{i}$. 

La matrice dei payoff è proprio la matrice di fitness. 
Passando in notazione vettoriale $f(\vec{P}) = A \cdot p$:
$$
\frac{d}{dt} I(q||p(t)) = (\overrightarrow{p(t)-q}) \cdot A \; p(t)
$$

>[!def] 
>Definisco q come una strategia dominante se $q \cdot Ap > p \cdot Ap \quad \forall p$. 

Se $q$ è dominante, abbiamo che 
$$
\frac{d}{dt} I(q||p(t)) \leq 0 
$$
E visto che q non dipende dal tempo, è un punto di equilibrio. 
Il guadagno previsto se io uso q e tu p: $q \cdot A p$
Se entrambi giochiamo p: $p \cdot A p$

>[!def] Stato Evolutivo Stazionario (ESS)
>Lo stato evolutivo stazionario lo definiamo come: 
>Dato una popolazione q, quando aggiungiamo una piccola popolazione di invasori, distribuita secondo p, la popolazione originaria è più fit, nel senso che 
>$$
> \begin{gather}
> q A ((1-\epsilon)q + \epsilon p) > p A((1-\epsilon)q+\epsilon p) \quad \forall p \text{ strategia mista e } \epsilon \text{ piccola}
\end{gather}
>$$
Notiamo che $(1-\epsilon) q + \epsilon p$ è la popolazione che ottengo se rimpiazzo una frazione $\epsilon$ della popolazione originaria con invasori. 

Espandiamo e troviamo che 
$$
q \cdot A q - \epsilon (q \cdot Aq - q \cdot Ap) > p \cdot Aq -\epsilon (p \cdot Aq - p \cdot Ap)
$$
Consideriamo (stato evolutivo stazionario)
* $q \cdot Aq \geq p \cdot Aq$ 
* se questo è saturato ($q \cdot Aq = p \cdot Aq$) $\implies q \cdot Ap > p \cdot Ap$
e quindi è una funzione di Liapunov, essendo che 
$$
\frac{d}{dt} I(q||p(t)) = (p(t) - q) \cdot Ap(t) > 0
$$
