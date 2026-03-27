# 控制单个光阱强度进行周期调制下的推导

## 路径一：先卷积后调制

### 单个光阱 + 卷积


单个高斯光阱（中心在$\theta=0$）
$$G_0(θ)=exp(−R²θ²/(2ω²))$$
其傅里叶级数为（周期 $2\pi$ 延拓）：

$$G_0(\theta) = \frac{\sqrt{2\pi}\,\omega}{2\pi R}\sum_{k=-\infty}^{\infty} \exp\!\left(-\frac{k^{2}\omega^{2}}{2R^{2}}\right)e^{ik\theta} = \frac{\sqrt{2\pi}\,\omega}{2\pi R}\left[1+2\sum_{k=1}^{\infty}B_k\cos(k\theta)\right], \quad B_k=\exp\!\left(-\frac{k^{2}\omega^{2}}{2R^{2}}\right).$$
粒子权重函数（高斯型）：
$$D(\theta) = \exp\left(-\frac{N^2 2\ln 2}{\pi^2} \theta^2\right), \quad A_D = \int_{-\pi}^{\pi} D(\theta) d\theta = \frac{\pi^{3/2}}{N \sqrt{2\ln 2}}$$

有效的单个光阱光强为卷积：

$$G(\theta) = \frac{1}{A_D} [D * G_0](\theta) = \frac{1}{A_D} \int_{-\pi}^{\pi} D(\Delta\theta) G_0(\theta + \Delta\theta) d(\Delta\theta)$$

带入计算可以得到（参考附录一）有效的单个光阱光强的傅里叶级数：
$$G(\theta) = \frac{\sqrt{2\pi} \omega}{2\pi R} \sum_{k=-\infty}^{\infty} B_k C_k e^{ik\theta}$$

其中 $C_k = \exp\left(-\frac{k^2 \pi^2}{8 N^2 \ln 2}\right)$

### 光阱阵列 + 调制

将有效单阱光强带入半径为 $R$ 的环上的等间距光阱阵列中，第 $i$ 束光中心在 $\theta_i = \frac{2\pi(i-1)}{M}$，并加上调制：

$$I_D(\theta) = \sum_{i=1}^{M} I_0 [1 + \varepsilon \cos(L \theta_i)] G(\theta - \theta_i)$$

利用泊松求和公式计算（参考附录二）可以得到：

$$I_D(\theta) = A_0 \left\{1 + \varepsilon B_L C_L \cos(L\theta) + \sum_{m=1}^{\infty} 2 B_{mM} C_{mM} \cos(mM\theta) + \varepsilon B_{mM \pm L} C_{mM \pm L} \cos((mM \pm L)\theta)\right\}$$
其中 $A_0 = I_0 \frac{\sqrt{2\pi} \omega M}{2\pi R}$

## 路径二：先调制后卷积

### 总光强：

$$I_{\text{tot}}(\theta) = \sum_{i=1}^{M} I_i(\theta) = \sum_{i=1}^{M} I_0 [1 + \varepsilon \cos(L \theta_i)] \exp\left(-\frac{R^2 (\theta - \theta_i)^2}{2 \omega^2}\right)$$

利用泊松求和公式（参考附录三）可以得到调制后总光强的傅里叶级数：

$$I_{\text{tot}}(\theta) = A_0 \sum_{m=-\infty}^{\infty} \left[B_{mM} + \frac{\varepsilon}{2} (B_{mM - L} + B_{mM + L})\right] e^{imM\theta}$$

### 对总光强做粒子卷积（参考附录四）：

得到下面表达式：
$$I_D(\theta) = A_0 \left\{1 + \varepsilon B_L C_L \cos(L\theta) + \sum_{m=1}^{\infty} 2 B_{mM} C_{mM} \cos(mM\theta) + \varepsilon B_{mM \pm L} C_{mM \pm L} \cos((mM \pm L)\theta)\right\}$$
其结果与路径一相同，表明两种路径结果一致。

## 胶体团簇在调制势场中的动力学方程

### 1 有效总光强
已知光阱阵列的有效总光强为

$$
I_D(\theta)=A_0\Bigl\{1+\varepsilon B_L C_L\cos(L\theta)
+\sum_{m=1}^{\infty}\bigl[2B_{mM}C_{mM}\cos(mM\theta)
+\varepsilon B_{mM\pm L}C_{mM\pm L}\cos\!\bigl((mM\pm L)\theta\bigr)\bigr]\Bigr\}.
$$

### 2 单粒子势场
势场与有效总光强成正比：

$$
U(\theta)=\kappa I_D(\theta).
$$

### 3 胶体团簇总势场
团簇含 $N$ 个粒子，角位置依次为
$\theta_i=\theta+\dfrac{2\pi i}{N},\ i=0,\dots ,N-1$。
总势场为

$$
U_{\text{total}}(\theta)=\sum_{i=0}^{N-1}U(\theta_i)
=\kappa\sum_{i=0}^{N-1}I_D\!\left(\theta+\frac{2\pi i}{N}\right).
$$

利用恒等式

$$
\sum_{i=0}^{N-1}\cos\!\left[k\left(\theta+\frac{2\pi i}{N}\right)\right]
=N\cos(k\theta)\cdot\delta_k,
$$

其中

$$
\delta_k=\begin{cases}
1,& k\ \text{是}\ N\ \text{的整数倍}\\[2mm]
0,& \text{其它}
\end{cases}
$$

得到

$$
\begin{aligned}
U_{\text{total}}(\theta)=\kappa A_0 N\Bigl\{
&1
+\varepsilon B_L C_L\cos(L\theta)\,\delta_L\\[4pt]
&+\sum_{m=1}^{\infty}\bigl[
2B_{mM}C_{mM}\cos(mM\theta)\,\delta_{mM}\\[4pt]
&\quad+\varepsilon B_{mM+L}C_{mM+L}\cos\!\bigl((mM+L)\theta\bigr)\,\delta_{mM+L}\\[4pt]
&\quad+\varepsilon B_{mM-L}C_{mM-L}\cos\!\bigl((mM-L)\theta\bigr)\,\delta_{mM-L}
\bigr]\Bigr\}.
\end{aligned}
$$

### 4 过阻尼朗之万方程
忽略热涨落，团簇动力学方程为

$$
\gamma\dot{\theta}=-\frac{\partial U_{\text{total}}(\theta)}{\partial \theta}.
$$

求导后整理得

$$
\boxed{
\begin{aligned}
\gamma\dot{\theta}=\kappa A_0 N\Bigl\{
&\varepsilon B_L C_L L\sin(L\theta)\,\delta_L\\[4pt]
&+\sum_{m=1}^{\infty}\bigl[
2B_{mM}C_{mM}(mM)\sin(mM\theta)\,\delta_{mM}\\[4pt]
&\quad+\varepsilon B_{mM+L}C_{mM+L}(mM+L)\sin\!\bigl((mM+L)\theta\bigr)\,\delta_{mM+L}\\[4pt]
&\quad+\varepsilon B_{mM-L}C_{mM-L}(mM-L)\sin\!\bigl((mM-L)\theta\bigr)\,\delta_{mM-L}
\bigr]\Bigr\}.
\end{aligned}
}
$$
