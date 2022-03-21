# plan-explainer

The plan-explainer is a tool for generating task plan explanations. It takes as input a planning domain, a planning problem, and a plan that solves the planning problem. It then computes E-Links and D-Links in that plan referring to relations of enabling and demanding, respectively. From these, explanations for each action in the plan are generated.

## Invoking the explainer

* python explainer.py [DomainName] [Plan]
    * For [DomainName] there must exist two files in the pddl folder: DomainName_domain.pddl and DomainName_problem.pddl. 
* python explainer.py lab "(AskHumanToOpenDoor);(Move office lab);(AskHumanToCloseDoor)"
* python explainer.py coke "(Serve coke);(RefillFridge coke)" 
* python explainer.py proxemics "(PassCloseBy);(SaySorry)" 

## Output

To make using the tool's output as easy as possible, explainer.py outputs a JSON structure, which can be easily parsed using any standard JSON library. The output structure consists of all E-Links and D-Links and of one verbalization for each action in the plan.

## Note
Because of a bug in the PDDL parser, currently only positive goal facts are allowed.