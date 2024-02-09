import setuptools

__version__ = "0.0.0"
REPO_NAME = "automated_document_analysis"
AUTHOR_NAME = "amulyaprasanth"
SRC_REPO = "automated_document_analysis"
AUTHOR_EMAIL = "amulyaprasanth301@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_NAME,
    author_email = AUTHOR_EMAIL,
    description = "Automated Document Analysis: Human vs. Machine Text Detection",
    url = f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    packages = setuptools.find_packages(where="src")
)