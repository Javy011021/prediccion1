# Example of using three metaheuristics with ECHO to show the step-by-step execution

# import the implementation of several search procedures
from MH240210 import set_problem, \
                     set_default_parameters, print_parameters, set_parameters, \
                     print_solution, systematicSearch, \
                     mh_RandomSearch, mh_RandomWalk, \
                     mh_HillClimbing, mh_LocalSearch, \
                     mh_EvolutionStrategy, mh_GeneticAlgorithm, \
                     execute_mh, compare_search_procedures, print_results

# ----------------------------------------------------------------------
# Import the objective function and operator from the corresponding problem
# ----------------------------------------------------------------------
#from problemTSP import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination
from problemKnapsack import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination
#from problemDifConsNumbers import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination
#from problemDifConsBinary import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination
#from problemOneMax import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination
#from problemMathFunction1 import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination
#from problemMathFunction2 import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination
#from problemMathFunction3 import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination
#from problemMathFunction4 import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination
#from problemMathFunction5 import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination
#from problemConsecutiveSorted import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination
#from problemAscendingOrder import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination
#from problemModelFineTuning1 import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination

# Suggestion: Change the imported file to change the problem!!!!!

# Set the imported aspects of the problem configuration for the metaheuristics
set_problem(objective_function,present_problem, \
            random_solution,not_random_solution, \
            random_change,not_random_change,random_combination)

# present the problem
present_problem()

'''
# ----------------------------------------------------------------------
# General configuration of the search procedures: By default
# ----------------------------------------------------------------------
OBJECTIVE_MAX   = True       # goal of the optimization, True: maximization, False: minimization
MAX_TRIALS      = 1000       # maximum number of solutions to be explored by each metaheuristic
ECHO            = False      # printing some traces of the run
GENERATION_SIZE =  10        # number of generations, for P-metaheuristics
BEST_REFERENCES =   4        # number of solutions considered in the construction of the next generation, for P-metaheuristics
GENERATIONAL    =  False     # type of replacement in P-metaheuristics, True: generational, False: SteadyState
SYSTEMATIC_S_INI=  True      # Systematic search, True: From an arbitrary initial solution, False: from random solution
RUNS=1                       # Repetitions of the metaheuristics
CRITERION = 'TA'             # 'TA': Treshold accepting, 'RRT': Record-to-Record Travel
TRESHOLD = 1                 # For TA and RRT
TRIALS_BEFORE_RESTART = 50   # For Local Search, trials before restart the search
'''

# Set the parameters for a Random Search
# 20 trials, maximize
# ECHO to show the steps of the execution
parameters = {'ECHO': True, 'MAX_TRIALS': 20, \
              'OBJECTIVE_MAX':True}
set_parameters(parameters)
print()
print('Execute Random Search')
solRS = mh_RandomSearch()
print()
print('Solutions obtained by Random Search')
print(solRS)

# Set the parameters for a Random Walk
# 20 trials, maximize
# ECHO to show the steps of the execution
parameters = {'ECHO': True, 'MAX_TRIALS': 20, \
              'OBJECTIVE_MAX':True}
set_parameters(parameters)
print()
print('Execute Random Walk')
solRW = mh_RandomWalk()
print()
print('Solutions obtained by Random Walk')
print(solRW)

# Set the parameters for a Hill Climbing
# 20 trials, maximize
# ECHO to show the steps of the execution
parameters = {'ECHO': True, 'MAX_TRIALS': 20, \
              'OBJECTIVE_MAX':True}
set_parameters(parameters)
print()
print('Execute Hill Climbing')
solHC = mh_HillClimbing()
print()
print('Solutions obtained by Hill Climbing')
print(solHC)

print()
print('Compare the results of the three search procedures')
print('RS:',solRS, 'with evalution',objective_function(solRS))
print('RW:',solRW, 'with evalution',objective_function(solRW))
print('HC:',solHC, 'with evalution',objective_function(solHC))

