from collections import defaultdict


messages = defaultdict(lambda: "N/A")
messages['error'] = 'Full Error Text'
messages['other']


used_default= [k for k in messages if messages[k] == "N/A"]
