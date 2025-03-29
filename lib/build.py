import os

import docker.errors

from lib.utils import get_image_name

client = docker.from_env()


def __find_dockerfile(base_path: str, repository: str, category: str, challenge: str):
    dockerfiles = []
    for root, dirs, files in os.walk(os.path.join(base_path, repository, category, challenge, "src")):
        if "Dockerfile" in files:
            dockerfiles.append(root)
    return dockerfiles


def build_image(base_path: str, registry: str, repository: str, category: str, challenge: str):
    dockerfiles = __find_dockerfile(base_path, repository, category, challenge)
    image_name = get_image_name(repository, category, challenge)
    if len(dockerfiles) != 1:
        print(f"More or less than one Dockerfile found in {image_name}!")
        return False
    dockerfile = dockerfiles[0]
    print(f"Building {image_name}...")
    try:
        client.images.build(
            path=dockerfile,
            tag=f"{registry}/{image_name}",
            rm=True,
        )
        print(f"Successfully built {registry}/{image_name}")
        return True
    except docker.errors.BuildError as ex:
        print(f"FAILED to build {registry}/{image_name}")
        print(ex)
        return False
