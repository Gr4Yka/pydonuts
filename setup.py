from setuptools import setup

setup(
    name='pydonuts',
    version='1.0.0',
    description='Library for work with VK Donuts app.',
    license='GNU General Public License v3.0',
    packages=['pydonuts'],
    author='Gr4Yka',
    author_email='greywolf2428@gmail.com',
    url='https://github.com/Gr4Yka/pydonuts',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'importlib',
        'requests',
        'json'
    ]
)
