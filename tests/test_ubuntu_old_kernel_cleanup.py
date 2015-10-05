import unittest

from ubuntu_old_kernel_cleanup import cleanup

EXPECTED = [
        ('linux-headers-3.13.0-44', (3, 13, 0, 44, 73)),
        ('linux-headers-3.13.0-44-generic', (3, 13, 0, 44, 73)),
        ('linux-image-3.13.0-44-generic', (3, 13, 0, 44, 73))
]

class TestUbuntuOldKernelCleanup(unittest.TestCase):
    def test_main(self):
        cleanup.run_command = return_dpkg_query_and_uname_responses
        cleanup.output = result_collector
        cleanup.main()
        self.assertItemsEqual(result, EXPECTED)

result = None

def result_collector(arg):
    global result
    result = arg

def return_dpkg_query_and_uname_responses(command, *args):
    response = {
        'dpkg-query': """linux-headers-3.0\t\tunknown ok not-installed
linux-headers-3.13.0-40-generic\t\tunknown ok not-installed
linux-headers-3.13.0-43-generic\t\tunknown ok not-installed
linux-headers-3.13.0-44\t3.13.0-44.73\tinstall ok installed
linux-headers-3.13.0-44-generic\t3.13.0-44.73\tinstall ok installed
linux-headers-3.13.0-46\t3.13.0-46.79\tinstall ok installed
linux-headers-3.13.0-46-generic\t3.13.0-46.79\tinstall ok installed
linux-headers-3.13.0-65\t3.13.0-65.106\tinstall ok installed
linux-headers-3.13.0-65-generic\t3.13.0-65.106\tinstall ok installed
linux-image-3.0\t\tunknown ok not-installed
linux-image-3.13.0-40-generic\t3.13.0-40.69\tdeinstall ok config-files
linux-image-3.13.0-43-generic\t3.13.0-43.72\tdeinstall ok config-files
linux-image-3.13.0-44-generic\t3.13.0-44.73\tinstall ok installed
linux-image-3.13.0-46-generic\t3.13.0-46.79\tinstall ok installed
linux-image-3.13.0-65-generic\t3.13.0-65.106\tinstall ok installed
""",
        'uname': '3.13.0-46-generic',
    }
    return response[command]
