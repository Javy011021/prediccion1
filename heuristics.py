from MHPython.MH240210 import set_problem, \
                     set_default_parameters, print_parameters, set_parameters, \
                     print_solution, systematicSearch, \
                     mh_RandomSearch, mh_RandomWalk, \
                     mh_HillClimbing, mh_LocalSearch, mh_GeneticAlgorithm
                    #  mh_EvolutionStrategy,  \
                    #  execute_mh, compare_search_procedures, print_results
                    
from rain_problem import present_problem, obj_function, random_solution, heuristic_solution, \
    random_change, not_random_change, random_combination

present_problem()

set_problem(obj_function,present_problem, random_solution, heuristic_solution, 
            random_change, not_random_change,random_combination)


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
SYSTEMATIC_S_INI=  True      # Systematic search, True: From an arbitrary initial solution, False: not random solution
RUNS=1                       # Repetitions of the metaheuristics
CRITERION = 'TA'             # 'TA': Treshold accepting, 'RRT': Record-to-Record Travel
TRESHOLD = 1                 # For TA and RRT
TRIALS_BEFORE_RESTART = 50   # For Local Search, trials before restart the search
'''

parameters = {'ECHO': True, 'MAX_TRIALS': 10, 'OBJECTIVE_MAX':False, 'GENERATION_SIZE':10, 'BEST_REFERENCES':4, 'GENERATIONAL': False}
set_parameters(parameters)

print('\nExecute Random Search')
solRS = mh_RandomSearch()
print('\nSolutions obtained by Random Search')
print(solRS)

print('\n---------------------------------------------------------------------------------------------\n')
print('Execute Random Walk')
solRW = mh_RandomWalk()
print('\nSolutions obtained by Random Walk')
print(solRW)

print('\n---------------------------------------------------------------------------------------------\n')
print('Execute Hill Climbing')
solHC = mh_HillClimbing()
print('\nSolutions obtained by Hill Climbing')
print(solHC)

print('\n---------------------------------------------------------------------------------------------\n')
print('Execute Generic Algorithm')
solGA = mh_GeneticAlgorithm()
print('\nSolution obtained by Generic Algorithm')
print(solGA)

print('\n\n')
print('Compare the results of the four search procedures')
print('RS:',solRS, 'with evalution',obj_function(solRS))
print('RW:',solRW, 'with evalution',obj_function(solRW))
print('HC:',solHC, 'with evalution',obj_function(solHC))
print('GA:', solGA, 'with evalution',obj_function(solGA))