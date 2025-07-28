import numpy as np
import matplotlib.pyplot as plt
from tau_calculator import calculate_tau

# Simulação de campo de velocidade em um tubo
def simulate_flow(rho, mu, v, L, tau):
    """Simula um perfil de velocidade com turbulência simplificada"""
    z = np.linspace(0, L, 100)
    r = np.linspace(-0.1, 0.1, 50)
    R, Z = np.meshgrid(r, z)
    
    # Perfil laminar + componente turbulenta proporcional a τ
    V_laminar = v * (1 - (R/0.1)**2)
    V_turbulent = 0.2 * tau * np.sin(10*Z) * np.exp(-(R/0.05)**2)
    
    return Z, R, V_laminar + V_turbulent

# Gera visualização comparativa
fig, axes = plt.subplots(1, 2, figsize=(15, 6), subplot_kw={'projection': '3d'})

# Configuração SANGUE
rho_b, mu_b, v_b, L_b = 1060, 0.003, 0.4, 0.005
tau_b = calculate_tau(rho_b, mu_b, v_b, L_b)
Z_b, R_b, V_b = simulate_flow(rho_b, mu_b, v_b, L_b, tau_b)
ax1 = axes[0]
ax1.plot_surface(Z_b, R_b, V_b, cmap='viridis', alpha=0.8)
ax1.set_title(f'Sangue: τ = {tau_b:.1f}', fontsize=14)
ax1.set_xlabel('Comprimento (m)')
ax1.set_ylabel('Raio (m)')
ax1.set_zlabel('Velocidade (m/s)')

# Configuração ÁGUA com τ equivalente
rho_w, mu_w, L_w = 1000, 0.001, 0.01
v_w = np.sqrt((tau_b * mu_w) / (rho_w * L_w))  # Mantém τ constante
Z_w, R_w, V_w = simulate_flow(rho_w, mu_w, v_w, L_w, tau_b)
ax2 = axes[1]
surf = ax2.plot_surface(Z_w, R_w, V_w, cmap='viridis', alpha=0.8)
ax2.set_title(f'Água: v = {v_w:.2f} m/s, τ = {tau_b:.1f}', fontsize=14)
ax2.set_xlabel('Comprimento (m)')
ax2.set_ylabel('Raio (m)')

plt.colorbar(surf, ax=axes, label='Velocidade (m/s)')
plt.savefig('fluid_comparison_3d.png', dpi=300)
plt.show()