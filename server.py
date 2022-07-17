import random
import socket

from http import HTTPStatus


LOCALHOST = '127.0.0.1'
RANDOM_PORT = random.randint(10000, 20000)


my_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

address_and_port = (LOCALHOST, RANDOM_PORT)
print(f'Binding server on {LOCALHOST}:{RANDOM_PORT}')
my_socket.bind(address_and_port)
my_socket.listen()

while True:
    print('Waiting for connection...')

    conn, addr = my_socket.accept()
    data = conn.recv(1024)

    if not data or data == b'close':
        print('Got termination signal', data, 'and closed connection')
        conn.close()

    print('Received', data, 'from', addr)

    decoded_data = data.decode('utf-8')
    decoded_request_method = decoded_data.split(' /')[0]
    decoded_headers = decoded_data.split('\r\n')[1:]
    decoded_status = decoded_data.split('\r\n')[0]

    try:
        int_status = int(decoded_status.split(' ')[1].split('status=')[1])
        status = HTTPStatus(int_status)
    except (ValueError, IndexError):
        status = HTTPStatus(200)

    body = (
        f'<div>Request Method: {decoded_request_method}</div>'
        f'<div>Request Source: {address_and_port}</div>'
        f'<div>Response Status: {status.value} {status.name}</div>'
        '<br></br>'
    )

    for header in decoded_headers:
        body += f'<div>{header}</div>'

    status_line = f'HTTP/1.1 {status.value} {status.name}'
    headers = '\r\n'.join([
        status_line,
        f'Content-Length: {len(body)}',
        'Content-Type: text/html'
    ])

    response = '\r\n\r\n'.join([
        headers,
        body
    ])

    conn.send(response.encode('utf-8'))
