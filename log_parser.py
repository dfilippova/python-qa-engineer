import argparse
import json
import os
import re

from datetime import datetime

parser = argparse.ArgumentParser(description='Process access.log')
parser.add_argument('--path', dest='path', action='store', help='Path to logs', default=os.path.expanduser('~/Develop'))
args = parser.parse_args()

file_paths = []
if os.path.isfile(args.path):
    file_paths.append(args.path)
else:
    files = os.listdir(args.path)
    for item in files:
        if item.endswith('.log'):
            file_paths.append(os.path.join(args.path, item))

for file_path in file_paths:
    report = {
        'File path': file_path,
        'Number of requests': None,
        'Number of requests by HTTP methods': {
            'GET': 0,
            'HEAD': 0,
            'POST': 0,
            'PUT': 0,
            'DELETE': 0,
            'CONNECT': 0,
            'OPTIONS': 0,
            'TRACE': 0,
            'PATCH': 0
        },
        'Top 3 IP': {},
        'Top 3 longest requests': []
    }

    all_requests = {}
    with open(file_path) as file:
        for number, line in enumerate(file):
            ip_match = re.search('(\d{1,3}\.){3}\d{1,3}', line)
            date_match = re.search(
                '\d{1,2}\/[A-Z]([a-z]){2}\/\d{4}:\d{2}:\d{2}:\d{2} \+\d{4}', line
            )
            method_match = re.search('] \"(GET|HEAD|POST|PUT|DELETE|CONNECT|OPTIONS|TRACE|PATCH)', line)
            url_match = re.search('"(GET|HEAD|POST|PUT|DELETE|CONNECT|OPTIONS|TRACE|PATCH) (\S+) +HTTP', line)
            str_duration = line.split(' ')[-1]

            if ip_match and date_match and method_match and url_match:
                ip = ip_match.group()
                date = date_match.group()
                method = method_match.group(1)
                url = url_match.group(2)
                duration = int(str_duration)

            report['Number of requests by HTTP methods'][method.upper()] += 1

            if len(report['Top 3 longest requests']) < 3:
                report['Top 3 longest requests'].append([method, url, ip, date, duration])
            else:
                fastest_request = min(
                    report['Top 3 longest requests'][0][-1],
                    report['Top 3 longest requests'][1][-1],
                    report['Top 3 longest requests'][2][-1]
                )

                if duration > int(fastest_request):
                    if report['Top 3 longest requests'][0][-1] == fastest_request:
                        report['Top 3 longest requests'].remove(report['Top 3 longest requests'][0])
                    elif report['Top 3 longest requests'][1][-1] == fastest_request:
                        report['Top 3 longest requests'].remove(report['Top 3 longest requests'][1])
                    elif report['Top 3 longest requests'][2][-1] == fastest_request:
                        report['Top 3 longest requests'].remove(report['Top 3 longest requests'][2])

                    report['Top 3 longest requests'].append([method, url, ip, date, duration])

            if ip in all_requests:
                all_requests[ip] += 1
            else:
                all_requests[ip] = 1

        sorted_keys = sorted(all_requests, key=all_requests.get, reverse=True)
        for i in range(3):
            report['Top 3 IP'][sorted_keys[i]] = all_requests[sorted_keys[i]]

        report['Number of requests'] = number + 1

    print(json.dumps(report, indent=4))

    file_name = (
        f'report_{os.path.basename(file_path).replace(".", "_")}_'
        f'{datetime.now().strftime("%d-%m-%Y-%H:%M.json")}'
    )
    with open(file=file_name, mode='w') as f:
        f.write(json.dumps(report, indent=4))
