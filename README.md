# τ-Turbulence: Universal Scaling Parameter

Python implementation for the τ parameter from the preprint:  
**"τ-Turbulence: A Universal Scaling Parameter for Fluid Behaviour Unification"**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)

## Theory
The τ parameter is defined as:

$$\tau = \text{Re} \cdot v = \frac{\rho v L}{\mu} \cdot v$$

When two fluids share the same τ value, they exhibit identical turbulent behavior regardless of their intrinsic properties.

## Code Examples
### Blood-Water Equivalence
```python
from tau_calculator import calculate_tau, find_equivalent_velocity

# Blood properties (stenosed artery)
tau_blood = calculate_tau(rho=1060, mu=0.003, v=0.4, L=0.005)

# Find equivalent water velocity
v_water = find_equivalent_velocity(tau_blood, rho_water=1000, mu_water=0.001, L=0.01)
print(f"Water velocity needed: {v_water:.2f} m/s")
```

### Visualization
![Fluid Comparison](fluid_comparison_3d.png)

## Applications
- Biomedical simulation
- Industrial fluid dynamics
- Climate modeling

## Preprint
Full theoretical framework:  
[Zenodo Link](https://zenodo.org/record/XXXXXX)