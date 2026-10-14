import pandas as pd

df = pd.read_csv("sales_performance_data.csv")
print(df.head(5))

region_min_revenue = df.groupby("Region")["Revenue"].min()
print(region_min_revenue)

region_max_revenue = df.groupby("Region")["Revenue"].max()
print(region_max_revenue)

region_order_count = df.groupby("Region")["Order_ID"].count()
print(region_order_count)

region_median_revenue = df.groupby("Region")["Revenue"].median()
print(region_median_revenue)

region_revenue_std = df.groupby("Region")["Revenue"].std()
print(region_revenue_std)

region_revenue_summary = df.groupby("Region")["Revenue"].agg(["sum", "mean", "max"])
print(region_revenue_summary)


region_summary = df.groupby("Region").agg({
    "Revenue" : ["sum", "mean", "max"],
    "Profit" : ["sum", "mean", "max"]
})
print(region_summary[("Profit", "sum")])

regional_report = df.groupby("Region").agg(
    Total_Revenue = ("Revenue", "sum"),
    Average_Revenue = ("Revenue", "mean"),
    Total_Profit = ("Profit", "sum"),
)
print(regional_report)

Product_Report = df.groupby("Product").agg(
    Total_Quantity = ("Quantity", "sum"),
    Total_Revenue = ("Revenue", "sum"),
    Total_Profit = ("Profit", "sum")
)
print(Product_Report)

salesperson_report = df.groupby("Salesperson").agg(
    Number_of_Orders = ("Order_ID", "count"),
    Total_Revenue = ("Revenue", "sum"),
    Average_Order_Value = ("Revenue", "mean")
)
print(salesperson_report)

top_region = regional_report["Total_Revenue"].idxmax()
top_product = Product_Report["Total_Revenue"].idxmax()
top_salesperson = salesperson_report["Total_Revenue"].idxmax()
print(top_region)
print(top_product)
print(top_salesperson)

total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()
average_order_value = df["Revenue"].mean()
print(total_revenue)
print(total_profit)
print(average_order_value)


print("Top Region (by Revenue):", top_region)
print("Top Product (by Revenue):", top_product)
print("Top Salesperson (by Revenue):", top_salesperson)
print("Total Revenue:", total_revenue)
print("Total Profit:", total_profit)
print("Average Order Value:", average_order_value)


regional_report.to_csv("regional_report.csv", index=True)
Product_Report.to_csv("product_report.csv", index=True)
salesperson_report.to_csv("salesperson_report.csv", index=True)