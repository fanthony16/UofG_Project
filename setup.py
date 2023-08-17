from setuptools import setup, find_packages
from typing import List

def get_requirement(filePath:str)-> List[str]:
    '''
        This function returns the list of required packages for the implementation
    '''
    HYPEN_E_DOT = "-e ."
    requirement =[]
    with open(filePath) as file_obj:
        requirement = file_obj.readlines()
    requirement = [req.replace("\n","")  for req in requirement]
    
    
    if HYPEN_E_DOT in requirement:
        requirement.remove(HYPEN_E_DOT)
    return requirement


setup(
    name="UofG ML Project",
    version="0.0.0.1",
    author="Taiwo Oluwafemi",
    author_email= "ot1489q@gre.ac.uk",
    packages=find_packages(),
    install_requires= get_requirement("requirement.txt")   
)


