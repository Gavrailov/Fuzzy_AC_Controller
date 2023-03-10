import numpy as np 
import skfuzzy as fuzz
from skfuzzy import control as ctrl  #pip dec

# Create the three fuzzy variables - two inputs, one output
temperature = ctrl.Antecedent(np.arange(0, 51, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 51, 1), 'humidity')
fan_speed = ctrl.Consequent(np.arange(0, 1601, 1), 'fan_speed')

# Use triangular membership function to make 9 fuzzy sets
temperature['cold'] = fuzz.trimf(temperature.universe, [0, 0, 25])
temperature['medium'] = fuzz.trimf(temperature.universe, [0, 25, 50])
temperature['hot'] = fuzz.trimf(temperature.universe, [25, 50, 50])
humidity['dry'] = fuzz.trimf(humidity.universe, [0, 0, 25])
humidity['normal'] = fuzz.trimf(humidity.universe, [0, 25, 50])
humidity['wet'] = fuzz.trimf(humidity.universe, [25, 50, 50])
fan_speed['slow'] = fuzz.trimf(fan_speed.universe, [0, 0, 800])
fan_speed['moderate'] = fuzz.trimf(fan_speed.universe, [0, 800, 1600])
fan_speed['fast'] = fuzz.trimf(fan_speed.universe, [800, 1600, 1600])
temperature.view()

# Get temperature
T = input("Input temperature\n")
H = input("Input humidity\n")

# Set rules
rule1 = ctrl.Rule(temperature['cold'] & humidity['dry'], fan_speed['moderate'])
rule2 = ctrl.Rule(temperature['cold'] & humidity['normal'], fan_speed['slow'])
rule3 = ctrl.Rule(temperature['cold'] & humidity['wet'], fan_speed['slow'])
rule4 = ctrl.Rule(temperature['medium'] & humidity['dry'], fan_speed['fast'])
rule5 = ctrl.Rule(temperature['medium'] & humidity['normal'], fan_speed['moderate'])
rule6 = ctrl.Rule(temperature['medium'] & humidity['wet'], fan_speed['slow'])
rule7 = ctrl.Rule(temperature['hot'] & humidity['dry'], fan_speed['fast'])
rule8 = ctrl.Rule(temperature['hot'] & humidity['normal'], fan_speed['fast'])
rule9 = ctrl.Rule(temperature['hot'] & humidity['wet'], fan_speed['moderate'])

# Build the fuzzy control system
fan_speed_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
speed = ctrl.ControlSystemSimulation(fan_speed_ctrl)

# Give inputs to the controller
speed.input['temperature'] = int(T)
speed.input['humidity'] = int(H)

# Compute and Print the output
speed.compute()
print(speed.output['fan_speed'], "RPM")
fan_speed.view(sim=speed)


#graph
input()     
