# -*- coding: utf-8 -*-
# This file is part of pygal
#
# A python svg graph plotting library
# Copyright © 2012-2015 Kozea
#
# This library is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pygal. If not, see <http://www.gnu.org/licenses/>.

import pytest
import pygal
from pygal.etree import etree
import sys
from . import get_data


@pytest.fixture
def etreefx(request):
    if request.param == 'etree':
        etree.to_etree()
    if request.param == 'lxml':
        etree.to_lxml()


def pytest_generate_tests(metafunc):
    if etree._lxml_etree and sys.version_info[:2] != (2, 6):
        metafunc.fixturenames.append('etreefx')
        metafunc.parametrize('etreefx', ['lxml', 'etree'], indirect=True)
    if sys.version_info[:2] != (2, 6):
        if not etree._lxml_etree:
            raise ImportError('lxml is required under python 2.6')

    if "Chart" in metafunc.funcargnames:
        metafunc.parametrize("Chart", pygal.CHARTS)
    if "datas" in metafunc.funcargnames:
        metafunc.parametrize(
            "datas",
            [
                [("Serie %d" % i, get_data(i)) for i in range(s)]
                for s in (5, 1, 0)
            ])
