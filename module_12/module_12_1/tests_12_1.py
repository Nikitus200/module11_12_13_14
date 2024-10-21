import The_source_code as ts
import unittest as un


class RunnerTest(un.TestCase):
    def test_walk(self):
        n = ts.Runner("test_name")
        for i in range(10):
            n.walk()
        self.assertEqual(n.distance, 100) #Если поставим 50, пройдут все три теста

    def test_run(self):
        n1 = ts.Runner("test_name")
        for i in range(10):
            n1.run()
        self.assertEqual(n1.distance, 100)

    def test_challenge(self):
        obj1 = ts.Runner("test_name1")
        obj2 = ts.Runner("test_name2")
        for i in range(10):
            obj1.run()
            obj2.walk()
        self.assertNotEqual(obj1.distance, obj2.distance)
if __name__ == "__main__":
    un.main()