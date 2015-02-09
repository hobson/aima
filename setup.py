# setup.py for aima package (Norvig & Russel, AI: Modern Approach)
from setuptools import find_packages, setup

import os

from aima import __version__ as version
from aima import __authors__, __github_url__
from aima import __doc__ as description
from aima import __name__ as package_name

print('Installing package named {0}. . .'.format(package_name))

try:
    from pip.req import parse_requirements
    requirements = list(parse_requirements('requirements.txt'))
except:
    requirements = []
install_requires=[str(req).split(' ')[0].strip() for req in requirements if req.req and not req.url]
print('requires: %r' % install_requires)
dependency_links=[req.url for req in requirements if req.url]
print('dependcies: %r' % dependency_links)

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError, OSError):
    long_description = 'Python packages implementing the algorithms and example code in the textbook "Artificial Intalligence: A Modern Approach" by Norvig and Russell.'

EXCLUDE_FROM_PACKAGES = []

setup(
    name = package_name,
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),   #[package_name],  
    include_package_data = True,  # install non-.py files listed in MANIFEST.in (.js, .html, .txt, .md, etc)
    install_requires = install_requires,
    dependency_links = dependency_links,
    version = version,
    description = description,
    long_description = long_description or open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    author = ', '.join(__authors__),
    author_email = "peter.norvig@gmail.com",
    #tests_require = ['doctest'],
    #test_suite = 'setuptest.setuptest.SetupTestSuite',
    #cmdclass = {'test': test},
    url = __github_url__,
    download_url = "%s/tarball/%s" % (__github_url__, version),
    keywords = ["ai", "ml", "artificial intelligence", "machine intelligence", "norvig", "russell", "agent", "bot", "book", "textbook", "algorithm", "machine-learning", "search"],
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
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Scientific/Engineering :: Mathematics",
        ],
)
