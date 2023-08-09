| Test Case Description | Status | 
| --------------------- | ------ |
 {%- for result in allresults %}
| {{ result["code_desc"]}} | {{ result["status"] }} {%- if result["status"]=="passed" %} {{ symbol}}     :heavy_check_mark: {%- else %} {{ symbol }} :negative_squared_cross_mark: {%- endif %} |
{%- endfor %}
 