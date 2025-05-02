
from setuptools import setup, find_packages

setup(
    name="MiniDB",
    version="0.1",
    packages=find_packages(),  # automatically includes 'minidb'
    py_modules=["main"],       # includes the standalone main.py
    install_requires=[],
    entry_points={
        'console_scripts': [
            'gizmodb=main:main',  # CLI entry point: yourcli → main.main()
        ],
    },
)


##
#


# ###################################################    NOTES    ######################################################






# ######################################################################################################################

##
#

