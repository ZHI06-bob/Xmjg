"""S3 冒烟测试：import app 与日志初始化。"""

from datetime import date
from pathlib import Path


def test_import_app() -> None:
    """import app 成功。"""
    import app

    assert app is not None


def test_init_logging_creates_daily_files() -> None:
    """init_logging() 后当日 app.log 与 error.log 存在。"""
    from app.gongyong.rizhi import init_logging

    init_logging()
    log_dir = Path(__file__).resolve().parents[2] / "RiZhiWenJian" / date.today().isoformat()
    assert (log_dir / "app.log").exists()
    assert (log_dir / "error.log").exists()
