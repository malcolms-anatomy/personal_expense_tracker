# setup.py

from setuptools import setup, find_packages

setup(
    name='personal_expense_tracker',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        'console_scripts': [
            'expense-tracker=expense_tracker:main',
        ],
    },
)

