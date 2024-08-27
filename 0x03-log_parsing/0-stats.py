import re
from collections import defaultdict

# Example log entries
log_entries = [
    '32.34.224.134 - [2017-02-05 23:30:47.190577] "GET /projects/260 HTTP/1.1" 200 939',
    '42.129.219.34 - [2017-02-05 23:30:47.694304] "GET /projects/260 HTTP/1.1" 400 894',
    # Add more log entries here...
]

def parse_log_entry(log_entry):
    pattern = r'(?P<ip>\S+) - \[(?P<timestamp>.*?)\] "(?P<request>.*?)" (?P<status_code>\d+) (?P<response_size>\d+)'
    match = re.match(pattern, log_entry)
    if match:
        return match.groupdict()
    else:
        return None

def analyze_logs(log_entries):
    status_code_counts = defaultdict(int)
    for entry in log_entries:
        parsed_entry = parse_log_entry(entry)
        if parsed_entry:
            status_code = parsed_entry['status_code']
            status_code_counts[status_code] += 1
    
    return status_code_counts

# Analyze the logs
result = analyze_logs(log_entries)
for status_code, count in result.items():
    print(f'Status Code {status_code}: {count} requests')

# To handle invalid status codes, you can add extra validation
valid_status_codes = {'200', '400', '500', '404', '403', '301', '405'}
for status_code in list(result.keys()):
    if status_code not in valid_status_codes:
        print(f'Invalid status code found: {status_code}')
