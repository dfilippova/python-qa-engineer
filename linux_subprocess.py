import re
from datetime import datetime
from subprocess import run, PIPE

import pandas as pd

system_info = run(['ps', 'aux'], stdout=PIPE, stderr=PIPE).stdout.decode()
system_info = system_info.split('\n')

report = {
    'Пользователи системы': None,
    'Процессов запущено': None,
    'Пользовательских процессов': None,
    'Всего памяти используется': None,
    'Всего CPU используется': None,
    'Больше всего памяти использует': None,
    'Больше всего CPU использует': None
}
columns = []
values = []
users = []

for i, line in enumerate(system_info):
    if i == 0:
        columns.append(line)
        continue
    else:
        values.append(line)
        user = re.search(r'^\S+', line)
        if user is not None and user.group() not in users:
            users.append(user.group())

report['Пользователи системы'] = ', '.join(users)
report['Процессов запущено'] = len(values)

columns = re.split(r'\s+', columns[0])
values = [re.split(r'\s+', value) for value in values]

for value in values:
    if len(columns) < len(value):
        info = ''
        for item in value[len(columns) - 1:len(value)]:
            info = info + ' ' + item
            value[len(columns) - 1] = info
        values[values.index(value)] = value = value[:-(len(value) - len(columns))]
    if len(columns) <= len(value):
        values[values.index(value)][2] = float(values[values.index(value)][2])
        values[values.index(value)][3] = float(values[values.index(value)][3])

data_frame = pd.DataFrame(values, columns=columns)

user_processes = dict()
for user in users:
    user_processes[user] = len(data_frame.loc[data_frame.USER == user].iloc[:])
    str_user_processes = '\n'.join([f'{key}: {val}' for key, val in user_processes.items()])
    report['Пользовательских процессов'] = '\n' + str_user_processes

all_memory = data_frame.iloc[:, 3].values.tolist()
report['Всего памяти используется'] = str(sum(all_memory[:-1])) + ' mb'

all_cpu = data_frame.iloc[:, 2].values.tolist()
report['Всего CPU используется'] = str(sum(all_cpu[:-1])) + '%'

cpu = data_frame.sort_values(by=['%CPU'], ascending=False).values.tolist()
report['Больше всего CPU использует'] = cpu[0][10][:20]

memory = data_frame.sort_values(by=['%MEM'], ascending=False).values.tolist()
report['Больше всего памяти использует'] = memory[0][10][:20]

report = ';\n'.join([f'{key}: {val}' for key, val in report.items()])
print('Отчёт о состоянии системы:\n' + report)

file_name = datetime.now().strftime("%d-%m-%Y-%H:%M-scan.txt")
with open(file=file_name, mode='w') as f:
    f.write('Отчёт о состоянии системы:\n')
    f.write(report)
