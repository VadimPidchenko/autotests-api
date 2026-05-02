import platform
import sys

from config import settings


def create_allure_environment_file():
    """
    Функция для создания файла с переменными окружения для allure
    """

    item = [f"{key}={value}" for key, value in settings.model_dump().items()]
    item.append(f"os_info={platform.system()}, {platform.release()}")
    item.append(f"python_version={sys.version}")

    properties = "\n".join(item)

    with open(settings.allure_results_dir.joinpath("environment.properties"), "w") as file:
        file.write(properties)

