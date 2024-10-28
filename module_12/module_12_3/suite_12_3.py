import unittest as un
import tests_12_3 as ts

objTS = un.TestSuite()
objTS.addTest(un.TestLoader().loadTestsFromTestCase(ts.RunnerTest))
objTS.addTest(un.TestLoader().loadTestsFromTestCase(ts.TournamentTest))

runner = un.TextTestRunner(verbosity=2)
runner.run(objTS)