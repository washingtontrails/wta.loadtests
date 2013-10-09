import unittest
from collective.funkload import testcase

class Homepage(testcase.FLTestCase):
    """This test use a configuration file Homepage.conf.
    """

    def setUp(self):
        """Setting up test."""
        self.base_url = '%s/wtamain/wtaadmin' % self.conf_get('main', 'url')

    def test_Homepage(self):
        self.get(self.base_url, description="WTA homepage")


def test_suite():
    return unittest.makeSuite(Homepage)
