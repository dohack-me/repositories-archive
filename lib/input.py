import os

from lib.utils import print_line


def __get_immediate_folders(root_dir):
    for folder in os.listdir(root_dir):
        if os.path.isdir(os.path.join(root_dir, folder)) and not folder.startswith(".") and not folder.startswith("_"):
            yield folder


def __get_input(target_name: str, root_dir: str) -> list[str]:
    print(f"Available {target_name}:")
    targets = {}
    for index, target in enumerate(__get_immediate_folders(root_dir)):
        targets.update({index: target})
        print(f"{index}: {target}")

    result_targets = []
    input_targets = input(f"Enter target {target_name}, split with \", \": ").split(", ")
    if input_targets == [""]:
        result_targets = targets.values()
    else:
        for input_target in input_targets:
            if not input_target.isnumeric():
                continue
            result_targets.append(targets.get(int(input_target)))
    print(f"Building for the following {target_name}: {", ".join(result_targets)}")
    print_line()
    return result_targets


def get_repository_input(base_path: str) -> list[str]:
    return __get_input("repositories", base_path)


def get_category_input(base_path: str, repository: str) -> list[str]:
    return __get_input("categories", os.path.join(base_path, repository))


def get_challenge_input(base_path: str, repository: str, challenge: str) -> list[str]:
    return __get_input("challenges", os.path.join(base_path, repository, challenge))
