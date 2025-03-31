import socket

import docker
import requests
from requests.adapters import HTTPAdapter, Retry

from lib import utils

client = docker.from_env()


def test_image(registry: str, repository: str, category: str, challenge: str):
    image_name = f"{registry}/{utils.get_image_name(repository, category, challenge)}"
    if category == "web":
        print(f"Testing {image_name}...")
        if (status_code := test_web_image(registry, repository, category, challenge)) == 200:
            print(f"Test passed for {image_name}")
            return True
        elif status_code == -1:
            print(f"Test FAILED for {image_name}, received connection error")
            return False
        else:
            print(f"Test FAILED for {image_name}, status code: {status_code}")
            return False
    elif category == "pwn":
        print(f"Testing {image_name}...")
        if test_pwn_image(registry, repository, category, challenge):
            print(f"Test passed for {image_name}")
            return True
        else:
            print(f"Test FAILED for {image_name}")
            return False
    else:
        return True


def test_web_image(registry: str, repository: str, category: str, challenge: str):
    image_name = f"{registry}/{utils.get_image_name(repository, category, challenge)}"
    container = client.containers.run(
        image=image_name,
        name=utils.clean(challenge),
        auto_remove=True,
        detach=True,
        publish_all_ports=True
    )
    container.reload()
    port = int(list(container.ports.values())[0][0]["HostPort"])

    try:
        s = requests.Session()
        s.mount('http://', HTTPAdapter(max_retries=Retry(total=10, backoff_factor=1, backoff_max=5)))
        res = s.get(f"http://localhost:{port}/")
        container.stop()

        return res.status_code
    except requests.exceptions.ConnectionError as ex:
        print(ex)
        return -1

def test_pwn_image(registry: str, repository: str, category: str, challenge: str):
    image_name = f"{registry}/{utils.get_image_name(repository, category, challenge)}"
    container = client.containers.run(
        image=image_name,
        name=utils.clean(challenge),
        auto_remove=True,
        detach=True,
        ports={"8000/tcp": 8000}
    )

    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client.connect(("localhost", 8000))
    data = socket_client.recv(1024)

    socket_client.close()
    container.stop()
    return data != b''
