# -*- coding: utf-8 -*-
import logging
import unittest

import rt_with_exceptions as rt


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(condition=is_frozen, reason="Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            runn = rt.Runner(name='Спортсмен № 1', speed=-10)
            for i in range(10):
                runn.walk()
            self.assertEqual(runn.distance, 100)
            logging.info('test_walk" выполнен успешно')
        except ValueError as err:
            logging.error(f"Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(condition=is_frozen, reason="Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            runn = rt.Runner(name=1, speed=8)
            for i in range(1, 11):
                runn.run()
            self.assertEqual(runn.distance, 160)
            logging.info('test_run" выполнен успешно')
        except TypeError as err:
            logging.error("Неверный тип данных для объекта Runner", exc_info=True)

    @unittest.skipIf(condition=is_frozen, reason="Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner1 = rt.Runner(name='Спортсмен № 1')
        runner2 = rt.Runner(name='Спортсмен № 2')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


# if __name__ == 'test_12_4':
logging.basicConfig(level=logging.INFO, filename="runner_tests.log", encoding="UTF-8",
                    filemode="w", format="%(name)s | %(asctime)s | %(levelname)s | %(message)s")

if __name__ == '__main__':
    logging.info('new test')
    unittest.main()
