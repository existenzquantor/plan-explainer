
import os

def  verbalize(plan, d_links, e_links):
    if os.getenv("OPENAI_API_KEY"):
        from verbalization import verbalizer_gpt3
        return verbalizer_gpt3.verbalize(plan, d_links, e_links)
    else:
        from verbalization import verbalizer_standard
        return verbalizer_standard.verbalize(plan, d_links, e_links)
    
    
    


