# Example of comparison of several configurations of metaheuristics

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
from problemTSP import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination
#from problemKnapsack import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination
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

# Several configurations of metaheuristics to be compared
SEARCH_PROCEDURES = [
['HC1','mh_HillClimbing', {'MAX_TRIALS': 1000, 'RUNS':10, 'TRESHOLD':10, 'OBJECTIVE_MAX':False}],
['HC2','mh_HillClimbing', {'MAX_TRIALS': 1000, 'RUNS':10, 'TRESHOLD':10, 'OBJECTIVE_MAX':True}],
['Sy1','systematicSearch', {'MAX_TRIALS': 36288, 'RUNS':1,'OBJECTIVE_MAX':True}], #3628800
['Sy2','systematicSearch', {'MAX_TRIALS': 36288, 'RUNS':1,'OBJECTIVE_MAX':False}], #3628800
['LS1','mh_LocalSearch',  {'MAX_TRIALS': 100, 'RUNS':10, 'TRESHOLD':0, 'CRITERION':'TA'}],
['LS2','mh_LocalSearch',  {'MAX_TRIALS': 100, 'RUNS':10, 'TRESHOLD':0, 'CRITERION':'RRT'}],
['LS3','mh_LocalSearch',  {'MAX_TRIALS': 100, 'RUNS':10, 'TRESHOLD':10, 'CRITERION':'TA'}],
['LS4','mh_LocalSearch',  {'MAX_TRIALS': 100, 'RUNS':10, 'TRESHOLD':10, 'CRITERION':'RRT'}],
['Sy3','systematicSearch', {'MAX_TRIALS': 10000, 'RUNS':1}],
['Sy4','systematicSearch', {'MAX_TRIALS': 234, 'RUNS': 10, 'SYSTEMATIC_S_INI': False}],
['Sy5','systematicSearch', {'MAX_TRIALS': 234, 'RUNS': 1}],
['RS1','mh_RandomSearch', {'MAX_TRIALS': 10000}],
['RW1','mh_RandomWalk', {'MAX_TRIALS': 100}],
['HC3','mh_HillClimbing', {'MAX_TRIALS': 100}],
['LS5','mh_LocalSearch', {'MAX_TRIALS': 100}],
['ES1','mh_EvolutionStrategy', {'MAX_TRIALS': 1000, 'RUNS': 10,'GENERATION_SIZE':  100, 'BEST_REFERENCES':  50} ],
['ES2','mh_EvolutionStrategy', {'MAX_TRIALS': 1000, 'RUNS': 10,'GENERATION_SIZE':  50, 'BEST_REFERENCES':  10} ],
['GA1','mh_GeneticAlgorithm', {'MAX_TRIALS': 1000, 'GENERATION_SIZE':  100, 'BEST_REFERENCES':  50} ],
['GA2','mh_GeneticAlgorithm', {'MAX_TRIALS': 1000, 'GENERATION_SIZE':  50, 'BEST_REFERENCES':  10} ],
['LS6','mh_LocalSearch',  {'ECHO': True, 'MAX_TRIALS': 20, 'RUNS':2, \
                     'TRIALS_BEFORE_RESTART':5, 'OBJECTIVE_MAX':False}],
['LS7','mh_LocalSearch',  {'ECHO': True, 'MAX_TRIALS': 20, 'RUNS':2, \
                     'criterion': 'TA', 'TRESHOLD': 1, \
                     'TRIALS_BEFORE_RESTART':5, 'OBJECTIVE_MAX':False}],
['LS8','mh_LocalSearch',  {'ECHO': True, 'MAX_TRIALS': 20, 'RUNS':2, \
                     'criterion': 'RRT', 'TRESHOLD': 1, \
                     'TRIALS_BEFORE_RESTART':5, 'OBJECTIVE_MAX':False}]
]

# Execute the experiments and get the results
print_parameters()
print()
results = compare_search_procedures(SEARCH_PROCEDURES)
print_results(SEARCH_PROCEDURES,results)

# Print the results .. ready to statistical analysis

print('Configurations')
for i in range(len(SEARCH_PROCEDURES)):
    print(SEARCH_PROCEDURES[i],': ',SEARCH_PROCEDURES)

print('Results')
for i in range(len(results)):
    print('Configuration ',SEARCH_PROCEDURES[i][0],': ',results[i])