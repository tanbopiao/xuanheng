"""璇衡（XUANHENG）· 择优推演，生成笺稿上交勘判

道统出处：元极恒一·道统构件定名册 V2 ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：择优推演，生成笺稿上交勘判。

边界：本件为算子 v1——骨架桩已按命名映射补齐实现；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Xuanheng:
    """璇衡（XUANHENG）算子 v1。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "XUANHENG"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕
        self.jiancao_box = []
        self._seq = 0

    def describe(self):
        """构件名帖：名、代号、职责、铭文、体系锚。"""
        return {
            "repo": "xuanheng",
            "cn": "璇衡",
            "code": self.CODE,
            "duty": "择优推演，生成笺稿上交勘判",
            "mingwen": "璇衡推演，择优上呈",
            "anchor": self.ANCHOR,
        }

    def propose(self, candidates):
        """璇衡推演：择优出笺。"""
        if not candidates:
            raise ValueError("无候选可推演")
        ranked = sorted(candidates, key=lambda c: -(c.get("score", 0) if isinstance(c, dict) else 0))
        self.events.append({"event": "propose", "candidates": len(candidates)})
        return {"best": ranked[0], "ranked": ranked}

    def submit_jiancao(self, draft):
        """择优上呈：笺稿入勘。"""
        self._seq += 1
        jid = "JC-%04d" % self._seq
        self.jiancao_box.append({"jiancao_id": jid, "draft": draft, "status": "submitted"})
        self.events.append({"event": "submit_jiancao", "jiancao_id": jid})
        return jid
