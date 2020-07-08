import unittest
import subprocess
import math

class TestSquare(unittest.TestCase):

    def test_positive(self):
        tests = [
            (0,         0**2,       False),
            (1.1,       1.1**2,     False),
            (10,        10**2,      False),
            (10000,     10000**2,   False)
        ]
        for test in tests:
            self.run_process(test)
    
    def test_negative(self):
        tests = [
            (-0,        (-0)**2,       False),
            (-1.1,      (-1.1)**2,     False),
            (-10,       (-10)**2,      False),
            (-10000,    (-10000)**2,   False)
        ]
        for test in tests:
            self.run_process(test)
    
    def test_text(self):
        tests = [
            ("", None, True),
            ("Crash", None, True),
            ("asdasdkasdasdasdasdasdasdasdasd", None, True),
        ]
        for test in tests:
            self.run_process(test)

    def run_process(self, context):
        arg, expected_out, expected_err = context

        p = subprocess.Popen(["./square.out", str(arg)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = [str(s.strip(), "utf-8") for s in p.communicate()]
        exitcode = p.wait()

        if not expected_err:
            # If an error is not expected, make sure exitcode is 0, and that the answer is correct
            self.assertEqual(exitcode, 0)
            self.assertAlmostEqual(float(stdout), expected_out)
        else:
            # If we expect an error, (such as passing a string in instead of a number), then make sure it doesnt
            # exit successfully
            self.assertNotEqual(exitcode, 0)

