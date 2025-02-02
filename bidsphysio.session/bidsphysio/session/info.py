""" NOTE: When bumping up the version number, double-check if you
need to also bump up the version of the dependencies
"""

__version__ = "21.06.24"
__author__ = "Pablo Velasco, Chrysa Papadaniil"
__author_email__ = "pablo.velasco@nyu.edu"
__url__ = "https://github.com/cbinyu/bidsphysio"
__packagename__ = 'bidsphysio.session'
__description__ = "physio-session-to-BIDS Converter"
__license__ = "MIT"
__longdesc__ = """Automatically converts a whole session worth of physio data to BIDS physiological recording."""

CLASSIFIERS = [
    'Environment :: Console',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Topic :: Scientific/Engineering'
]

PYTHON_REQUIRES = ">=3.6"

REQUIRES = [
    'bidsphysio.base>=1.4.0',
    'bids',
    'pandas',
    'numpy >= 1.17.1',
    'matplotlib',
]

TESTS_REQUIRES = [
    'pytest'
]

EXTRA_REQUIRES = {
    'tests': TESTS_REQUIRES,
}

# Flatten the lists
EXTRA_REQUIRES['all'] = sum(EXTRA_REQUIRES.values(), [])
