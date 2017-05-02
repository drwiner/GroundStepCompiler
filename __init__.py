import sys
from Planner import PlanSpacePlanner
from Planner import topoSort
from PlanElementGraph import Action
from Ground import GLib


if __name__ ==  '__main__':
	num_args = len(sys.argv)
	if num_args >1:
		domain_file = sys.argv[1]
		if num_args > 2:
			problem_file = sys.argv[2]
	else:
		domain_file = 'domains/travel_domain.pddl'
		problem_file = 'domains/travel-to-la.pddl'

	GL = GLib(domain_file, problem_file)
	# planner = PlanSpacePlanner(GL)
	#
	# results = planner.POCL(1)
	#
	# for result in results:
	# 	totOrdering = topoSort(result)
	# 	print('\n\n\n')
	# 	for step in topoSort(result):
	# 		print(Action.subgraph(result, step))
	# 	#print(result)