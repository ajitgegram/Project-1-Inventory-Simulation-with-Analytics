# Project 1: Inventory Simulation with Analytics

This project demonstrates **Inventory Simulation** with **Four Types of Analytics**.

## Overview

Simulates single-product inventory management with deterministic ordering rules and provides comprehensive analytics to understand, diagnose, predict, and optimize inventory performance.

## Features

- ✅ **Two Simulation Scenarios:**
  - Scenario 1: Basic ordering (no lead time)
  - Scenario 2: Ordering with lead time

- ✅ **Four Types of Analytics:**
  1. **Descriptive Analytics** - What happened?
  2. **Diagnostic Analytics** - Why did it happen?
  3. **Predictive Analytics** - What will happen?
  4. **Prescriptive Analytics** - What should we do?

## Project Structure

```
Project1_Inventory_Simulation_Analytics/
├── src/
│   └── inventory_analytics/
│       ├── __init__.py
│       ├── inventory_sim.py      # Simulation engine
│       └── analytics.py          # Analytics engine
├── test_inventory_analytics.py   # Test script
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Run the Test

```bash
python test_inventory_analytics.py
```

This will:
1. Run Scenario 1 (no lead time) with all 4 analytics types
2. Run Scenario 2 (with lead time) with all 4 analytics types
3. Compare the two scenarios

### Use in Your Code

```python
from inventory_analytics import InventorySimulation, InventoryParams, InventoryAnalytics

# Set up parameters
params = InventoryParams(
    annual_demand=2000.0,
    days=365,
    lead_time=5,
    order_period=10,
    order_quantity=55.0,
    initial_stock=55.0
)

# Run simulation
sim = InventorySimulation(params)
results = sim.scenario_2_leadtime()

# Apply analytics
analytics = InventoryAnalytics(results)
analytics.descriptive()    # What happened?
analytics.diagnostic()      # Why did it happen?
analytics.predictive()       # What will happen?
analytics.prescriptive()    # What should we do?
```

## Analytics Output

### 1. Descriptive Analytics
- Average, min, max stock levels
- Total demand and sales
- Shortage statistics
- Fill rate
- Order statistics

### 2. Diagnostic Analytics
- Shortage analysis (first, last, frequency)
- Order pattern analysis
- Stock level analysis
- Root cause identification

### 3. Predictive Analytics
- Stock trend analysis (autocorrelation)
- Next shortage prediction
- Trend analysis (increasing/decreasing/stable)

### 4. Prescriptive Analytics
- Recommendations for high shortage rates
- Safety stock suggestions
- Order quantity optimization
- Order frequency recommendations

## Example Output

```
============================================================
DESCRIPTIVE ANALYTICS - What Happened?
============================================================

📊 Inventory Summary:
  Average Stock: 45.23 units
  Min Stock: -10.50 units
  Max Stock: 110.00 units
  Total Demand: 2000.00 units
  Total Sales: 1990.50 units
  Days with Shortage: 15 days
  Shortage Rate: 4.11%
  Fill Rate: 99.53%
  ...
```

## Parameters

- `annual_demand`: Total yearly demand in units
- `days`: Number of days to simulate
- `lead_time`: Days until order arrives (0 for immediate)
- `order_period`: Days between orders
- `order_quantity`: Quantity per order
- `initial_stock`: Starting inventory level

## Notes

- This is a **deterministic** simulation (no randomness)
- Results are reproducible with same parameters
- Analytics work with any simulation results DataFrame

