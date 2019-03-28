from app import App
from helpers.config import Config, APP_NAME
import unittest
import sys


class TestSomething(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_env_config_path(self):
        self.assertTrue(type(Config.init_env_config_path()) == list)

    def test_env_config(self):
        self.assertIn(sys.path[0], Config.init_env_config_path())

    @unittest.skipIf(sys.platform.startswith('win'), 'linux required')
    def test_win_sys_disc(self):
        self.assertRaises(EnvironmentError, Config.get_windows_system_disk)

    def test_wind_sd_len(self):
        self.assertEqual(Config.get_windows_system_disk(), 'C:')

    def test_init(self):
        conf = Config()
        self.assertTrue(
            conf.config_file == '{}.yaml'.format(APP_NAME) or conf.config_file == conf.__init__.__defaults__[0])


if __name__ == '__main__':
    unittest.main()
