import os
import openai
from tools import fact_to_string

openai.api_key = os.getenv("OPENAI_API_KEY")

def query_gpt3(QUERY):
  response = openai.Completion.create(
    model="text-davinci-002",
    prompt="Convert this data to text:\n\nE-LINK((Serve coke), (have coke), (Drink coke))\nServing coke results in having coke, which enables drinking coke.\n\nE-LINK((Serve coke), (have coke), Goal)\nServing coke results in having coke, which achieves the goal.\n\nE-LINK(Init, (have coke), (Drink coke))\nInitially having coke enables drinking coke.\n\nE-LINK(Init, (have coke), Goal)\nInitially having coke already achieves the goal.\n\nD-Link((Serve coke), (have coke), (Drink coke))\nServing coke results in having coke, which requires drinking coke.\n\nD-Link(Init, (have coke), (Drink coke))\nInitially having coke requires drinking coke.\n\nD-Link((Undergo surgery), (healthy), (Give lecture))\nUndergoing surgery results in being healthy, which requires giving lectures.\n\nD-Link((BeingAt hospital), (longHair), (Get haircut))\nBeing at the hospital results in having long hair, which requires getting a haircut.\n\nE-Link((BeingAt hospital), (not (ill)), (MakeJourney))\nBeing in the hospital results in not being ill, which enables making a journey.\n"+QUERY+"\n",
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.2,
    presence_penalty=0
  )
  
  return response["choices"][0]["text"]+" "

def verbalize_enablers(eLinks):
    loc = ""
    for e in eLinks:
        if e[0] == -1:
            loc = loc + query_gpt3("E-Link(Init, "+fact_to_string(e[2]) + ", " + e[4] + ")")
        else:
            if e[-1] == "Goal":
                loc = loc + query_gpt3("E-Link("+e[1] + ", " + fact_to_string(e[2]) + ", Goal)")
            else:  
                loc = loc + query_gpt3("E-Link("+e[1] + ", " + fact_to_string(e[2]) + ", " + e[4] + ")")
    return loc

def verbalize(Plan, dLinks, eLinks):
    """
    It is assumed that the links are already ordered in the order of verbalization.
    """
    glob = dict()
    for i in range(len(Plan)):
        loc = ""
        for d in [x for x in dLinks if x[3] == i]:
            if d[0] == -1:
                loc = loc + query_gpt3("D-Link(Init, "+fact_to_string(d[2]) + ", " + d[4] + ")")
            else:
                loc = loc + query_gpt3("D-Link("+d[1] + ", " + fact_to_string(d[2]) + ", " + d[4] + ")")
        loc = loc + verbalize_enablers([x for x in eLinks if (x[0] == i or (x[0] == -1 and x[3] == i))])
        glob["ACTION"+str(i)] = loc
    return glob