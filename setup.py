from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Reads a requirements file and returns a list of dependencies.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [
            req.strip() for req in requirements if req.strip() and not req.startswith("#")
        ]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='diamondpriceprediction',  # Added missing comma
    version='0.0.1',
    author='harsh',
    author_email='mishraharsh689@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages(),
)
