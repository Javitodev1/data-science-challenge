import enum
import os


class Platform(enum.Enum):
    """Represent supported operating systems."""

    Unix = enum.auto()
    Windows = enum.auto()


class UnsupportedOSError(Exception):
    """Custom error class for Unsupported OS."""

    def __init__(self, msg: str) -> None:
        super().__init__(self, msg)


def get_os() -> Platform:
    """Get the current OS as Platform Enum.

    Raises:
        UnsupportedOSError: exception is raised in case the script is run
        in an unsupported OS.

    Returns:
        Platform: current OS representation

    """
    current_os = os.name
    if current_os == "posix":
        return Platform.Unix
    if current_os == "nt":
        return Platform.Windows

    msg = f"Unsupported OS:{current_os}"
    raise UnsupportedOSError(msg)


def setup_enviroment() -> None:
    """Execute the development environment of the application."""
    # check if venv exists, otherwise, create it

    # activate venv

    # check if python dependencies are installed, otherwise, ask to install them

    # check if docker engine or docker desktop is installed, ask to try to install it

    # check if the sql image is downloaded, otherwise, try to install it

    # check if the sql container is running, otherwise, try to start the container

    # load local env

    # config app

    # run app


if __name__ == "__main__":
    setup_enviroment()
