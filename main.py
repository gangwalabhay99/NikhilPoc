import json
from jinja2 import Template
import os
import builtins

with open("test.json") as jsondata:
    allresults=json.load(jsondata)["profiles"][0]["controls"][0]['results']
    
list_resource_type = []
list_time_taken =[]

for result in allresults:
   
    list_resource_type.append(result["code_desc"].split('-')[0])
    list_time_taken.append(result["run_time"])


 
 #{%- for result in allresults & time in list_time_taken & type in list_resource_type %}

context = {
 'list_time_taken':list_time_taken,
 'list_resource_type':list_resource_type,
 'allresults':allresults
}

context['zip'] = builtins.zip

with open("template.md", "r") as f:
 template = Template(f.read())

 markdown = template.render(context)


 

 #with open("table.md", "w") as f:
  #f.write(markdown)

with open(os.environ["GITHUB_STEP_SUMMARY"], "w") as f:
  f.write(markdown)

