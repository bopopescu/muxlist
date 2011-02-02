import unittest
from server_commands import ServerCommandsTestCase
from connection_pool import ConnectionPoolTestCase
from pipeline import PipelineTestCase
from lock import LockTestCase

def all_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ServerCommandsTestCase))
    suite.addTest(unittest.makeSuite(ConnectionPoolTestCase))
    suite.addTest(unittest.makeSuite(PipelineTestCase))
    suite.addTest(unittest.makeSuite(LockTestCase))
    return suite
