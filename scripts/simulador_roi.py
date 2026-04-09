import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =================================================================
# PROJECT: Retail 360 - Inventory ROI Simulator
# MBA: Business Management (Retail & Pharma)
# Author: Anna (Systems Engineer)
# =================================================================

def run_simulation():
    # 1. Configuration & Simulation Parameters
    np.random.seed(42)
    num_skus = 1000  # Simulamos 1000 productos (ej. una farmacia promedio)
    days = 30         # Periodo de análisis: 1 mes
    
    # Parámetros de Negocio
    precision_traditional = 0.70  # 70% de exactitud (Código de barras)
    precision_rfid = 0.99         # 99% de exactitud (RFID)
    avg_margin = 0.35             # Margen del 35% (Promedio Farma/Varejo)
    rfid_tag_cost = 0.05          # Costo por etiqueta en USD
    
    # 2. Generating Synthetic Data
    data = {
        'SKU_ID': [f'SKU-{i:04d}' for i in range(num_skus)],
        'Price': np.random.uniform(10, 100, num_skus),
        'Daily_Demand': np.random.poisson(15, num_skus),
        'Physical_Stock': np.random.randint(20, 150, num_skus)
    }
    
    df = pd.DataFrame(data)
    
    # 3. Modeling "Phantom Inventory" (Stock Fantasma)
    # En el sistema tradicional, el sistema cree que tiene más de lo que hay físicamente
    df['System_Stock_Traditional'] = (df['Physical_Stock'] * np.random.uniform(0.85, 1.25, num_skus)).astype(int)
    
    # Con RFID, el sistema es idéntico a la realidad física (99% precisión)
    df['System_Stock_RFID'] = df['Physical_Stock']
    
    # 4. Calculating Lost Sales (Out-of-Stock Invisible)
    # Se pierde venta si: Demanda > Stock Físico PERO el Sistema dice que SÍ hay (por eso no se repone)
    df['Units_Lost_Traditional'] = np.where(
        (df['Daily_Demand'] > df['Physical_Stock']) & (df['System_Stock_Traditional'] > 0),
        df['Daily_Demand'] - df['Physical_Stock'],
        0
    )
    
    # Con RFID, el quiebre es visible y se activa la reposición proactiva (reducción del 95% de error)
    df['Units_Lost_RFID'] = df['Units_Lost_Traditional'] * (1 - precision_rfid)
    
    # 5. Financial Impact Analysis (Monthly)
    df['Revenue_Loss_Traditional'] = df['Units_Lost_Traditional'] * df['Price'] * days
    df['Revenue_Loss_RFID'] = df['Units_Lost_RFID'] * df['Price'] * days
    
    total_loss_trad = df['Revenue_Loss_Traditional'].sum()
    total_loss_rfid = df['Revenue_Loss_RFID'].sum()
    recovered_revenue = total_loss_trad - total_loss_rfid
    ebitda_gain = recovered_revenue * avg_margin
    
    # 6. Printing Executive Summary
    print("-" * 50)
    print("RETAIL 360 - EXECUTIVE ROI SUMMARY")
    print("-" * 50)
    print(f"Total Products Simulated:      {num_skus}")
    print(f"Traditional Revenue Loss:      ${total_loss_trad:,.2f}")
    print(f"RFID Revenue Loss:             ${total_loss_rfid:,.2f}")
    print(f"RECOVERED REVENUE (Monthly):   ${recovered_revenue:,.2f}")
    print(f"ESTIMATED EBITDA GAIN:         ${ebitda_gain:,.2f}")
    print("-" * 50)
    
    # 7. Visualization
    create_plots(total_loss_trad, total_loss_rfid, ebitda_gain)

def create_plots(loss_trad, loss_rfid, gain):
    plt.style.use('ggplot')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot 1: Revenue Loss Comparison
    scenarios = ['Traditional (70%)', 'RFID (99%)']
    losses = [loss_trad, loss_rfid]
    ax1.bar(scenarios, losses, color=['#e74c3c', '#2ecc71'])
    ax1.set_title('Monthly Revenue Loss (Out-of-Stock)', fontsize=14, fontweight='bold')
    ax1.set_ylabel('USD Amount')
    
    # Plot 2: Monthly EBITDA Impact
    ax2.text(0.5, 0.6, f'${gain:,.2f}', fontsize=40, color='#27ae60', 
             ha='center', fontweight='bold')
    ax2.text(0.5, 0.4, 'Potential Monthly\nEBITDA Improvement',
