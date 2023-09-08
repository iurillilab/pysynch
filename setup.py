from distutils.core import setup

from setuptools import find_namespace_packages

with open("requirements_dev.txt") as f:
    requirements_dev = f.read().splitlines()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("README.md") as f:
    long_description = f.read()

setup(
    name="pysynch",
    version="0.1.0",
    author="Luigi Petrucco @ Iurilli Lab",
    author_email="luigi.petrucco@gmail.com",
    license="MIT",
    packages=find_namespace_packages(exclude=("docs", "tests*")),
    install_requires=requirements,
    extras_require=dict(dev=requirements_dev),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Video",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="multiprocessing queues arrays",
    description="Multiprocessing queues for numpy arrays using shared memory",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iurillilab/pysynch",
)