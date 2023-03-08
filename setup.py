
from setuptools import setup, find_packages

setup(
    name="clean",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "clean=clean:sort_folder"
        ]
    }
)






