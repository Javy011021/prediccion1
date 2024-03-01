# Example of exploring exhaustively a TSP instance with 10 point, 3628800 solutions

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

# TSP ... 10 point, 3628800 solutions

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

# Set the parameters for a Systematic Search
# 10000 trials, minximize
parameters = {'MAX_TRIALS': 3628800, \
              'OBJECTIVE_MAX':False, 'ECHO': True,
              'SYSTEMATIC_S_INI':False} # change this to star in 0123456789
set_parameters(parameters)
print()
print('Execute Systematic Search')
solSystS = systematicSearch()
print()
print('Solutions obtained by Systematic Search')
print(solSystS)


