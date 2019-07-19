import wmoc

# open an example network and creat a transient model
inp_file = 'examples/networks/Tnet1.inp'
tm = wmoc.network.TransientModel(inp_file)
# set wavespeed
tm.set_wavespeed(1200.)

# add leak
# t0 = 0. # add the leak at 0s
# leak_node = '1'
# emitter_coeff = 0.1 #[ m^3/s/(m H20)^(1/2)]
# tm.add_leak('1', emitter_coeff)

# Initialize
t0 = 0. # initialize the simulation at 0s
dt = 0.05  # time step [s]
tf = 20 # simulation peroid [s]
tm = wmoc.simulation.Initializer(tm, t0, dt, tf)

# # set valve operation
tc = 2 # valve closure peroid
ts = 0 # valve closure start time
se = 0 # end open percentage
m = 1 # closure constant
valve_op = [tc,ts,se,m]
tm.valve_closure('9',valve_op)

# set pump operation
# tc = 2 # pump closure peroid
# ts = 0 # pump closure start time
# se = 0.001 # end open percentage
# m = 1 # closure constant
# pump_op = [tc,ts,se,m]
# tm.pump_shut_off('1', pump_op)

# add burst
# ts = 1 # burst start time
# tc = 1 # time for burst to fully develop
# final_burst_coeff = 0.01 # final burst coeff [ m^3/s/(m H20)^(1/2)]
# tm.add_burst('3', ts, tc, final_burst_coeff)

# Transient simulation
tm = wmoc.simulation.MOCSimulator(tm)

import matplotlib.pyplot as plt
pipe = '0'
pipe = tm.get_link(pipe)
plt.plot(tm.simulation_timestamps,pipe.start_node_head,label='Start Node')
plt.plot(tm.simulation_timestamps,pipe.end_node_head,label='End Node')
plt.xlim([tm.simulation_timestamps[0],tm.simulation_timestamps[-1]])
plt.title('Pressure Head of Pipe %s '%pipe)
plt.xlabel("Time")
plt.ylabel("Pressure Head (m)")
plt.legend(loc='best')
plt.grid(True)
plt.show()