"""璇衡（XUANHENG）算子骨架单测：名帖完整、桩位齐整、只增不覆盖。"""
import unittest

from xuanheng import Xuanheng


class TestXuanheng(unittest.TestCase):
    def setUp(self):
        self.op = Xuanheng()

    def test_describe(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "xuanheng")
        self.assertEqual(d["code"], "XUANHENG")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))
        self.assertTrue(d["mingwen"])

    def test_propose_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.propose(None)

    def test_submit_jiancao_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.submit_jiancao(None)


if __name__ == "__main__":
    unittest.main()
