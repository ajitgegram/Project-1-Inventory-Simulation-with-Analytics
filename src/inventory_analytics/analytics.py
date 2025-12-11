"""
Inventory Simulation Analytics

Provides four types of analytics for inventory simulation data:
1. Descriptive - What happened?
2. Diagnostic - Why did it happen?
3. Predictive - What will happen?
4. Prescriptive - What should we do?
"""

import pandas as pd


class InventoryAnalytics:
    """Analytics for inventory simulation data."""
    
    def __init__(self, data: pd.DataFrame):
        """
        Initialize with inventory simulation DataFrame.
        
        Expected columns: day, demand, order, receipt, stock, sales, shortage
        """
        self.df = data.copy()
    
    def descriptive(self) -> None:
        """Descriptive Analytics: What happened?"""
        print("\n" + "="*60)
        print("DESCRIPTIVE ANALYTICS - What Happened?")
        print("="*60)
        
        print("\n📊 Inventory Summary:")
        print(f"  Average Stock: {self.df['stock'].mean():.2f} units")
        print(f"  Min Stock: {self.df['stock'].min():.2f} units")
        print(f"  Max Stock: {self.df['stock'].max():.2f} units")
        print(f"  Total Demand: {self.df['demand'].sum():.2f} units")
        print(f"  Total Sales: {self.df['sales'].sum():.2f} units")
        print(f"  Days with Shortage: {(self.df['shortage'] > 0).sum()} days")
        print(f"  Shortage Rate: {(self.df['shortage'] > 0).mean():.2%}")
        
        if self.df['demand'].sum() > 0:
            fill_rate = (self.df['sales'].sum() / self.df['demand'].sum()) * 100
            print(f"  Fill Rate: {fill_rate:.2%}")
        
        print(f"  Total Orders Placed: {(self.df['order'] > 0).sum()} times")
        print(f"  Total Order Quantity: {self.df['order'].sum():.2f} units")
    
    def diagnostic(self) -> None:
        """Diagnostic Analytics: Why did it happen?"""
        print("\n" + "="*60)
        print("DIAGNOSTIC ANALYTICS - Why Did It Happen?")
        print("="*60)
        
        shortage_days = self.df[self.df['shortage'] > 0]
        
        if len(shortage_days) > 0:
            print("\n Shortage Analysis:")
            print(f"  First Shortage: Day {shortage_days['day'].iloc[0]}")
            print(f"  Last Shortage: Day {shortage_days['day'].iloc[-1]}")
            print(f"  Total Shortage Days: {len(shortage_days)}")
            print(f"  Average Stock Before Shortage: {shortage_days['stock'].mean():.2f} units")
            
            # Order pattern analysis
            print("\n Order Pattern Analysis:")
            order_days = self.df[self.df['order'] > 0]
            print(f"  Orders Placed: {len(order_days)} times")
            if len(order_days) > 1:
                intervals = order_days['day'].diff().dropna()
                avg_interval = intervals.mean()
                print(f"  Average Order Interval: {avg_interval:.1f} days")
                print(f"  Order Quantity: {self.df['order'].max():.2f} units per order")
            
            # Stock level before shortages
            print("\n Stock Level Analysis:")
            print(f"  Average Stock Level: {self.df['stock'].mean():.2f} units")
            print(f"  Stock Level on Shortage Days: {shortage_days['stock'].mean():.2f} units")
        else:
            print("\n No shortages occurred in this simulation")
            print("  → Inventory policy is working well")
    
    def predictive(self) -> None:
        """Predictive Analytics: What will happen?"""
        print("\n" + "="*60)
        print("PREDICTIVE ANALYTICS - What Will Happen?")
        print("="*60)
        
        # Stock trend analysis
        print("\n Stock Trend Analysis:")
        self.df['stock_lag1'] = self.df['stock'].shift(1)
        
        # Correlation between consecutive days
        corr_data = self.df[['stock', 'stock_lag1']].dropna()
        if len(corr_data) > 0 and corr_data['stock'].std() > 0:
            correlation = corr_data.corr().iloc[0, 1]
            print(f"  Stock Autocorrelation (Day t vs Day t-1): {correlation:.3f}")
            
            if correlation > 0.7:
                print("  → Strong positive trend: Stock levels are stable")
            elif correlation < 0.3:
                print("  → Weak correlation: Stock levels are volatile")
            else:
                print("  → Moderate correlation: Stock levels show some stability")
        
        # Predict next shortage
        shortage_days = self.df[self.df['shortage'] > 0]['day'].tolist()
        if len(shortage_days) >= 2:
            intervals = [shortage_days[i+1] - shortage_days[i] 
                        for i in range(len(shortage_days)-1)]
            avg_interval = sum(intervals) / len(intervals)
            last_shortage = shortage_days[-1]
            predicted_next = int(last_shortage + avg_interval)
            print(f"\n Predicted Next Shortage: Around Day {predicted_next}")
            print(f"  Based on average interval of {avg_interval:.1f} days")
        elif len(shortage_days) == 1:
            print(f"\n Only one shortage occurred on Day {shortage_days[0]}")
            print("  → Insufficient data for prediction")
        else:
            print("\n No shortages occurred")
            print("  → Current policy should prevent future shortages")
        
        # Trend analysis: first half vs second half
        mid_point = len(self.df) // 2
        first_half_shortages = self.df.iloc[:mid_point]['shortage'].sum()
        second_half_shortages = self.df.iloc[mid_point:]['shortage'].sum()
        
        if second_half_shortages > first_half_shortages * 1.2:
            print(f"\n Trend: Shortages increasing ({first_half_shortages} → {second_half_shortages})")
            print("  → Action needed to prevent worsening situation")
        elif first_half_shortages > second_half_shortages * 1.2:
            print(f"\n Trend: Shortages decreasing ({first_half_shortages} → {second_half_shortages})")
            print("  → Situation is improving")
        else:
            print(f"\n Trend: Shortage pattern is stable")
    
    def prescriptive(self, threshold: float = 0.05) -> None:
        """Prescriptive Analytics: What should we do?"""
        print("\n" + "="*60)
        print("PRESCRIPTIVE ANALYTICS - What Should We Do?")
        print("="*60)
        
        shortage_rate = (self.df['shortage'] > 0).mean()
        avg_stock = self.df['stock'].mean()
        avg_demand = self.df['demand'].mean()
        
        print("\n Recommendations:")
        
        if shortage_rate > threshold:
            print(f"  High shortage rate ({shortage_rate:.2%}) detected!")
            print(f"  Current average stock: {avg_stock:.2f} units")
            print(f"  Average daily demand: {avg_demand:.2f} units")
            
            # Calculate recommendations
            recommended_safety_stock = avg_demand * 3  # 3 days of demand
            current_order_qty = self.df[self.df['order'] > 0]['order'].max()
            if pd.isna(current_order_qty):
                current_order_qty = 0
            
            print(f"\n  → Increase safety stock to at least {recommended_safety_stock:.0f} units")
            print(f"    (Currently averaging {avg_stock:.0f} units)")
            
            if current_order_qty > 0:
                recommended_order_qty = current_order_qty * 1.2
                print(f"  → Increase order quantity from {current_order_qty:.0f} to {recommended_order_qty:.0f} units (20% increase)")
            
            # Check order frequency
            order_days = self.df[self.df['order'] > 0]
            if len(order_days) > 1:
                avg_order_interval = order_days['day'].diff().mean()
                if avg_order_interval > 15:
                    print(f"  → Consider ordering more frequently (currently every {avg_order_interval:.0f} days)")
                elif avg_order_interval < 5:
                    print(f"  → Consider ordering less frequently (currently every {avg_order_interval:.0f} days)")
        else:
            print(f"  ✓ Shortage rate ({shortage_rate:.2%}) is acceptable")
            print(f"  Current average stock: {avg_stock:.2f} units")
            print("  → Current inventory policy appears adequate")
            print("  → Monitor performance and adjust if demand patterns change")

