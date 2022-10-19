# plan-explainer

The plan-explainer is a tool for generating task plan explanations. It takes as input a planning domain, a planning problem, and a plan that solves the planning problem. It then computes E-Links and D-Links in that plan referring to relations of enabling and demanding, respectively. From these, explanations for each action in the plan are generated.

Read about our task plan explanation approach in http://existenzquantor.info/wp-content/uploads/2022/08/RO-MAN22_CausalLinks.pdf published in the RO-MAN'22 proceedings:

F. Lindner and C. Olz, "Step-by-Step Task Plan Explanations Beyond Causal Links," 2022 31st IEEE International Conference on Robot and Human Interactive Communication (RO-MAN), 2022, pp. 45-51, doi: 10.1109/RO-MAN53752.2022.9900590.

## Installation
```
git clone https://github.com/existenzquantor/plan-explainer.git
cd plan-explainer
pip install -r requirements.txt
```

## Invoking the explainer

* ```python explainer.py [DomainName] [Plan]```
    * For [DomainName] there must exist two files in the pddl folder: 
        * [DomainName]_domain.pddl
        * [DomainName]_problem.pddl
    * [Plan] must be written as a sequence of ground actions separated by semicolons, see examples below.
* ```python explainer.py lab "(AskHumanToOpenDoor);(Move office lab);(AskHumanToCloseDoor)"```
* ```python explainer.py coke "(Serve coke);(RefillFridge coke)"```
* ```python explainer.py proxemics "(PassCloseBy);(SaySorry)"```

## Output

To make using the tool's output as easy as possible, explainer.py outputs a JSON structure, which can be easily parsed using any standard JSON library. The output structure consists of all E-Links and D-Links and of one verbalization for each action in the plan.

The verbalizations will be generated using GPT-3 in case you have set your ```OPENAI_API_KEY``` environment variable and you have the openai python package installed. If GPT-3 is not available, the verbalizations will be a mixture of natural language and relational terms for actions and facts.

### Verbalization using GPT-3 support

* ```python explainer.py coke "(Serve coke);(RefillFridge coke)"```

```json
  "VERBALIZATION": {
    "ACTION0": "Initially not being served coke requires serving coke. Initially, having coke in the fridge enables serving coke. Serving coke results in having served coke, which achieves the goal. ",
    "ACTION1": "Serving coke results in not having coke in the fridge, which requires refilling the fridge with coke. Refilling the fridge with coke results in there being coke in the fridge, which achieves the goal. "
  }
```

### Verbalization without GPT-3 support

* ```python explainer.py coke "(Serve coke);(RefillFridge coke)"```

```json
  "VERBALIZATION": {
    "ACTION0": "(not (served coke)) holds initially and requires (Serve coke).\n(inFridge coke) holds initially and enables (Serve coke).\n(Serve coke) results in (served coke), which fulfills the goal.\n",
    "ACTION1": "(Serve coke) results in (not (inFridge coke)), which requires (RefillFridge coke).\n(RefillFridge coke) results in (inFridge coke), which fulfills the goal.\n"
  }
```
