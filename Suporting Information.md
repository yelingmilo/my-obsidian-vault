
\section{Effective Potential of a Single Particle in Rotating Modulated Optical Tweezers}

Here we derive the effective potential $U(\theta, t)$ experienced by a single colloidal particle (referred to hereafter as the particle) confined to a circular trajectory (or ring) of radius $R$ within a rotating modulated array of Gaussian laser tweezers. Due to the strong confinement to the ring, the particle's dynamics are effectively described by a single angular coordinate $\theta$, which also serves as the position variable for the potential. 

\subsection{Potential Field and Particle Weight Function}

For a dielectric \textbf{single particle}, the primary trapping mechanism in optical tweezers is the \textbf{optical gradient force}, which attracts the particle towards regions of high light intensity. Neglecting the scattering force, the particle's \textbf{optical potential energy} $U(\theta, t)$ is proportional to the \textbf{effective light intensity} $I_{\text{eff}}(\theta, t)$\cite{pesceOpticalTweezersTheory2020}.
\begin{equation}
U_{\text{eff}}(\theta, t) = -\kappa I_{\text{eff}}(\theta, t)
\end{equation}
Here, $\kappa$ is a proportionality constant related to the particle's polarizability. The effective intensity $I_{\text{eff}}(\theta, t)$ results from the convolution of the instantaneous laser intensity profile, $I(\theta, t)$, with a particle weight function, $D(\theta)$, which accounts for the particle's finite size.

{\it Rotating Laser Intensity Profile---}
The instantaneous intensity profile $I(\theta, t)$ of a single Gaussian laser tweezer, rotating at \textbf{angular velocity} $\omega$ on a ring of radius $R$, is:
\begin{equation}
I(\theta, t) = I_0 \exp\left( -\frac{R^2(\theta - \omega t)^2}{2 \mathbf{w}^2} \right) \equiv I_0 G_0(\theta - \omega t)
\end{equation}
where $I_0$ is the peak intensity and $\mathbf{w}$ is the laser beam waist radius.


{\it Particle Weight Function---}
The finite physical size of the particle necessitates that its interaction with the light field is modeled as the intensity averaged over its volume, which effectively smooths the potential. This effect is captured by a normalized \textbf{weight function} $D(\theta)$ acting as a convolution kernel.

The particle's diameter corresponds to an angular span of $\Delta\theta_{\text{particle}} = 2\pi/N$ on the ring. We assume this angular span is equivalent to the \textbf{Full Width at Half Maximum (FWHM)} of the Gaussian weight function.

The relationship between the FWHM of a Gaussian function $D(\theta) = A e^{-a\theta^2}$ and its $a$ parameter is $\text{FWHM} = 2 \sqrt{\ln(2)/a}$. Setting the FWHM equal to the particle's angular size:
\begin{equation}
\label{eq:fwhm_relation}
\Delta\theta_{\text{particle}} = \frac{2\pi}{N} = 2 \sqrt{\frac{\ln 2}{a}}
\end{equation}
Solving for the scaling factor $a$ leads to the form of the normalized Gaussian weight function:
\begin{equation}
 \begin{split}
D(\theta) = &A_D \exp\left( -\frac{N^2 \ln 2}{\pi^2} \theta^2 \right) \\ \equiv &A_D \exp\left( -a \theta^2 \right)    
 \end{split}   
\end{equation}
where the scaling factor is $a = \frac{ N^2 \ln 2}{\pi^2}$, and $A_D$ is the normalization constant defined by $\int_{-\pi}^{\pi} D(\theta) d\theta = 1$. 

Alternatively, motivated by the particle's spherical geometry, a semicircle weight function $D_S(\theta)$ can be employed. This function is defined as non-zero only across the particle's angular span, $\Delta\theta_{\text{particle}} = 2\pi/N$:
\begin{equation}
D_S(\theta) = \begin{cases} &A_S \sqrt{(\pi/N)^2 - \theta^2} , \quad |\theta| \le \pi/N \\  &\quad \quad\quad\quad\quad\quad\quad0, \quad |\theta| > \pi/N \end{cases}
\end{equation}
where $A_S$ is the corresponding normalization constant defined by $\int_{-\pi}^{\pi} D_S(\theta) d\theta = 1$.

\subsection{Effective Potential of Rotating Tweezer Arrays}

The \textbf{effective intensity} $I_{\text{eff}}(\theta, t)$ experimented by an individual particle, arising from a single optical tweezer, is defined as the normalized convolution of the incident light intensity $I(\theta, t)$ with the particle's angular weight function $D(\theta) \cite{bewerungeExperimentalCreationCharacterization2016}$:
\begin{equation}
\label{eq:I_eff_conv}
\begin{split}
I_{\text{eff}}(\theta, t) &= \left[D * I\right](\theta, t) \\
&= \int_{-\pi}^{\pi} D(\Delta \theta) G_0(\theta - \Delta \theta - \omega t) d(\Delta \theta)
\end{split}
\end{equation}
By invoking the \textbf{Poisson summation formula}, the effective intensity can be efficiently expressed as a Fourier series:
\begin{equation}
\label{eq:I_eff_series}
I_{\text{eff}}(\theta, t) = \left( I_0 \frac{w\sqrt{2\pi}}{2\pi R} \right) \sum_{k=-\infty}^{\infty} B_k C_k e^{ik(\theta - \omega t)}
\end{equation}
The characteristic attenuation factors for the Gaussian tweezer beam profile ($B_k$) and the finite particle size ($C_k$) are given, respectively. The tweezer attenuation is:
\begin{align}
\label{eq:B_k}
B_k &= \exp \left( - \frac{k^2 w^2}{2 R^2} \right)
\end{align}
For the particle size attenuation, assuming the Gaussian weight function primarily used in this work, the factor is:
\begin{align}
\label{eq:C_k_gaussian}
C_k &= \exp \left( - \frac{k^2 \pi^2}{8 N^2 \ln 2} \right)
\end{align}
(For comparison, if the alternative semicircle weight function were used, the factor would be $C_k = (2N/k\pi)J_1(k\pi/N)$ for $k \ge 1$, with $C_0=1$.)

The \textbf{effective potential} $U_s(\theta, t)$ experienced by the single particle due to the optical tweezer is directly proportional to the effective intensity, $U_s(\theta, t) = -\kappa I_{\text{eff}}(\theta, t)$. This potential can be expressed as a Fourier series:
\begin{equation}
\label{eq:U_s_final}
U_s(\theta, t) = -\kappa I_0 \frac{w\sqrt{2\pi}}{2\pi R} \sum_{k=-\infty}^{\infty} B_k C_k e^{ik(\theta - \omega t)}
\end{equation}
This potential $U_s(\theta, t)$ models the conservative potential energy of an individual particle under the influence of a single, rotating optical trap.

The total effective potential $U_{\text{tot}}(\theta, t)$ is the superposition of $M$ equally spaced traps at $\theta_j = \omega t+2\pi(j-1)/M$:
\begin{equation}
U_{\text{tot}}(\theta, t) = \sum_{j = 1}^{M} U_{s}(\theta - \theta_j, t).
\end{equation}
Substituting the single-trap potential [Eq.~(\ref{eq:U_s_final})] and applying the discrete orthogonality relation $\sum_{j=1}^{M} e^{-ik\theta_j} = M \sum_{m} \delta_{k, mM}$ filters the Fourier spectrum. This yields a compact series:
\begin{equation}
\label{eq:U_tot_final}
U_{\text{tot}}(\theta, t) = -A_0 \sum_{m = -\infty}^{\infty} B_{mM} C_{mM} e^{i mM (\theta - \omega t)},
\end{equation}
where $A_0 = M A_0^{\prime} = \kappa I_0\frac{w\sqrt{2\pi} M}{2\pi R}$ is the global potential prefactor.

As the potential is real, this expression can be simplified into the following real-valued Fourier series:
\begin{equation}
\label{eq:U_tot_cos_real}
U_{\text{tot}}(\theta, t) = -A_0 B_0 C_0 - \sum_{m = 1}^{\infty} 2 A_0 B_{mM} C_{mM} \cos(mM (\theta - \omega t))
\end{equation}
This expression is consistent with previously reported results\cite{juniperColloidalParticlesDriven2016}.

\subsection{Potential of Rotating Modulated Tweezer Arrays}

The peak intensity $I_i$ of the $i$-th individual tweezer within the array is periodically modulated based on its fixed angular position $\theta_i$, consistent with the geometric constraints of the experimental setup:
\begin{equation}
I_i = I_0 \left[1 + \varepsilon \cos (L \theta_i)\right]
\end{equation}
where $\varepsilon$ represents the modulation depth and $L$ is the modulation wave number (or angular momentum index).

By replacing the constant intensity $I_0$ in the single-tweezer Fourier expansion with the modulated $I_i$ and summing the contributions over all $M$ fixed trap positions $\theta_i$:
\begin{equation}
\label{eq:total_potential_sum}
\begin{split}
U(\theta, t) &= \sum_{i = 1}^{M} U_{s}(\theta - \theta_i, t) \\
&= -A_0^{\prime} \sum_{i = 1}^{M} \left[1 + \varepsilon \cos (L \theta_i)\right] \\
&\quad \times \sum_{k=-\infty}^{\infty} B_k C_k e^{ik(\theta - \theta_i)}
\end{split}
\end{equation}
 We then apply Euler's formula to the cosine term, $\cos(L\theta_i) = \frac{1}{2}\left(e^{iL\theta_i} + e^{-iL\theta_i}\right)$, to explicitly separate the modulation terms:
\begin{equation}
\label{eq:total_potential_expanded}
\begin{split}
U(\theta, t) &= -A_0^{\prime} \sum_{k=-\infty}^{\infty} B_k C_k e^{ik(\theta)} \\
&\quad \times \sum_{i = 1}^{M} \left[e^{-ik\theta_i} + \frac{\varepsilon}{2} \left(e^{-i(k-L)\theta_i} + e^{-i(k+L)\theta_i}\right)\right]
\end{split}
\end{equation}
Here, $\theta_i$ represents the instantaneous angular position of the $i$-th trap. The $M$ traps form a rigid pattern rotating with angular velocity $\omega$, where the traps are equally spaced such that $\theta_i \equiv \theta_i(t) = \omega t + 2\pi (i-1)/M$. Substituting the trap positions $\theta_i(t)$ into Eq. (\ref{eq:total_potential_expanded}), the total potential $U(\theta, t)$ can be expressed as:
\begin{equation}
\label{eq:potential_fourier_final}
\begin{split}
U(\theta, t) &= -A_0 \sum_{m = -\infty}^{\infty} B_{mM}C_{mM} e^{i mM (\theta - \omega t)} \\
&\quad - \frac{A_0 \varepsilon}{2} \sum_{m = -\infty}^{\infty} B_{mM+L}C_{mM+L} \\
& \qquad \times e^{i [(mM+L) \theta - mM\omega t]} \\
&\quad - \frac{A_0 \varepsilon}{2} \sum_{m = -\infty}^{\infty} B_{mM-L}C_{mM-L} \\
& \qquad \times e^{i [(mM-L) \theta - mM\omega t]}
\end{split}
\end{equation}

