import json
import socket
from json import JSONDecodeError

from mobile_network import count_unreachable


class Server:
    """
    server for handling requests to count_unreachable()
    """
    break_set = {"", "q\r\n"}

    def __init__(self, host, port, queue_len=5):
        self.host = host
        self.port = port
        # max number of connections in listen queue
        self.queue_len = queue_len

    def run(self):
        """
        start the server
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            print(f"run server on {self.host}:{self.port}")

            server_socket.listen(self.queue_len)
            while True:
                # accept new connection
                connection, address = server_socket.accept()
                print(f"Connection from: {address} is opened")
                self._handel_connection(connection)
                print(f"Connection from: {address} is closed")

    def _handel_connection(self, connection):
        whole_request = []
        while True:
            data = connection.recv(1024).decode()
            print(f"received '{data}'")
            if data in self.break_set:
                break
            whole_request += [data]
            if "\n" in data:
                str_request = ''.join(whole_request).replace("'", '"')
                try:
                    json_data = json.loads(str_request)
                except JSONDecodeError as e:
                    message = f"incorrect input {str_request}\n{e}\n"
                    print(f"answer '{message}'", sep="")
                    connection.sendall(message.encode())
                    connection.close()
                    return
                output = count_unreachable(*json_data)
                connection.sendall(f"{output}\n".encode())
                print(f"answer '{output}'")
                whole_request = []
        connection.close()


def run_server():
    """
    wrapper of server for call from terminal
    """
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-hs", "--host", default="0.0.0.0", type=str,
                        help="socket address")
    parser.add_argument("-p", "--port", default=5019, type=int,
                        help="socket port")
    args = parser.parse_args()
    server = Server(host=args.host, port=args.port)
    server.run()


if __name__ == '__main__':
    run_server()
