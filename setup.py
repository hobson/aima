# setup.py for aima package
from distutils.core import setup

from aima import __version__, __authors__, __github_url__
from aima import __name__ as package_name
import os

try:
    from pip.req import parse_requirements
    requirements = list(parse_requirements('requirements.txt'))
except:
    requirements = []
install_requires=[str(req).split(' ')[0].strip() for req in requirements if req.req and not req.url]
dependency_links=[req.url for req in requirements if req.url]

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError, OSError):
    try:
        long_description = open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    except:
        long_description = package_name

setup(
    name = package_name,
    packages = ["aima"],  # without this: Downloading/unpacking aima ... ImportError: No module named aima ... from aima import __version__, __name__, __doc__, _github_url_
    include_package_data = True,  # install non-.py files listed in MANIFEST.in (.js, .html, .txt, .md, etc)
    install_requires = install_requires,
    dependency_links = dependency_links,
    version = __version__,
    description = __doc__,
    long_description = long_description,
    author = ', '.join(__authors__),
    author_email = "peter.norvig@gmail.com",
    #tests_require = ['doctest'],
    #test_suite = 'setuptest.setuptest.SetupTestSuite',
    #cmdclass = {'test': test},
    url = __github_url__,
    download_url = "%s/archive/v%s.tar.gz" % (__github_url__, __version__),
    keywords = ["ai", "agent", "bot", "book", "textbook", "algorithm", "machine-learning", "search"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.5",
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Mathematics",
        ],
)
