import json

path = "/Users/admin/jenkins/workspace/iOS-FauxPas/diagnostics_set.json" # paste your path to diagnostics_set.json

with open(path) as data_file:
    data = json.load(data_file)

print "Total errors:  %s \n" %len(data["diagnostics"])
severity = []
for i in range(0, len(data["diagnostics"])):
    severity.append(data["diagnostics"][i]["severityDescription"])

print "Severity Fatal: %s" %severity.count("Fatal")
print "Severity Error: %s" %severity.count("Error")
print "Severity Warning: %s" %severity.count("Warning")
print "Severity Concern: %s" %severity.count("Concern")
