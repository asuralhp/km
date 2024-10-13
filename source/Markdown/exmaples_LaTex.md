
## Mathematical formula

We can use LaTeX to write mathematical equations in Markdown. To write
inline LaTeX formula use a single `$` before and after the equation and
use a double `$` to display equations.

-----

## LaTeX
The following provides a quick reference of the most commonly used LaTeX syntax. You may find a more extensive references about mathematical formulas at [LaTeX Wikibooks](https://en.wikibooks.org/wiki/LaTeX/Mathematics).

## LaTeX equations


- Inline equation: `$equation$`
- Display equation: `$$equation$$`
## Operators
 
- $x + y$
- $x - y$
- $x \times y$ 
- $x \div y$
- $\dfrac{x}{y}$
- $\sqrt{x}$

## Symbols
 
- $\pi \approx 3.14159$
- $\pm \, 0.2$
- $\dfrac{0}{1} \neq \infty$
- $0 < x < 1$
- $0 \leq x \leq 1$
- $x \geq 10$
- $\forall \, x \in (1,2)$
- $\exists \, x \notin [0,1]$
- $A \subset B$
- $A \subseteq B$
- $A \cup B$
- $A \cap B$
- $X \implies Y$
- $X \impliedby Y$
- $a \to b$
- $a \longrightarrow b$
- $a \Rightarrow b$
- $a \Longrightarrow b$
- $a \propto b$
- $\bar a$
- $\tilde a$
- $\breve a$
- $\hat a$
- $a^ \prime$
- $a^ \dagger$
- $a^ \ast$
- $a^ \star$
- $\mathcal A$
- $\mathrm a$
- $\cdots$
- $\vdots$
- $\#$
- $\$$
- $\%$
- $\&$
- $\{ \}$
- $\_$
## Space
- Horizontal space: \quad
- Large horizontal space: \qquad
- Small space: \,
- Medium space: \:
- Large space: \;
- Negative space: \!
- Greek alphabets
- Small Letter	Capital Letter	Alternative

## Greek alphabets
Small Letter | Capital Letter |	Alternative
:- | - | - 
 $\alpha$ \alpha |	$\mathrm{A}$ A	
 $\beta$ \beta |	$\mathrm{B}$ B	
 $\gamma$ \gamma |	 $\Gamma$ \Gamma	
 $\delta$ \delta |	 $\Delta$ \Delta	
 $\epsilon$ \epsilon | $\mathrm{E}$ E |	 $\varepsilon$ \varepsilon
 $\zeta$ \zeta |	$\mathrm{Z}$ Z	
 $\eta$ \eta |	$\mathrm{H}$ H	
 $\theta$ \theta |	 $\Theta$ \Theta | $\vartheta$\vartheta
 $\zeta$ \zeta |	$\mathrm{I}$ I	
 $\kappa$ \kappa |	$\mathrm{K}$ K	| $\varkappa$ \varkappa
 $\lambda$ \lambda |	 $\Lambda$ \Lambda	
 $\mu$ \mu |	 $\mathrm{M}$ M	
 $\nu$ \nu |	 $\mathrm{N}$ N	
 $\xi$ \xi |	 $\Xi$ \Xi	
 $\omicron$ \omicron |	$\mathrm{O}$ O	
 $\pi$ \pi |	 $\Pi$ \Pi	| $\varpi$ \varpi
 $\rho$ \rho |	$\mathrm{P}$ P	| $\varrho$ \varrho
 $\sigma$ \sigma |	 $\Sigma$ \Sigma	| $\varsigma$ \varsigma
 $\tau$ \tau |	$\mathrm{T}$ T	
 $\upsilon$ \upsilon |	 $\Upsilon$ \Upsilon	
 $\phi$ \phi |	 $\Phi$ \Phi | $\varphi$ \varphi
 $\chi$ \chi |	$\mathrm{X}$ X	
 $\psi$ \psi |	 $\Psi$ \Psi	
 $\omega$ \omega |	 $\Omega$ \Omega	

## Equations

$$\mathbb{N} = \{ a \in \mathbb{Z} : a > 0 \}$$

$$\forall \; x \in X \quad \exists \; y \leq \epsilon$$

$$\color{blue}{X \sim Normal \; (\mu,\sigma^2)}$$
 

$$P \left( A=2 \, \middle| \, \dfrac{A^2}{B}>4 \right)$$
 

$$f(x) = x^2 - x^\frac{1}{\pi}$$

$$f(X,n) = X_n + X_{n-1}$$

$$f(x) = \sqrt[3]{2x} + \sqrt{x-2}$$
 
 

$$\mathrm{e} = \sum_{n=0}^{\infty} \dfrac{1}{n!}$$
 

$$\prod_{i=1}^{n} x_i - 1$$
 
 

$$\lim_{x \to 0^+} \dfrac{1}{x} = \infty$$

$$\int_a^b y \: \mathrm{d}x$$

$$\log_a b = 1$$
 

$$\max(S) = \max_{i:S_i \in S} S_i$$
 

$$\dfrac{n!}{k!(n-k)!} = \binom{n}{k}$$
 

$$\text{$\dfrac{b}{a+b}=3, \:$ therefore we can set $\: a=6$}$$
Functions
 

$$
f(x)=
\begin{cases}
1/d_{ij} & \quad \text{when $d_{ij} \leq 160$}\\ 
0 & \quad \text{otherwise}
\end{cases}
$$
Matrices
 

$$
\begin{matrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{matrix}
$$
 
 
 
 
 
 
 

$$
M = 
\begin{bmatrix}
\frac{5}{6} & \frac{1}{6} & 0 \\[0.3em]
\frac{5}{6} & 0 & \frac{1}{6} \\[0.3em]
0 & \frac{5}{6} & \frac{1}{6}
\end{bmatrix}
$$
  			 

$$ 
M =
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
$$
  			 

$$ 
M =
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
$$
 

$$
A_{m,n} = 
\begin{pmatrix}
a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m,1} & a_{m,2} & \cdots & a_{m,n} 
\end{pmatrix}
$$

## Font sizes

$\Huge Hello!$
$\huge Hello!$
$\LARGE Hello!$
$\Large Hello!$
$\large Hello!$
$\normalsize Hello!$
$\small Hello!$
$\scriptsize Hello!$
$\tiny Hello!$

### Example :

$$\small \text{Font size is small, eg. $\sum{x_i = 10}$}$$