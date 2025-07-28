import numpy as np
import matplotlib.pyplot as plt

def calculate_tau(rho, mu, v, L):
    """
    Calcula o parâmetro τ (Tetra) para um fluido.
    
    Args:
        rho: densidade (kg/m³)
        mu: viscosidade dinâmica (Pa·s)
        v: velocidade característica (m/s)
        L: comprimento característico (m)
    
    Returns:
        Valor de τ (adimensional)
    """
    Re = (rho * v * L) / mu  # Número de Reynolds
    tau = Re * v             # τ = Re * v
    return tau

def find_equivalent_velocity(tau_target, rho, mu, L):
    """
    Encontra a velocidade necessária para atingir um τ desejado.
    
    Args:
        tau_target: valor de τ desejado
        rho, mu, L: propriedades do fluido-alvo
    
    Returns:
        Velocidade equivalente (m/s)
    """
    return np.sqrt((tau_target * mu) / (rho * L))

# Exemplo: Fazendo água simular sangue
if __name__ == "__main__":
    # Propriedades do sangue (artéria com estenose)
    rho_blood = 1060    # kg/m³
    mu_blood = 0.003    # Pa·s
    v_blood = 0.4       # m/s
    L_blood = 0.005     # m (escala de estenose)
    
    # Calcula τ do sangue
    tau_blood = calculate_tau(rho_blood, mu_blood, v_blood, L_blood)
    print(f"τ do sangue: {tau_blood:.2f}")
    
    # Propriedades da água
    rho_water = 1000    # kg/m³
    mu_water = 0.001    # Pa·s
    L_water = 0.01      # m (tubo padrão)
    
    # Encontra velocidade da água para τ equivalente
    v_water = find_equivalent_velocity(tau_blood, rho_water, mu_water, L_water)
    print(f"Velocidade da água necessária: {v_water:.2f} m/s")
    
    # Visualização
    fluids = ['Sangue', 'Água']
    tau_values = [tau_blood, tau_blood]
    velocities = [v_blood, v_water]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    ax1.bar(fluids, tau_values, color=['#c1121f', '#48cae4'])
    ax1.set_title('Valores Equivalentes de τ')
    ax1.set_ylabel('τ')
    
    ax2.bar(fluids, velocities, color=['#c1121f', '#48cae4'])
    ax2.set_title('Velocidades Correspondentes')
    ax2.set_ylabel('Velocidade (m/s)')
    
    plt.savefig('tau_equivalence.png', dpi=300)
    plt.show()