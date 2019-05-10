import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="spyce",
    version="0.0.1",
    author="Filippo Volpe",
    author_email="filippovolpe98@gmail.com",
    description=("ngspice glue library"),
    license="Apache 2.0",
    keywords="Python",
    url="https://github.com/volpx/spyce",
    packages=['spyce'],
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GPL v3.0',
        'Programming Language :: Python',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ]
)
