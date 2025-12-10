"""
Simple Inventory Simulation

Provides basic inventory simulation with two scenarios:
1. Basic ordering (no lead time)
2. Ordering with lead time
"""

from dataclasses import dataclass
from typing import Optional
import pandas as pd


@dataclass
class InventoryParams:
    """Simple inventory parameters."""
    annual_demand: float = 2000.0
    days: int = 365
    lead_time: int = 0
    order_period: int = 10
    order_quantity: float = 55.0
    initial_stock: float = 55.0


class InventorySimulation:
    """Simple inventory simulation engine."""
    
    def __init__(self, params: InventoryParams):
        self.params = params
        self.daily_demand = params.annual_demand / params.days
    
    def scenario_1_basic(self) -> pd.DataFrame:
        """
        Scenario 1: Basic ordering with no lead time.
        Orders arrive immediately.
        """
        days = self.params.days
        T = self.params.order_period
        Q = self.params.order_quantity
        demand = self.daily_demand
        
        results = []
        stock = self.params.initial_stock
        
        for day in range(1, days + 1):
            # Place order every T days
            order = Q if (day > 1 and (day - 1) % T == 0) else 0
            
            # Receive order immediately (no lead time)
            receipt = order
            
            # Update stock
            stock = stock + receipt
            
            # Fulfill demand
            sales = min(stock, demand)
            stock = stock - sales
            shortage = 1 if stock < 0 else 0
            
            results.append({
                'day': day,
                'demand': demand,
                'order': order,
                'receipt': receipt,
                'stock': stock,
                'sales': sales,
                'shortage': shortage
            })
        
        return pd.DataFrame(results)
    
    def scenario_2_leadtime(self) -> pd.DataFrame:
        """
        Scenario 2: Ordering with lead time.
        Orders arrive after lead_time days.
        """
        days = self.params.days
        T = self.params.order_period
        Q = self.params.order_quantity
        LT = self.params.lead_time
        demand = self.daily_demand
        
        results = []
        stock = self.params.initial_stock
        pending_orders = []  # List of (day_to_arrive, quantity)
        
        for day in range(1, days + 1):
            # Check for arriving orders
            receipt = 0
            new_pending = []
            for arrival_day, qty in pending_orders:
                if arrival_day == day:
                    receipt += qty
                else:
                    new_pending.append((arrival_day, qty))
            pending_orders = new_pending
            
            # Place order every T days
            order = Q if (day > 1 and (day - 1) % T == 0) else 0
            if order > 0:
                pending_orders.append((day + LT, order))
            
            # Update stock
            stock = stock + receipt
            
            # Fulfill demand
            sales = min(stock, demand)
            stock = stock - sales
            shortage = 1 if stock < 0 else 0
            
            results.append({
                'day': day,
                'demand': demand,
                'order': order,
                'receipt': receipt,
                'stock': stock,
                'sales': sales,
                'shortage': shortage
            })
        
        return pd.DataFrame(results)

