import pandas as pd
import numpy as np

# Define the file path
file_path = r"C:\Users\logan\Documents\Merged.xlsx"

# Load the Excel file
df = pd.read_excel(file_path, engine="openpyxl")

# Display the first few rows
#print(df.head())
#print(df.columns)
#print(df.rows)
#Setting alpha=0.3
alpha = 0.3

# Compute the Solow residual: log(At) = log(Yt) - αlog(Kt) - (1 − α)log(Lt)
df["log_Y"] = np.log(df["GDP"])
df["log_K"] = np.log(df["Capital"])
df["log_L"] = np.log(df["Labor"])

#Computing solow residual
df["log_A"] = df["log_Y"] - (alpha * df["log_K"]) - ((1 - alpha) * df["log_L"])
print(df[["log_Y", "log_K", "log_L", "log_A"]].head())

#Saving the solow residual in a new excel file
df.to_excel("Solow_Residual_Output.xlsx", index=False)

#Plotting the Solow Residual
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.plot(df["Year"], df["log_A"], marker="o", linestyle="-", color="b", label="Solow Residual (log A_t)")
plt.xlabel("Year")
plt.ylabel("log(A_t)")
plt.title("Solow Residual Over Time")
plt.legend()
plt.grid()
plt.show()

# Load the data (assuming the columns are 'Year', 'GDP', 'Capital', and 'Labor')
file_path = r"C:\Users\logan\Python\Solow_Residual_Output.xlsx"
df = pd.read_excel(file_path, engine="openpyxl")

# Define parameters
alpha = 0.3  # Capital elasticity
delta = 0.05  # Depreciation rate (assuming)
s = 0.299  # Savings rate (assuming, could be derived from national accounts)
A = df["log_A"]  # Solow residual
k0 = df["Capital"].iloc[0] / df["Labor"].iloc[0]# Initial capital per worker
k=df["Capital"]

# Time period for simulation (adjust as needed)
years = len(df)

# Initialize arrays for k_t (capital per worker) and Y_t (output)
k_t = np.zeros(years)  # Initialize capital per worker as an array of zeros
Y_t = np.zeros(years)  # Initialize output as an array of zeros
A_t = A.values

# Set the initial k_t (capital per worker)
k_t[0] = k0

# Simulate the path of capital per worker (k_t)
for t in range(1, years):
    k_t[t] = s * np.exp(A[t]) * k_t[t-1]**alpha + (1 - delta) * k_t[t-1]
    Y_t[t] = np.exp(A[t]) * k_t[t]**alpha * (df["Labor"].iloc[t])**(1-alpha)

# Add the simulated results to the DataFrame
df["Simulated_k_t"] = k_t
df["Simulated_Y_t"] = Y_t

#Loading file with simulation results
file_path = r"C:\Users\logan\Python\Solow_Model_Simulation_Results.xlsx"

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(df["Year"], df["Simulated_k_t"], label="Simulated Capital per Worker (k_t)", color="blue")
plt.xlabel("Year")
plt.ylabel("Capital per Worker (k_t)")
plt.title("Simulated Path of Capital per Worker (k_t)")
plt.legend()
plt.grid()
plt.show()

# Plot the output (Y_t)
plt.figure(figsize=(10, 5))
plt.plot(df["Year"], df["Simulated_Y_t"], label="Simulated Output (Y_t)", color="red")
plt.xlabel("Year")
plt.ylabel("Output (Y_t)")
plt.title("Simulated Output (Y_t)")
plt.legend()
plt.grid()
plt.show()

# Compare simulated output with actual GDP (Y_t)
plt.figure(figsize=(10, 5))
plt.plot(df["Year"], df["GDP"], label="Actual GDP", color="green")
plt.plot(df["Year"], df["Simulated_Y_t"], label="Simulated GDP", color="red", linestyle="--")
plt.xlabel("Year")
plt.ylabel("GDP")
plt.title("Comparison of Actual and Simulated GDP")
plt.legend()
plt.grid()
plt.show()



