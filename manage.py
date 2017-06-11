
# Ensure external libs path is added
import sys
sys.path.append('libs')
sys.path.append('services')


from config import create_app
from config.cli import command_manager


if __name__ == "__main__":
    command_manager.app = create_app()
    command_manager.run()
