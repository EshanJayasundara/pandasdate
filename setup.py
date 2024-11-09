from setuptools import setup, find_packages

setup(
    name="pandasdate",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A pandas DataFrame extension with date tracking",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pandasdate",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.2.2",
        "numpy>=1.26.3",
        "pyarrow>=18.0.0",
        "openpyxl>=3.1.5",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
