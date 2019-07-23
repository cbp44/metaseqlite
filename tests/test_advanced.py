# -*- coding: utf-8 -*-

from .context import metaseqlite

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        assert True
        # self.assertIsNone(sample.hmm())


if __name__ == '__main__':
    unittest.main()
