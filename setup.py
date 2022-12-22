from setuptools import setup, find_packages

with open("README.md", "r") as fh:

    long_description = fh.read()

install_requires = [
    "requests==2.28.1",
    "xmltodict==0.13.0",
]


setup(
    name="kopisapi",
    version="0.1.0",
    license="MIT license",
    author="jinwooyoon",
    author_email="say_stop@naver.com",
    url="https://github.com/jinwooyoon/kopisapi",
    description="This program provides data related to Korean performances.",
    install_requires=install_requires,
    python_requires = ">=3",
    packages=find_packages()
)
