import matplotlib.pyplot as plot
# @title Date fields
radio_input = 0.005 # @param {type:"number"}

print(date_input)
radio_tierra = radio_input
radio_sol = 109 * radio_tierra
# Crea la figura y los ejes
fig, ax = plot.subplots(figsize=(18, 18))
sol=plot.Circle((0.5,0.5),radio_sol, color='yellow')
ax.add_patch(sol)
i = 0.5 - radio_sol
veces = 1
while veces < 110:
  tierra=plot.Circle((i,0.5),radio_tierra, color='blue')
  ax.add_patch(tierra)
  i += radio_tierra * 2
  veces += 1
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_aspect('equal')
plot.show()

