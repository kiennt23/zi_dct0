import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zi_dct0",
    version="0.0.1",
    author="Kien Nguyen",
    author_email="kiennt23@gmail.com",
    description="ZI DCT0 implementation in python",
    long_description="ZI DCT0 implementation in python",
    long_description_content_type="text/markdown",
    url="https://gitlab.com/kiennt23/price_watcher.git",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)