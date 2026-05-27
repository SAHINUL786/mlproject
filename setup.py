from typing import List
from setuptools import find_packages,setup
HYPEN_e_DOT = '-e .'
def get_requirements(filepath:str)->list:
    requirements = []
    with open (filepath) as file_obj:
       requirements =  file_obj.readlines()
       requirements = [req.replace("\n","") for req in requirements]
    if HYPEN_e_DOT in requirements:
        requirements.remove(HYPEN_e_DOT)
    return requirements
    

setup(
    name='mlproject',
    version='0.0.1',
    author='sahinul',
    author_email='sksahinulislam2511@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirement.txt')

)