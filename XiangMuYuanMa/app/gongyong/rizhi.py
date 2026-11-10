"""日志模块：按配置初始化按日期、按级别分文件的日志。"""

import logging.config
import shutil
from datetime import date, timedelta
from pathlib import Path

import yaml

_PROJECT_ROOT = Path(__file__).resolve().parents[3]
_CONFIG_PATH = _PROJECT_ROOT / "HuanJingYiLai" / "rizhi.yaml"


def _load_config() -> dict:
    """读取日志配置。"""
    with _CONFIG_PATH.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file) or {}


def _archive_expired_logs(config: dict) -> None:
    """将超过保留天数的日期目录迁移到归档目录。"""
    log_root = _PROJECT_ROOT / "RiZhiWenJian"
    archive_root = _PROJECT_ROOT / str(config["archive_dir"])
    cutoff = date.today() - timedelta(days=int(config["retention_days"]))
    if not log_root.exists():
        log_root.mkdir(parents=True, exist_ok=True)
        return
    archive_root.mkdir(parents=True, exist_ok=True)
    for child in log_root.iterdir():
        if not child.is_dir() or child.name == "GuiDang":
            continue
        try:
            log_date = date.fromisoformat(child.name)
        except ValueError:
            continue
        if log_date >= cutoff:
            continue
        target = archive_root / child.name
        if target.exists():
            for item in child.iterdir():
                shutil.move(str(item), str(target / item.name))
            child.rmdir()
        else:
            shutil.move(str(child), str(target))


def _build_dict_config(config: dict, date_str: str) -> dict:
    """按配置组装 dictConfig 结构，并创建当日日志目录。"""
    level = str(config.get("level", "INFO"))
    handlers = {}
    for name, spec in config.get("handlers", {}).items():
        filename = _PROJECT_ROOT / str(spec["filename"]).format(date=date_str)
        filename.parent.mkdir(parents=True, exist_ok=True)
        handlers[name] = {
            "class": "logging.FileHandler",
            "level": spec.get("level", level),
            "formatter": "standard",
            "filename": str(filename),
            "encoding": "utf-8",
        }
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {"standard": {"format": str(config["format"])}},
        "handlers": handlers,
        "root": {"level": level, "handlers": list(handlers)},
    }


def init_logging() -> None:
    """读取 HuanJingYiLai/rizhi.yaml 并初始化日志。"""
    config = _load_config()
    _archive_expired_logs(config)
    logging.config.dictConfig(_build_dict_config(config, date.today().isoformat()))
