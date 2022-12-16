from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    this function returns list of requirements 
    '''
    requirements_list : List[str] = []

    '''
    finish the code to get list of requirements from requirements.txt
    '''

    return requirements_list

setup(

    name = "sensor",
    version = "0.0.1",
    author = "nageswar",
    author_email = "nageswar.307@gmail.com",
    packages = find_packages(),
    install_requires = []
)