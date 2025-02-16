### Steady State kt ###
library(readxl)
Solow_Model_Simulation_Results <- read_excel("Solow_Model_Simulation_Results.xlsx")

## Calculation of steady state capital (ktss) ##

# kt+1 is given by: kt+1 = (s*At*kt^alpha)+(1-delta)*kt

# In a steady state, kt+l = kt holding all else constant

# Substituting kt for kt+1 into the first equation yields:

# kt = (s*At*kt^alpha)+(1-delta)*kt // Simplified:
# ktss = ((s*At)/delta)^(1/1-alpha)

#Plugging in values calculated/assumed in sections 1 & 2
  # s = .299
  # alpha (Capital elasticity) = .3
  # delta (Depreciation rate) = .05
  # At = Solow_Model_Simulation_Results$A
# We can now simulate the steady state kt (Capital to labor ratio)

Solow_Model_Simulation_Results$A = exp(Solow_Model_Simulation_Results$log_A)
ktss = ((.299 * Solow_Model_Simulation_Results$A)/.05)^(1/.7)
Solow_Model_Simulation_Results$ktss = ktss

#### Part 3 Question 1 ####

### Calculating path of yt ###

# Aggregate Cobb-Douglas Production Function: Yt = At*Kt^(alpha)*Lt^(1-alpha)

# Divide both sides by Lt to obtain: yt = At*kt^(alpha)

# Now we can use our simulated kt and calculated Solow residual
# to estimate the path of yt with (Solow_Model_Simulation_Results$A * Solow_Model_Simulation_Results$simulated_k_t:

yt = Solow_Model_Simulation_Results$A * (Solow_Model_Simulation_Results$Simulated_k_t)^.3
Solow_Model_Simulation_Results$simulated_y_t = yt

#### Part 3 Question 2 ####
### Calculating Steady-State Yt (Ytss) ###

#### Ytss = At * Ktss^alpha ####
  # At = Solow_Model_Simulation_Results$A
  # Ktss = ktss * Labor (steady-state capital/labor ratio * Total Labor Hours)

Solow_Model_Simulation_Results$Ktss = Solow_Model_Simulation_Results$ktss * Solow_Model_Simulation_Results$Labor

Ytss = Solow_Model_Simulation_Results$A * (Solow_Model_Simulation_Results$Ktss)^.3 * (Solow_Model_Simulation_Results$Labor)^.7
Solow_Model_Simulation_Results$Ytss = Ytss

df = data.frame(Solow_Model_Simulation_Results)

install.packages("writexl")
library(writexl)
write_xlsx(df, "Solow_Model_Simulation_Results_Part3Updated2.xlsx")

