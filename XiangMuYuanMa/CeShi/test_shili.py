"""示例模块冒烟测试。"""

from app.shili.demo import demo


def test_demo_returns_value() -> None:
    """demo() 可正常调用并返回预期值。"""
    assert demo() == "shili"
