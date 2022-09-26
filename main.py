from tsn_analyzer import tsn_analyzer
from network_gen import *
import pulp

# Initialize an analyzer
analyzer = tsn_analyzer("networks/network_def.json")



print("Fig. 6: 2-server tandem")
# Solve ordinary TFA problem (without shapers)
optimal_delay = analyzer.solve_tfa()
if sum(optimal_delay) < np.inf:
    print(f"TFA\tdelays = {optimal_delay} ; \tTotal delay = {sum(optimal_delay)}")

# Solve TFA++ problem (with shapers)
optimal_delay_shapers = analyzer.solve_tfa_pp()
if sum(optimal_delay_shapers) < np.inf:
    print(f"TFA++\tdelays = {optimal_delay_shapers} ; \tTotal delay = {sum(optimal_delay_shapers)}")



print("-----------------------------")
print("Fig. 15: interleaved tendem network")
network_def_dir = "./networks/interleaved_tandem.json"
generate_interleaved_tandem(size=2,
                            burst=1, arr_rate=1, pkt_leng=0,
                            latency=1, ser_rate=4, capacity=4,
                            dir=network_def_dir)
analyzer = tsn_analyzer(network_def_dir)



# Solve ordinary TFA problem (without shapers)
optimal_delay = analyzer.solve_tfa()
if sum(optimal_delay) < np.inf:
    print(f"TFA\tdelays = {optimal_delay} ; \tTotal delay = {sum(optimal_delay)}")

# Solve TFA++ problem (with shapers)
optimal_delay_shapers = analyzer.solve_tfa_pp()
if sum(optimal_delay_shapers) < np.inf:
    print(f"TFA++\tdelays = {optimal_delay_shapers} ; \tTotal delay = {sum(optimal_delay_shapers)}")

# for var in analyzer.solver.variables():
#     print(var, pulp.value(var))
print("-----------------------------")
print("Fig. 25: ring network")
network_def_dir = "./networks/ring.json"
generate_ring(size=2,
              burst=1, arr_rate=1, pkt_leng=0,
              latency=1, ser_rate=4, capacity=4,
              dir=network_def_dir)
analyzer = tsn_analyzer(network_def_dir)

# Solve ordinary TFA problem (without shapers)
optimal_delay = analyzer.solve_tfa()
if sum(optimal_delay) < np.inf:
    print(f"TFA\tdelays = {optimal_delay} ; \tTotal delay = {sum(optimal_delay)}")

# Solve TFA++ problem (with shapers)
optimal_delay_shapers = analyzer.solve_tfa_pp()
if sum(optimal_delay_shapers) < np.inf:
    print(f"TFA++\tdelays = {optimal_delay_shapers} ; \tTotal delay = {sum(optimal_delay_shapers)}")

# for var in analyzer.solver.variables():
#     print(var, pulp.value(var))