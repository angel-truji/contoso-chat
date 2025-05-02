## Load environment variables
from dotenv import load_dotenv
load_dotenv()

import json
import prompty
# to use the azure invoker make 
# sure to install prompty like this:
# pip install prompty[azure]
import prompty.azure
from prompty.tracer import trace, Tracer, console_tracer, PromptyTracer

# add console and json tracer:
# this only has to be done once
# at application startup
Tracer.add("console", console_tracer)
json_tracer = PromptyTracer()
Tracer.add("PromptyTracer", json_tracer.tracer)

# if your prompty file uses environment variables make
# sure they are loaded properly for correct execution

@trace
def run(    
) -> str:

  # execute the prompty file
  result = prompty.execute(
    "chat-3.prompty", 
    inputs={
    }
  )

  return result

if __name__ == "__main__":
   json_input = '''null'''
   args = json.loads(json_input) or {}  # <-- esta linha é a chave

   result = run(**args)
   print(result)

