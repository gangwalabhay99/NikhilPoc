| Resource Type | Test Case Description | Status | Time taken :clock3: |
| ------------- | --------------------- | ------ | ------------------- |
 {%- for time, type, result in zip(list_time_taken, list_resource_type, allresults) %}
| {{ type }} | {{ result["code_desc"]}} | {{ result["status"] }} {%- if result["status"]=="passed" %} {{ symbol}}     :white_check_mark: {%- else %} {{ symbol }}:negative_squared_cross_mark: {%- endif %} | {{ time }} seconds |
{%- endfor %}


 
