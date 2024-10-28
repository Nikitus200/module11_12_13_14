import code as cd
import unittest as un
import logging

logging.basicConfig(level=logging.INFO,
                        filemode="w",
                        filename="runner_tests.log",
                        encoding="UTF-8",
                        format="%(asctime)s ┆ ⛔ ┆ %(levelname)s ┆ ⛔ ┆ %(message)s")
class RunnerTest(un.TestCase):
    is_frozen = False
    @un.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            n = cd.Runner("test_name", -2)
            logging.info("'test_walk' выполнен успешно")
            for i in range(10):
                n.walk()
            self.assertEqual(n.distance, 50)
        except ValueError as exc:
            logging.warning("Неверная скорость для Runner", exc_info=True)
    @un.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            n1 = cd.Runner(15)
            logging.info("'test_run' выполнен успешно")
            for i in range(10):
                n1.run()
            self.assertEqual(n1.distance, 100)
        except TypeError as exc:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)
    @un.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        obj1 = cd.Runner("test_name1")
        obj2 = cd.Runner("test_name2")
        for i in range(10):
            obj1.run()
            obj2.walk()
        self.assertNotEqual(obj1.distance, obj2.distance)

if __name__ == "__main__":
    un.main()