import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Poultry_Shield-Deep-Learning-for-Poultry-Coccidiosis-Diagnosis"
AUTHOR_USER_NAME = "Shahriyar31"
SRC_REPO = "Poultry_Shield"
AUTHOR_EMAIL = "Shahriyarfarhan3101@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=Shahriyar31,
    author_email=shahriyarfarhan3101@gmail.com,
    description="A small python package for Poultry_Shield app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{Shahriyar31}/{Poultry_Shield-Deep-Learning-for-Poultry-Coccidiosis-Diagnosis}",
    project_urls={
        "Bug Tracker": f"https://github.com/{Shahriyar31}/{Poultry_Shield-Deep-Learning-for-Poultry-Coccidiosis-Diagnosis}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)