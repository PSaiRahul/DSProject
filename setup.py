from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(filepath:str)->List[str]:
    '''Reads the requirements file and returns a list of required packages'''
    requirements = []
    with open(filepath, 'r') as file:
        requirements=file.readlines()
        requirements=[requirement.replace('\n','') for requirement in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements


setup(name='MLProject',
      version='0.0.1',
      author='Rahul',
      author_email='sairahulperumalla51@gmail.com',
      packages=find_packages(),
      install_requires=get_requirements('requirements.txt')
      )