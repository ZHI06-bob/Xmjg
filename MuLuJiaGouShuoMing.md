# 项目目录架构说明

> 本文档由 `.claude/skills/project-structure/references/directory-guide.md` 派生同步；两者不一致时以 guide 为准。

## 1. 技术栈

- 单仓单项目，Python **>=3.14**。
- 依赖管理：`uv`；`pyproject.toml` 与 `uv.lock` 位于项目根，`HuanJingYiLai/` 只放依赖说明与辅助文件。
- 构建后端：`hatchling`，`packages = ["XiangMuYuanMa/app"]`。
- 安装方式：editable（乙方案），入口不做 `sys.path` 注入。
- 运行依赖：`pyyaml`；开发依赖：`pytest`、`pytest-html`、`ruff`。
- 项目根路径必须为纯 ASCII（见附节「环境约束」）。

安装步骤：

```bash
uv sync
uv run python -m pytest -q
bash XiangMuQiDongRuKou/QiDong.sh --env dev
```

## 2. 目录结构

```text
project-root/
├── MuLuJiaGouShuoMing.md
├── HuanJingYiLai/
│   ├── YunXingYiLai/
│   │   └── ShuoMing.md
│   ├── KaiFaYiLai/
│   │   └── ShuoMing.md
│   ├── HuanJingBianLiang/
│   │   └── .env.example
│   └── rizhi.yaml
├── XiangMuYuanMa/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── mokuai_a/
│   │   │   └── __init__.py
│   │   ├── mokuai_b/
│   │   │   └── __init__.py
│   │   └── gongyong/
│   │       ├── __init__.py
│   │       └── rizhi.py
│   └── CeShi/
│       ├── __init__.py
│       └── test_maoyan.py
├── RiZhiWenJian/
│   ├── .gitkeep
│   └── GuiDang/
│       └── .gitkeep
├── XiangMuBaoGao/
│   ├── RenGongZhuanXie/
│   │   ├── JiXianQueRenQingDan_S0.md
│   │   └── S4_YanZhengJiLu.md
│   └── ZiDongShengCheng/
│       └── .gitkeep
├── XiangMuQiDongRuKou/
│   ├── QiDongRuKou.py
│   ├── QiDong.sh
│   └── QiDongCanShu.yaml
├── .claude/skills/project-structure/
│   ├── SKILL.md
│   └── references/directory-guide.md
├── pyproject.toml
├── uv.lock
└── .gitignore
```

六个一级项均在项目根：`HuanJingYiLai/`、`XiangMuYuanMa/`、`RiZhiWenJian/`、`XiangMuBaoGao/`、`XiangMuQiDongRuKou/`、`MuLuJiaGouShuoMing.md`。

## 3. 命名

- 六个一级项：目录与说明文档用拼音首字母大写，如 `RiZhiWenJian/`、`MuLuJiaGouShuoMing.md`。
- 可 import 的包/模块：小写拼音，如 `app/`、`mokuai_a/`、`gongyong/`。
- 非包目录（日志、报告、启动入口）：大写拼音。
- `XiangMuYuanMa/` 为源码根，本身不参与 import；`app/` 是唯一包根。
- `CeShi/` 与 `app/` 平级，不被 import；含 `__init__.py`（可空），用于 pytest 包结构一致与同名测试模块导入稳定。
- `app/` 及其每个子包目录需含 `__init__.py`（可空），用于 editable 安装与 pytest 导入稳定。
- 工具层 `.claude/skills/project-structure/` 使用工具规范小写名（`SKILL.md`、`directory-guide.md`），不计入六个一级项。

## 4. 配置与依赖

- `pyproject.toml` 负责项目定义、依赖、构建与 pytest 配置三段：

```toml
[project]
name = "xiang-mu-yuan-ma"
version = "0.1.0"
requires-python = ">=3.14"
dependencies = ["pyyaml>=6"]

[dependency-groups]
dev = ["pytest>=8", "pytest-html>=4", "ruff>=0.6"]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["XiangMuYuanMa/app"]

[tool.pytest.ini_options]
testpaths = ["XiangMuYuanMa/CeShi"]
pythonpath = ["XiangMuYuanMa"]
```

- `uv.lock` 由 uv 生成，不手改。
- `HuanJingYiLai/HuanJingBianLiang/.env.example` 只列键名与空值（`LOG_LEVEL=`、`APP_ENV=`），真实值不入库；`.env` 被 `.gitignore` 忽略。
- `HuanJingYiLai/rizhi.yaml` 承载日志配置值，消费方为 `app/gongyong/rizhi.py`。
- `XiangMuQiDongRuKou/QiDongCanShu.yaml` 承载启动参数，消费方为 `XiangMuQiDongRuKou/QiDongRuKou.py`。
- 依赖说明：`YunXingYiLai/ShuoMing.md` 指向 `[project.dependencies]`，`KaiFaYiLai/ShuoMing.md` 指向 `[dependency-groups].dev`。

## 5. 日志

- 配置项：`level=INFO`；`format=%(asctime)s %(levelname)s %(name)s %(message)s`；`retention_days=7`。
- 输出布局：按日期子目录 `RiZhiWenJian/<YYYY-MM-DD>/`，内含 `app.log`（INFO 及以上）与 `error.log`（ERROR）。
- 归档策略：`init_logging()` 启动时按 `retention_days` 计算截止日，早于截止日的日期目录整体迁入 `RiZhiWenJian/GuiDang/<YYYY-MM-DD>/`。
- 入库边界：日志内容不入库；`RiZhiWenJian/.gitkeep` 与 `RiZhiWenJian/GuiDang/.gitkeep` 入库。
- 测试约定：本环境统一使用 `uv run python -m pytest`，不使用 `pytest.exe`（应用控制策略拦截，`os error 4551`）。

## 6. 报告

- 自动报告：`uv run python -m pytest --html=XiangMuBaoGao/ZiDongShengCheng/ceShiBaoGao.html --self-contained-html`。
- 归属：自动产物落 `XiangMuBaoGao/ZiDongShengCheng/`，不入库，仅 `.gitkeep` 占位；人工报告落 `XiangMuBaoGao/RenGongZhuanXie/`，入库。
- 现有报告：`RenGongZhuanXie/JiXianQueRenQingDan_S0.md`（S0 基线）、`RenGongZhuanXie/S4_YanZhengJiLu.md`（S4 验证记录）。

## 7. 启动

- 唯一入口：`XiangMuQiDongRuKou/QiDongRuKou.py`；`QiDong.sh` 为 `uv run python XiangMuQiDongRuKou/QiDongRuKou.py "$@"` 的包装。
- 环境区分：`--env dev|prod`，默认 `dev`。
- 参数优先级：项目根 `.env`（若存在）> `QiDongCanShu.yaml` 的 `dev` 组；`.env` 中同名键按大写覆盖（`HOST`、`PORT`、`WORKERS`）。
- 执行顺序：解析 `--env` → 加载 `.env` → `init_logging()` → 读取并覆盖启动参数 → 记录日志并打印生效参数 → 正常退出。
- 当前基线：`host=127.0.0.1`、`port=8000`、`workers=1`；prod 组不单列，由 `.env` 覆盖。
- 入口直接 `from app.gongyong.rizhi import init_logging`，依赖 editable 安装，不做 `sys.path` 注入。

## 8. 维护

- 新增目录：必须先在 `references/directory-guide.md` 登记，再同步本文档；未登记不得创建。
- 一级项增删：更新 `directory-guide.md`、本文档与 `.claude/skills/project-structure/SKILL.md`，并在 S0 变更记录注明原因。
- 配置或依赖变更：同步更新 `directory-guide.md` 对应行与本文档第 4 节。
- 工具层技能文件变更：同步 S0 变更记录。
- 变更留痕：统一记入 `XiangMuBaoGao/RenGongZhuanXie/JiXianQueRenQingDan_S0.md` 的「变更记录」。

## 附：环境约束

- 项目根路径必须为纯 ASCII。路径含非 ASCII（中文/日文等）时，Python 3.10–3.13 的 `site.py` 会以 locale(cp936) 读取 editable 安装生成的 `.pth`，遇 UTF-8 字节直接 `Fatal Python error`，解释器无法启动。
- 本项目现状：路径含中文且暂不迁移，故 `requires-python = ">=3.14"`（Python 3.14 的 `site.py` 按字节读取 `.pth`，不受 locale 影响）。
- 依据：变更记录 C-08（requires-python 收紧）、C-11（路径 ASCII 前置检查）。
- 未来新项目：由技能 `SKILL.md` 的「环境前置检查」强制要求 ASCII 路径。
