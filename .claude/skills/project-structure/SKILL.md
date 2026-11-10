---
name: project-structure
description: 在新建 Python 项目或生成项目骨架、判断新增文件应放在哪个目录、重构项目目录结构时使用。给出六个一级项的标准目录框架、拼音命名规则，以及基于 uv + hatchling + editable 安装的技术栈约束。
---

# 项目目录架构技能

## 触发时机

1. **新建 Python 项目 / 生成骨架**：需要一次性产出标准目录树、根级依赖配置与测试配置时。
2. **新增文件定位**：需要判断新文件应归入哪个目录、采用什么名称时。
3. **重构目录**：需要调整既有目录结构、拆合模块或迁移文件时。

## 标准目录框架

```text
项目根/
├── MuLuJiaGouShuoMing.md          # 目录架构说明（含安装说明）
├── pyproject.toml                 # 项目定义与依赖声明
├── uv.lock                        # uv 锁定文件
├── .gitignore
├── HuanJingYiLai/                 # ② 环境依赖
│   ├── YunXingYiLai/              # 运行期依赖说明与辅助文件
│   ├── KaiFaYiLai/                # 开发期依赖说明与辅助文件
│   ├── HuanJingBianLiang/
│   │   └── .env.example           # 环境变量样例
│   └── rizhi.yaml                 # 日志配置值（置于本项根下）
├── XiangMuYuanMa/                 # ③ 项目源码根（不参与 import）
│   ├── app/                       # 可 import 的包根（小写拼音）
│   │   ├── mokuai_a/
│   │   ├── mokuai_b/
│   │   └── gongyong/
│   │       └── rizhi.py           # 日志模块
│   └── CeShi/                     # 测试目录，与 app/ 平级，不被 import
├── RiZhiWenJian/                  # ④ 日志文件（目录入库，内容不入库）
│   ├── .gitkeep
│   ├── GuiDang/                   # 归档目录
│   │   └── .gitkeep
│   └── YYYY-MM-DD/                # 运行时按日期生成的子目录（不入库）
│       ├── app.log
│       └── error.log
├── XiangMuBaoGao/                 # ⑤ 项目报告
│   ├── RenGongZhuanXie/           # 人工撰写，入库
│   └── ZiDongShengCheng/          # 自动生成，不入库，.gitkeep 占位
│       └── .gitkeep
└── XiangMuQiDongRuKou/            # ⑥ 启动入口
    ├── QiDongRuKou.py             # 唯一入口，--env 区分开发/生产
    ├── QiDong.sh
    └── QiDongCanShu.yaml          # 启动参数（YAML）
```

## 命名规则

- **一级项**：目录与说明文档一律大写拼音首字母（如 `HuanJingYiLai/`、`MuLuJiaGouShuoMing.md`）。
- **可 import 的包/模块**：小写拼音（`app/`、`mokuai_a/`、`gongyong/`）。
- **测试目录**：`CeShi/` 与 `app/` 平级，不参与 import。
- **非包目录**：日志、报告、启动入口用大写拼音（`RiZhiWenJian/`、`XiangMuBaoGao/`、`XiangMuQiDongRuKou/`）。

## 技术栈约束

- 单仓单项目；Python + uv + hatchling；`pyproject.toml` 与 `uv.lock` 放在项目根，`HuanJingYiLai/` 只放依赖说明与辅助文件。
- 包根为 `XiangMuYuanMa/app/`，以 editable 模式安装（乙方案）。

`pyproject.toml` 关键段：

```toml
[project]
name = "<项目名>"
version = "0.1.0"
dependencies = []

[dependency-groups]
dev = ["pytest", "pytest-html"]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["XiangMuYuanMa/app"]

[tool.pytest.ini_options]
testpaths = ["XiangMuYuanMa/CeShi"]
pythonpath = ["XiangMuYuanMa"]
```

入口文件 `XiangMuQiDongRuKou/QiDongRuKou.py` 直接引用已安装包，不做 `sys.path` 注入：

```python
from app.mokuai_a import <模块>
from app.gongyong.rizhi import <日志对象>
```

### 环境前置检查

- 生成项目前检查项目根路径是否纯 ASCII。
- 若含非 ASCII（中文/日文等）：Python 3.10–3.13 会在 `site.py` 因 locale(cp936) 读 `.pth` 触发 fatal；必须提示用户迁移到 ASCII 路径，或明确接受 `requires-python >=3.14` 的降级。
- 本项目现状：路径含中文，`requires-python >=3.14`，本条为记录性检查项。

## 使用规则

1. 先输出完整目录树，再生成文件；调整目录前先给出目标树。
2. 新增文件前，按 `references/directory-guide.md` 的「归属判定决策树」逐层定位；均不命中时询问用户，不自行造目录。
3. 新增目录必须同步登记 `references/directory-guide.md` 与 `MuLuJiaGouShuoMing.md`（后者由前者派生）。
4. 职责归属出现争议时，以 `references/directory-guide.md` 为准。
5. 生成后做六项自检：① 位置是否符合「归属判定决策树」的结论；② import 前缀是否为 `from app.`；③ 命名是否符合拼音规则；④ 测试是否同步放入 `CeShi/`；⑤ `.gitkeep` 与 `.gitignore` 是否一致；⑥ **文档已同步**：`references/directory-guide.md` 与 `MuLuJiaGouShuoMing.md` 均已登记新增模块/目录。第 ⑥ 项是规则第 3 条的闭环检查——第 3 条是"要做"，本项是"做完要验"。

## 维护依据

- 目录增删改：只改 `references/directory-guide.md` 与项目文档 `MuLuJiaGouShuoMing.md`，不动本文件。
- 一级项变化：才更新本文件的目录框架，并记录变更原因。
