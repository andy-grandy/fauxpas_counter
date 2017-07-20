from __future__ import print_function
import json

path = "/path/to/diagnostics_set.json" # path to diagnostics_set.json

with open(path) as data_file:
    data = json.load(data_file)

print ("Total errors: {0} \n").format(len(data["diagnostics"]))
severity = []
for i in range(0, len(data["diagnostics"])):
    severity.append(data["diagnostics"][i]["severityDescription"])

print ("severity Fatal: {0}").format(severity.count("Fatal"))
print ("severity Error: {0}").format(severity.count("Error"))
print ("severity Warning: {0}").format(severity.count("Warning"))
print ("severity Concern: {0}").format(severity.count("Concern"))
