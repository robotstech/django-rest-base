from enum import Enum


class Environment(Enum):
    DEV = "dev"
    STAGING = "staging"
    PRODUCTION = "prod"
    TEST = "test"
    LOCAL = "local"
    CI = "ci"

    @classmethod
    def get(cls, env_str):
        for env in cls:
            if env_str in {env.name, env.value}:
                return env
