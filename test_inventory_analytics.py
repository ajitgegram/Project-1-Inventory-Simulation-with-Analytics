"""
Test Inventory Simulation Analytics

This script tests all four types of analytics for inventory simulation:
1. Descriptive Analytics
2. Diagnostic Analytics
3. Predictive Analytics
4. Prescriptive Analytics
"""

import sys
import os

# Add src to path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from inventory_analytics import InventorySimulation, InventoryParams, InventoryAnalytics


def test_analytics():
    """Test all four analytics types with inventory simulation."""
    
    print("="*70)
    print("INVENTORY SIMULATION ANALYTICS TEST")
    print("="*70)
    
    # Test Scenario 1: Basic Ordering (No Lead Time)
    print("\n" + "="*70)
    print("SCENARIO 1: BASIC ORDERING (NO LEAD TIME)")
    print("="*70)
    
    params1 = InventoryParams(
        annual_demand=2000.0,
        days=365,
        lead_time=0,
        order_period=10,
        order_quantity=55.0,
        initial_stock=55.0
    )
    
    sim1 = InventorySimulation(params1)
    results1 = sim1.scenario_1_basic()
    
    print(f"\n⚙️  Simulation Parameters:")
    print(f"  - Annual Demand: {params1.annual_demand} units")
    print(f"  - Days: {params1.days}")
    print(f"  - Lead Time: {params1.lead_time} days")
    print(f"  - Order Period: {params1.order_period} days")
    print(f"  - Order Quantity: {params1.order_quantity} units")
    print(f"  - Initial Stock: {params1.initial_stock} units")
    
    # Apply Analytics
    print("\n📈 Applying Analytics...")
    analytics1 = InventoryAnalytics(results1)
    
    # 1. Descriptive Analytics
    analytics1.descriptive()
    
    # 2. Diagnostic Analytics
    analytics1.diagnostic()
    
    # 3. Predictive Analytics
    analytics1.predictive()
    
    # 4. Prescriptive Analytics
    analytics1.prescriptive(threshold=0.05)
    
    # Test Scenario 2: Ordering with Lead Time
    print("\n\n" + "="*70)
    print("SCENARIO 2: ORDERING WITH LEAD TIME")
    print("="*70)
    
    params2 = InventoryParams(
        annual_demand=2000.0,
        days=365,
        lead_time=5,  # 5 days lead time
        order_period=10,
        order_quantity=55.0,
        initial_stock=55.0
    )
    
    sim2 = InventorySimulation(params2)
    results2 = sim2.scenario_2_leadtime()
    
    print(f"\n⚙️  Simulation Parameters:")
    print(f"  - Annual Demand: {params2.annual_demand} units")
    print(f"  - Days: {params2.days}")
    print(f"  - Lead Time: {params2.lead_time} days")
    print(f"  - Order Period: {params2.order_period} days")
    print(f"  - Order Quantity: {params2.order_quantity} units")
    print(f"  - Initial Stock: {params2.initial_stock} units")
    
    # Apply Analytics
    print("\n📈 Applying Analytics...")
    analytics2 = InventoryAnalytics(results2)
    
    # 1. Descriptive Analytics
    analytics2.descriptive()
    
    # 2. Diagnostic Analytics
    analytics2.diagnostic()
    
    # 3. Predictive Analytics
    analytics2.predictive()
    
    # 4. Prescriptive Analytics
    analytics2.prescriptive(threshold=0.05)
    
    # Comparison
    print("\n\n" + "="*70)
    print("COMPARISON: SCENARIO 1 vs SCENARIO 2")
    print("="*70)
    
    print("\n📊 Key Differences:")
    print(f"  Scenario 1 (No Lead Time):")
    print(f"    - Shortage Days: {(results1['shortage'] > 0).sum()}")
    print(f"    - Average Stock: {results1['stock'].mean():.2f} units")
    print(f"    - Fill Rate: {(results1['sales'].sum() / results1['demand'].sum()):.2%}")
    
    print(f"\n  Scenario 2 (5-Day Lead Time):")
    print(f"    - Shortage Days: {(results2['shortage'] > 0).sum()}")
    print(f"    - Average Stock: {results2['stock'].mean():.2f} units")
    print(f"    - Fill Rate: {(results2['sales'].sum() / results2['demand'].sum()):.2%}")
    
    print("\n" + "="*70)
    print("✓ All analytics tests completed successfully!")
    print("="*70)


if __name__ == "__main__":
    test_analytics()

