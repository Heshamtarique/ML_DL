import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    



__version__ = "0.0.0"

REPO_NAME = "Summarization"
AUTHOR_USER_NAME = "Hesham"
SRC_REPO = "textSummarization"
AUTHOR_EMAIL = "heshamtarique.jmi@gmail.com"



# this will look for __init__ file in every folder and run it

# make sure you used e . in the requirements file, otherwise it won't work.
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)