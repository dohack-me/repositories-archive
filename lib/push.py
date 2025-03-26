import docker

from lib.utils import get_image_name

client = docker.from_env()


def push_image(registry: str, repository: str, category: str, challenge: str):
    image_name = get_image_name(repository, category, challenge)
    print(f"Pushing {registry}/{image_name}")
    client.images.push(repository=f"{registry}/{image_name}", tag="latest")
    print(f"Finished pushing {registry}/{image_name}")
