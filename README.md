# Macro-Project-2
Code for ECON8030 Project 2 - Jack Fisher, Noble Nwankwo, Caleb Loganathan

All of Questions 1 and 2 (except for the calculation of steady state kt) are analyzed by the code "Macro Project 2 Code Parts1,2,4.py".  

"Solow_Model_Simulation_Results.xslx" Contains all the initial data on gathered for India:
   -> Gross capital = "Capital"
   -> GDP = "GDP"
   -> Total labor hours = "Labor"
   -> The log of each of this variables: "Log_K", "Log_Y", "Log_L" respectively
 
 As well as variables created in the analysis
   -> The log of the Solow residual, calculated using the Cobb-Douglas production function with α = .3 = "log_A"
   -> Simulated kt = "simulated_k_t", calculated by kt+1 = s · At · kt^α + (1 − δ) · kt, where:
       -> s = .299
       -> δ = .05
       -> α = .3
       -> At = exp(log_A)
  -> Simulated Yt = "simulated_Y_t", calculated using the Cobb-Douglas production function with At = exp(log_A) and α = .3

The calculation of steady-state kt and Question 3 are analyzed in "Part-3-Code.R"

"Solow_Model_Simulation_Results_Part3Updated2.xlsx" contains all variables previously gathered and calculated, plus:
    -> Steady state kt (ktss) = "ktss"
    -> Steady state Kt (Ktss) = "Ktss"
    -> Steady state Yt (Ytss) = "Ytss"
    -> Simulated path of yt = "simulated_y_t"
    -> The Solow Residual in level (exp(logA)) = "A"

Detailed explanations on each of these variable's calculations and the code to do so is contained in "Part-3-Code.R"

Code for generating the Simulated v Actual GDP and Steady-State v Actual GDP plots are contained in "PlotCodes.R"

The code for solving the optimization problem (Part 4) is contained in lines of "Macro Project 2 Code Parts1,2,4.py"
