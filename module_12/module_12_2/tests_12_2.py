import code as cd
import unittest as un

class TournamentTest(un.TestCase):

    @classmethod
    def setUpClass(cls):
        global all_results
        all_results = {}

    def setUp(self):
        global obj1, obj2, obj3
        obj1 = cd.Runner("Усэйн", speed=10 )
        obj2 = cd.Runner("Андрей", speed=9)
        obj3 = cd.Runner("Ник", speed=3)

    def test_run(self):
        obj = cd.Tournament(90, obj1, obj3)
        dict_ = obj.start()
        for _ in dict_.values():
            pass
        dict_1 = {}
        for k, v in dict_.items():
            dict_1.update([(k, v.name)])
        all_results.update([("1", dict_1)])
        self.assertTrue(dict_[max(dict_1)].name, _.name)

    def test_run2(self):
        obj = cd.Tournament(90, obj2, obj3)
        dict_ = obj.start()
        for _ in dict_.values():
            pass
        dict_2 = {}
        for k, v in dict_.items():
            dict_2.update([(k, v.name)])
        all_results.update([("2", dict_2)])
        self.assertTrue(dict_[max(dict_2)].name, _.name)

    def test_run3(self):
        obj = cd.Tournament(90, obj1, obj2, obj3)
        dict_ = obj.start()
        for _ in dict_.values():
            pass
        dict_3 = {}
        for k, v in dict_.items():
            dict_3.update([(k, v.name)])
        all_results.update([("3", dict_3)])
        self.assertTrue(dict_[max(dict_3)].name, _.name)

    @classmethod
    def tearDownClass(cls):
        for k, v in all_results.items():
            print(v)

if __name__ == "__main__":
    un.main()