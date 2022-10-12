from setuptools import find_packages, setup

with open("README.md", 'r', encoding= 'utf-8') as f: 
    long_description= f.read() 

classifiers= [
    "Development Status :: 3 - Alpha",
    'Intended Audience :: Developers',
    "Programming Language :: Python :: 3.7",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent"
]

setup(
    name= 'vietokenizer', 
    version= '1.0.3', 
    description= 'Vietnamese Tokenizer package based on deep learning method',
    long_description= long_description, 
    long_description_content_type= 'text/markdown',
    url= 'https://github.com/Nguyendat-bit/VieTokenizer', 
    author= 'Dat Tien Nguyen',
    author_email= 'nduc0231@gmail.com', 
    maintainer='Dat Tien Nguyen',
    maintainer_email= 'nduc0231@gmail.com',
    classifiers= classifiers,
    keywords= 'vietokenizer',
    packages= find_packages(), 
    install_requires= ['tensorflow>=2.8.2', "gdown>=4.4.0"],
    python_requires= ">=3.7", 
)