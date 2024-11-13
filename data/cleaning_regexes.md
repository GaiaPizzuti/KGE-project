# List of regexes used to clean the datasets
- ".*?": "",?
- ".*?": \[\],?
- ".*?": \{[\n\s]*\},? 
- ".*?": null,?
- \{\}|".*?": \{[\n\s]*\}
- ,\n\s+\} (replace with })
- \[\n\s+,
- "licenza":.* (to remove single fields)