from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
      name='iso226',
      
      version='1.0.0',
      
      description='ISO',
      
      long_description=long_description,
      
      url='',
      
      
      author='Sergio Callegari',
      author_email='sergio.callegari@unibo.it',
      
      license='GNU General Public License v3.0',
      
      classifiers=[
           'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Topic :: Scientific/Engineering',
    
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
      ],
      
      # What does your project relate to?
    keywords='Acoustics',
    
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    
    install_requires=['numpy',
                      'scipy'],
    
    extras_require={},
      
      )