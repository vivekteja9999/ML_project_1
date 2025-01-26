from setuptools import find_packages,setup
from typing import List

hypen="-e ."

def getrequirements(filepath:str)->List[str]:
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[ req.replace("\n" , "")for req in requirements]

        if hypen in requirements:
            requirements.remove(hypen)
    return requirements


setup(
    name="mlproject1",
    author="Vivek_Teja",
    author_email="vivekteja9999@gmail.com",
    packages=find_packages(),
    install_requires=getrequirements('requirements.txt')
)