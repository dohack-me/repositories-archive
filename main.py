import input
import build
import test

REGISTRY = "dohackme.azurecr.io"

repositories = input.get_repository_input()
for repository in repositories:
    categories = input.get_category_input(repository)
    for category in categories:
        challenges = input.get_challenge_input(repository, category)
        for challenge in challenges:
            success = build.build_image(REGISTRY, repository, category, challenge)
            if success:
                test.test_image(REGISTRY, repository, category, challenge)