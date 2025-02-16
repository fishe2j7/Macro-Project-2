### Plot of Simulated GDP v Actual GDP ###

ggplot(df, aes(x = Year)) +
  geom_line(aes(y = GDP, color = "Actual GDP"), size = 1) +  # Line plot
  geom_line(aes(y = Simulated_Y_t, color = "Simulated GDP"), size = 1, linetype = "dashed") +
  labs(title = "Actual v Simulated GDP, India",
       x = "Year",
       y = "GDP ($)",
       color = "Legend") +
  theme_grey()

### Plot of Steady-State GDP v Actual GDP ###

ggplot(df, aes(x = Year)) +
  geom_line(aes(y = GDP, color = "Actual GDP"), size = 1) +  # Line plot
  geom_line(aes(y = Ytss, color = "Steady-State GDP"), size = 1, linetype = "dashed") +
  labs(title = "Actual v Steady-State GDP, India",
       x = "Year",
       y = "GDP ($)",
       color = "Legend") +
  theme_grey()




