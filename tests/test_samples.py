import glob
import contextlib
import io
import unittest
from .test_setup import run_program


class Tests(unittest.TestCase):

    def test_samples(self):
        dirList = glob.glob("./examples/**/*.py")
        for d in dirList:
            print(d)
            sio = io.StringIO()
            with contextlib.redirect_stdout(sio):
                run_program("python3", d)

        # run one by one