import socket
import json


def client(host, port, requests):
    """
    connect to server at <response:port> and check its responses
        by comparing with pre-set correct answers
    :param requests: list of requests with correct answers
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((host, port))
        for request, answer in requests:
            sock.sendall(f"{request}\n".encode())
            print("Sent: {}".format(request))
            received = str(sock.recv(1024), "utf-8")
            print(f"Received: {received}, answer is "
                  f"{'CORRECT' if int(received) == answer else 'WRONG'}")
        sock.sendall("q\r\n".encode())  # close connection


def run_client():
    """
    wrapper of client for call from terminal
    """
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-hs", "--host", default="0.0.0.0", type=str,
                        help="socket address")
    parser.add_argument("-p", "--port", default=5019, type=int,
                        help="socket port")
    args = parser.parse_args()

    with open("requests.json") as f:
        requests = json.load(f)
    client(host=args.host, port=args.port, requests=requests)


if __name__ == '__main__':
    run_client()
