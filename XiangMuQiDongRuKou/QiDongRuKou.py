"""启动入口：解析环境、加载参数与 .env、初始化日志并输出生效参数。"""

import argparse
import logging
import os
from pathlib import Path

import yaml
from app.gongyong.rizhi import init_logging

_PROJECT_ROOT = Path(__file__).resolve().parents[1]
_CONFIG_PATH = _PROJECT_ROOT / "XiangMuQiDongRuKou" / "QiDongCanShu.yaml"


def _load_dotenv() -> None:
    """读取项目根 .env；已存在的环境变量优先。"""
    env_file = _PROJECT_ROOT / ".env"
    if not env_file.exists():
        return
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip("'\""))


def parse_args() -> argparse.Namespace:
    """解析启动参数。"""
    parser = argparse.ArgumentParser(description="项目启动入口")
    parser.add_argument("--env", choices=["dev", "prod"], default="dev", help="运行环境")
    return parser.parse_args()


def _load_settings(env: str) -> dict:
    """读取启动参数，并用环境变量覆盖同名键。"""
    with _CONFIG_PATH.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file) or {}
    defaults = data.get(env) or data.get("dev", {})
    settings = {}
    for key, value in defaults.items():
        raw = os.environ.get(key.upper())
        if raw is None:
            settings[key] = value
        elif isinstance(value, int):
            settings[key] = int(raw)
        else:
            settings[key] = raw
    return settings


def main() -> None:
    """初始化日志并打印生效参数。"""
    args = parse_args()
    _load_dotenv()
    init_logging()
    settings = _load_settings(args.env)
    logging.getLogger(__name__).info("启动入口 env=%s 参数=%s", args.env, settings)
    print(f"env={args.env}")
    for key, value in settings.items():
        print(f"{key}={value}")


if __name__ == "__main__":
    main()
