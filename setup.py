#!/usr/bin/env python
# coding: utf-8

# In[1]:


from setuptools import setup

def readme():
    with open ('README.md') as f:
        README = f.read()
    return README

setuptools.setup(
    name="SSG_API_test", # Replace with your own username
    version="0.0.1",
    author="Ho Jun Le",
    author_email="hojunle@outlook.com",
    description="A Python package to get SSG APIs.",
    long_description= readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/hojunle/SSG_API_test",
    packages=["SSG_API_test"],
    include_package_Data = True
    install_requires=["requests","json","pprint","HTTPBasicAuth"]
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

