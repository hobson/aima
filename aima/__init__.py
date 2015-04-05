# Copyright (C) 2009-2014 Peter Norvig <peter.norvig@gmail.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""aima -- Artificial Intelligence, A Modern Approach, by Stuart Russell and Peter Norvig"""

__version__ = '2015.4.5'
__authors__ = [
    'Peter Norvig <peter.norvig@gmail.com>',
    'Darius Bacon <withal@gmail.com>',
    'Spotted Metal? <spottedMetal@gmail.com>',
    'S R Burnet? <srburnet@gmail.com>',
    'Phil Ruggera',
    'Peng Shao',
    'Amit Patil',
    'Ted Nienstedt',
    'Jim Martin',
    'Ben Catanzariti',
    'Hobson Lane <admin@totalgood.com>'
    ]
__github_url__ = "https://github.com/hobson/%s" % (__name__)

# import utils
# import text
# import search
# import probability
# import logic
# import rl
__all__ = ['utils', 'text', 'search', 'probability', 'logic', 'rl']


# import pkgutil
# __all__ = []
# for loader, module_name, is_pkg in  pkgutil.walk_packages(__path__):
#     __all__.append(module_name)
#     module = loader.find_module(module_name).load_module(module_name)
#     exec('%s = module' % module_name)