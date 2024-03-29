#!/usr/bin/python
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the (LGPL) GNU Lesser General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library Lesser General Public License for more details at
# ( http://www.gnu.org/licenses/lgpl.html ).
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
# written by: Jeff Ortel ( jortel@redhat.com )

import sys
import suds
from setuptools import setup, find_packages

setup(
    name='suds',
    version=suds.__version__,
    description="Lightweight SOAP client",
    long_description="""The "suds" is a lightweight soap-based client for python2 and python3 licensed under LGPL. 
	This is a mirror of https://pypi.python.org/pypi/suds supporting Python2 
	and http://svn.fedorahosted.org/svn/suds/trunk/ supporting Python3 and some fixes.""",
    author='Mircea Dan (Cackharot (original Jeff Ortel))',
    author_email='byrealmircea@yahoo.com',
    packages=find_packages(exclude=['tests']),
    url='https://github.com/ByReaL/suds',
    test_suite='tests',
    license='LGPL',
    keywords='soap, wsdl,basic http binding, basic auth',
    platforms=['Python2', 'Python3'],
    classifiers=[
	    'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
    ]
)
