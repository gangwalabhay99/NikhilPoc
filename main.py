import json
from jinja2 import Template

with open("test.json") as jsondata:
    allresults=json.load(jsondata)["profiles"][0]["controls"][0]['results']
    
#for result in allresults:
 
 #print(result["status"])
 #print(result["code_desc"])
 


with open("template.md", "r") as f:
 template = Template(f.read())

 markdown = template.render(allresults=allresults)

 print(markdown)

with open("GITHUB_STEP_SUMMARY", "w") as f:
  f.write(markdown)

