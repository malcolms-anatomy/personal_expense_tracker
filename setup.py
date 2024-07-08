from setuptools import setup, find_packages

setup(
    name='personal_expense_tracker',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'tk',
    ],
    entry_points={
        'console_scripts': [
            'expense-tracker=expense_tracker:main',
        ],
    },
    description='A simple personal expense tracker application built with Python.',
    author='Malcolm Iheremelam',
    author_email='malcolmihere@outlook.com',
    url='https://github.com/yourusername/personal_expense_tracker',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

