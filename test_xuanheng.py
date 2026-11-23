"""璇衡（XUANHENG）算子单测：名帖完整、行为达标、只增不覆盖。"""
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

    def test_propose(self):
        out = self.op.propose([{"name": "甲", "score": 2}, {"name": "乙", "score": 9}])
        self.assertEqual(out["best"]["name"], "乙")
        with self.assertRaises(ValueError):
            self.op.propose([])

    def test_submit_jiancao(self):
        jid = self.op.submit_jiancao("笺稿正文")
        self.assertTrue(jid.startswith("JC-"))


if __name__ == "__main__":
    unittest.main()
