import unittest

import logging

import pypluggy
import pylogconf

from pypluggy.mgr import Mgr

pylogconf.setup()
pypluggy.mgr.logger.setLevel(logging.DEBUG)
# pypluggy.mgr.logger.disabled = False
# pylogconf.show_tree()


class TestNames(unittest.TestCase):
    def testList(self):
        m = Mgr()
        m.load_modules()
        self.assertListEqual(m.list_names(cls=unittest.TestCase), ['TestNames'], msg='uh uh')

    def testInstantiate(self):
        m = Mgr()
        m.load_modules()
        t = m.instantiate_name(cls=unittest.TestCase, name='TestNames')
        self.assertIsInstance(t, unittest.TestCase)