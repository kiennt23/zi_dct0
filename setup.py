import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zi_dct0",
    version="0.0.8",
    author="Kien Nguyen",
    author_email="kiennt23@gmail.com",
    description="ZI DCT0 implementation in python",
    long_description=long_description,
    url="https://github.com/kiennt23/zi_dct0.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
