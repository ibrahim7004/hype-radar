from setuptools import setup, find_packages

setup(
    name='hype-radar',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'flask',
        'scikit-learn',
        'pandas',
        'numpy',
        'tweepy',
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'hype-radar=src.main:main',
        ],
    },
)