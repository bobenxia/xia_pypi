import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xia_pypi",
    version="0.0.1",
    author="xia",
    author_email="xiazheng1996@126.com",
    description="xia pypi",
    url="https://github.com/bobenxia/xia_pypi",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)