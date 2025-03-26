import lib.input
import lib.build
import lib.test
import lib.utils
import lib.push

REGISTRY = "dohackme.azurecr.io"

successes = []

repositories = lib.input.get_repository_input()
for repository in repositories:
    categories = lib.input.get_category_input(repository)
    for category in categories:
        challenges = lib.input.get_challenge_input(repository, category)
        for challenge in challenges:
            built = lib.build.build_image(REGISTRY, repository, category, challenge)
            if built:
                if lib.test.test_image(REGISTRY, repository, category, challenge):
                    successes.append((REGISTRY, repository, category, challenge))

lib.utils.print_line()

if (input("Build all successful images? (Y/n) ") or "y").lower() == "y":
    for success in successes:
        lib.push.push_image(success[0], success[1], success[2], success[3])