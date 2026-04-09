# Retail 360: Inventory Optimization via RFID & Digital Twins 🚀
### Retail Business Management | Sector: Pharmacies & Supermarkets

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.9+-green.svg)
![Industry](https://img.shields.io/badge/Industry-Retail%20%26%20Pharma-orange)
![Focus](https://img.shields.io/badge/Focus-EBITDA%20Growth-success)

## 📋 Project Overview
This project presents a strategic and technical framework to solve **"Phantom Inventory"** and **Out-of-Stock (OOS)** challenges in high-volume retail environments. 

Developed for an **MBA in Retail Business Management**, the project integrates **RFID (Radio Frequency Identification)** and **Digital Twin** technology to transition from a standard 70% inventory accuracy to a **99% precision model**. This shift directly impacts the bottom line by recovering lost sales and optimizing operational efficiency in Supermarkets and Pharmacies.

---

## 📉 The Problem: The Visibility Gap
In traditional retail (Barcode-based), the discrepancy between system records and physical shelf stock leads to:
* **Lost Sales:** Customers leave when products are missing, even if the system says they are "In Stock."
* **Shrinkage:** Lack of real-time traceability for expiration dates (critical in Pharma).
* **Operational Inertia:** Manual audits taking 8-12 hours with high human error rates.


---

## 📊 Strategic Business Analysis

### 1. SWOT Analysis (FODA)

| **Strengths (Fortalezas)** | **Weaknesses (Debilidades)** |
| :--- | :--- |
| • 99% inventory accuracy.<br>• Real-time data for SAP/ERP integration.<br>• High scalability across branches. | • High initial hardware cost (CAPEX).<br>• Tagging costs for low-margin items. |
| **Opportunities (Oportunidades)** | **Threats (Amenazas)** |
| • Omnichannel enablement (Click & Collect).<br>• Automated checkout solutions.<br>• Retail Media monetization. | • Global chip shortages (RFID supply).<br>• Resistance to process changes from staff. |

---

### 2. Financial Model: CAPEX & OPEX
A successful implementation requires balancing the initial investment against long-term operational savings.

#### **CAPEX (Capital Expenditure)**
* **Hardware:** RFID Portals (receiving docks), fixed overhead antennas, and handheld readers.
* **Infrastructure:** Server upgrades and middleware integration with existing ERP (e.g., **SAP FI/CO/MM**).
* **Software:** Digital Twin visualization platform and AI alerting engine.

#### **OPEX (Operational Expenditure)**
* **Tagging:** Unit cost of RFID tags (Source tagging vs. In-store tagging).
* **Maintenance:** Cloud subscription for data processing and hardware calibration.
* **Training:** Continuous staff education on RFID-enabled workflows.

> **Financial Conclusion:** The model projects a **Payback Period of 14-18 months** driven by a 4-8% recovery in lost sales and a 90% reduction in labor hours for inventory counting.

---

### 3. Change Management 
Technology alone does not drive ROI; people do. The transition strategy follows three pillars:

1.  **Skill Shift:** Moving floor staff from "manual counters" to "data-driven replenisher" roles using mobile alerts.
2.  **Incentive Alignment:** Linking store manager bonuses to **Inventory Accuracy** rather than just sales volume.
3.  **Phased Rollout:** Starting with high-value/high-shrinkage categories (e.g., Dermocosmetics in Pharma) to demonstrate quick wins before full-store deployment.

---

## 🧠 About the Author
**Anna E P Rausseo** *Systems Engineer | MBA in Retail Business Management* Specialized in IT processes, SAP Analytics, and Business Analysis with over 15 years of experience. Focused on digital transformation and supply chain optimization in the Southern Cone (Venezuela/Brazil/Uruguay).

---

## 📄 License
This project is licensed under the MIT License.

---

## 🛠️ Technical Solution & Python Simulator
The repository includes a Financial ROI Simulator [simulador_roi.py](https://github.com/annaeparrar/retail-rfid-optimization/blob/main/simulador_roi.py) written in Python. It models 1,000 SKUs over a 30-day period to quantify:
1. **Revenue Recovery:** Income gained by eliminating invisible out-of-stocks.
2. **EBITDA Impact:** The direct improvement in operating margin.

### Installation & Usage
```bash
# Clone the repo
git clone [https://github.com/your-user/retail-rfid-optimization.git](https://github.com/your-user/retail-rfid-optimization.git)

# Install dependencies
pip install pandas numpy matplotlib

# Run the simulator
python simulador_roi.py
