# 基线确认清单（S0 冻结版）

> 说明：本清单仅整理并冻结前序评审已定稿的决策，不新增规则、不新增目录、不重开设计讨论。全部条目的来源均为“前序评审确认”；凡输入未给出的内容，一律不作补充判断。

## 1. 技术栈与工程形态

| 项 | 内容 | 来源 | 状态 |
| --- | --- | --- | --- |
| 开发语言 | Python | 前序评审确认 | 已冻结 |
| 工程形态 | 单仓单项目（单一仓库、单一项目） | 前序评审确认 | 已冻结 |
| 依赖管理工具 | uv | 前序评审确认 | 已冻结 |
| 依赖声明与锁定文件位置 | `pyproject.toml` 与 `uv.lock` 放置在项目根 | 前序评审确认 | 已冻结 |
| `HuanJingYiLai/` 的边界 | 仅放置依赖说明与辅助文件，不承载 `pyproject.toml`、`uv.lock` | 前序评审确认 | 已冻结 |
| 构建后端与包发现 | hatchling；`packages = ["XiangMuYuanMa/app"]` | 前序评审确认 | 已冻结 |
| 安装方式 | editable 安装（乙方案） | 前序评审确认 | 已冻结 |
| 入口导入方式 | 入口不做 `sys.path` 注入 | 前序评审确认 | 已冻结 |
| pytest 测试路径 | `testpaths = ["XiangMuYuanMa/CeShi"]` | 前序评审确认 | 已冻结 |
| pytest 导入路径 | `pythonpath = ["XiangMuYuanMa"]` | 前序评审确认 | 已冻结 |

## 2. 目录结构

| 项 | 内容 | 来源 | 状态 |
| --- | --- | --- | --- |
| 一级项数量与位置 | 六个一级项全部位于项目根 | 前序评审确认 | 已冻结 |
| ① `MuLuJiaGouShuoMing.md` | 单文件；内容为目录架构说明，并含安装说明 | 前序评审确认 | 已冻结 |
| ② `HuanJingYiLai/` | 环境依赖一级项；内部含 `YunXingYiLai/`、`KaiFaYiLai/`、`HuanJingBianLiang/.env.example`，以及 `rizhi.yaml`（日志配置值，置于本项根下） | 前序评审确认 | 已冻结 |
| ③ `XiangMuYuanMa/` | 项目源码根，不参与 import；内含小写包根 `app/`（`mokuai_a/`、`mokuai_b/`、`gongyong/rizhi.py`）与平级 `CeShi/` | 前序评审确认 | 已冻结 |
| ④ `RiZhiWenJian/` | 日志文件一级项；目录入库（`.gitkeep`），内容不入库；扁平结构，按日期子目录 + 级别文件（`app.log`、`error.log`）；`GuiDang/` 用于归档 | 前序评审确认 | 已冻结 |
| ⑤ `XiangMuBaoGao/` | 项目报告一级项；`RenGongZhuanXie/` 入库；`ZiDongShengCheng/` 不入库，以 `.gitkeep` 占位 | 前序评审确认 | 已冻结 |
| ⑥ `XiangMuQiDongRuKou/` | 启动入口一级项；`QiDongRuKou.py`（唯一入口，`--env` 区分开发/生产）、`QiDong.sh`、`QiDongCanShu.yaml`（启动参数，YAML） | 前序评审确认 | 已冻结 |
| 测试目录位置 | `CeShi/` 与 `app/` 平级，不被 import | 前序评审确认 | 已冻结 |
| 包根层级 | `app/` 为可 import 的包根，位于 `XiangMuYuanMa/` 之下；`gongyong/` 为其内部公共模块包 | 前序评审确认 | 已冻结 |

## 3. 命名规则

| 项 | 内容 | 来源 | 状态 |
| --- | --- | --- | --- |
| 六个一级项命名 | 目录与说明文档均用拼音首字母大写（如 `HuanJingYiLai/`、`MuLuJiaGouShuoMing.md`） | 前序评审确认 | 已冻结 |
| 可 import 的包/模块命名 | 小写拼音（`app/`、`mokuai_a/`、`gongyong/`） | 前序评审确认 | 已冻结 |
| 非包目录命名 | 日志、报告、启动入口等非包目录用大写拼音 | 前序评审确认 | 已冻结 |
| 命名语种 | 一律使用已定稿的中文拼音命名，不改用英文 | 前序评审确认 | 已冻结 |
| 入口文件命名 | `QiDongRuKou.py`、`QiDong.sh`、`QiDongCanShu.yaml` 沿用拼音命名 | 前序评审确认 | 已冻结 |

## 4. 配置与依赖

| 项 | 内容 | 来源 | 状态 |
| --- | --- | --- | --- |
| 依赖清单 | `pyproject.toml`、`uv.lock` 位于项目根，由 uv 管理 | 前序评审确认 | 已冻结 |
| 包发现配置 | hatchling，`packages = ["XiangMuYuanMa/app"]` | 前序评审确认 | 已冻结 |
| 安装形态 | editable 安装（乙方案），入口不做 `sys.path` 注入 | 前序评审确认 | 已冻结 |
| 测试路径配置 | `testpaths = ["XiangMuYuanMa/CeShi"]`；`pythonpath = ["XiangMuYuanMa"]` | 前序评审确认 | 已冻结 |
| 环境变量样例 | `HuanJingYiLai/HuanJingBianLiang/.env.example` | 前序评审确认 | 已冻结 |
| 日志配置值 | `HuanJingYiLai/rizhi.yaml`，位于 `HuanJingYiLai/` 根下 | 前序评审确认 | 已冻结 |
| 启动参数 | `XiangMuQiDongRuKou/QiDongCanShu.yaml`，格式为 YAML | 前序评审确认 | 已冻结 |
| 依赖目录边界 | `HuanJingYiLai/` 只放依赖说明与辅助文件，依赖声明与锁文件仍留在项目根 | 前序评审确认 | 已冻结 |

## 5. 日志

| 项 | 内容 | 来源 | 状态 |
| --- | --- | --- | --- |
| 日志文件位置 | `RiZhiWenJian/` 一级项目录 | 前序评审确认 | 已冻结 |
| 入库策略 | 目录入库（`.gitkeep`），日志内容不入库 | 前序评审确认 | 已冻结 |
| 目录形态 | 扁平结构：按日期划分子目录，子目录内按级别输出文件 | 前序评审确认 | 已冻结 |
| 日志文件命名 | 级别文件为 `app.log`、`error.log` | 前序评审确认 | 已冻结 |
| 归档机制 | 由 `GuiDang/` 承担归档 | 前序评审确认 | 已冻结 |
| 保留策略 | 日志库按保留天数自动迁移至 `GuiDang/`（保留天数的具体数值未在输入中给出，作为 `rizhi.yaml` 配置值，不在本清单冻结范围） | 前序评审确认 | 已冻结 |
| 日志配置位置 | 配置值集中在 `HuanJingYiLai/rizhi.yaml` | 前序评审确认 | 已冻结 |
| 日志代码位置 | `XiangMuYuanMa/app/gongyong/rizhi.py` | 前序评审确认 | 已冻结 |

## 6. 报告

| 项 | 内容 | 来源 | 状态 |
| --- | --- | --- | --- |
| 报告根目录 | `XiangMuBaoGao/` 一级项目录 | 前序评审确认 | 已冻结 |
| 人工报告 | `RenGongZhuanXie/` 入库 | 前序评审确认 | 已冻结 |
| 自动报告 | `ZiDongShengCheng/` 不入库，以 `.gitkeep` 占位 | 前序评审确认 | 已冻结 |
| 自动产物类型 | pytest-html 生成的报告归入 `ZiDongShengCheng/`，不入库 | 前序评审确认 | 已冻结 |
| 人工文档归属 | 人工文档归 `RenGongZhuanXie/`；架构与安装说明归 `MuLuJiaGouShuoMing.md` | 前序评审确认 | 已冻结 |
| 不入库原则 | 自动生成的产物一律不入库 | 前序评审确认 | 已冻结 |

## 7. 启动

| 项 | 内容 | 来源 | 状态 |
| --- | --- | --- | --- |
| 启动目录 | `XiangMuQiDongRuKou/` 一级项目录 | 前序评审确认 | 已冻结 |
| 唯一入口 | `QiDongRuKou.py` 为项目唯一启动入口 | 前序评审确认 | 已冻结 |
| 环境区分 | 通过 `--env` 参数区分开发环境与生产环境 | 前序评审确认 | 已冻结 |
| Shell 启动脚本 | `QiDong.sh` | 前序评审确认 | 已冻结 |
| 启动参数文件 | `QiDongCanShu.yaml`，以 YAML 承载启动参数 | 前序评审确认 | 已冻结 |
| 入口约束 | 入口不做 `sys.path` 注入，依赖 editable 安装 | 前序评审确认 | 已冻结 |

## 8. 维护依据

| 项 | 内容 | 来源 | 状态 |
| --- | --- | --- | --- |
| 新增目录登记 | 新增目录必须在 `directory-guide.md` 与 `MuLuJiaGouShuoMing.md` 两处登记 | 前序评审确认 | 已冻结 |
| 技能文件变更范围 | 仅当一级项发生变化时才修改 `SKILL.md` | 前序评审确认 | 已冻结 |
| 变更追溯 | 所有结构性变更须留下记录并可追溯 | 前序评审确认 | 已冻结 |

## 9. 待决事项

| 编号 | 事项 | 为何无法在本阶段冻结 |
| --- | --- | --- |
| D-01（已决） | `directory-guide.md` 与 `SKILL.md` 的存放位置与归属，输入未给出 | 这两份文件不属于六个一级项，输入只规定了“新增目录须在其中登记”，未交代其位置与归属。若在 S0 自行指定位置，即属于新增决策，超出“只整理与冻结”的授权范围；故本阶段仅冻结登记义务本身，其文件位置待明确后再落实，不影响 S1–S5 对八类内容的执行 |

D-01 已于 S1 裁决并关闭：技能文件位于项目根 `.claude/skills/project-structure/`，含 `SKILL.md` 与 `references/directory-guide.md`；归属为进项目版本控制、团队共享。`directory-guide.md` 是目录职责维护源，`MuLuJiaGouShuoMing.md` 由其派生同步，`SKILL.md` 是触发入口与规则总纲。上表“为何无法在本阶段冻结”仅反映 S0 当时状态，现已解除。

## 10. 冻结声明

以上内容自本清单确认起冻结，S1–S5 阶段不得改动；如需变更，须走变更记录并注明原因。

## 变更记录

| 编号 | 日期 | 变更内容 | 原因 / 依据 |
| --- | --- | --- | --- |
| C-01 | 2026-11-08 | 补记技能文件位置与归属：`.claude/skills/project-structure/`，含 `SKILL.md` 与 `references/directory-guide.md`；进项目版本控制、团队共享。`directory-guide.md` 为维护源，`MuLuJiaGouShuoMing.md` 由其派生，`SKILL.md` 为触发入口与规则总纲 | S0 遗留缺口 D-01 已决 |
| C-02 | 2026-11-08 | S1 补建 `.claude/skills/` 工具层，并在 `references/directory-guide.md` 新增“工具层目录”一节完成登记；明确其为工具元数据、非业务结构、不计入六个一级项 | S1 偏差 D-02 收尾 |
| C-03 | 2026-11-08 | 补记 `__init__.py` 包标记规则：`app/` 及其每个子包目录需含 `__init__.py`（可空），用于 editable 安装与 pytest 导入稳定；标准目录树保持简洁，不在树内绘制该文件 | S1 偏差 D-03 收尾 |
| C-04 | 2026-11-08 | S0 清单归档至 `XiangMuBaoGao/RenGongZhuanXie/JiXianQueRenQingDan_S0.md`；移动前后 SHA-256 一致，正文内容未因移动改变 | S1 偏差 D-04 收尾（按方案 A） |
| C-05 | 2026-11-08 | `.gitignore` 补 `RiZhiWenJian/GuiDang/*` 与 `!RiZhiWenJian/GuiDang/.gitkeep`，修复归档目录内日志会被跟踪的缺陷 | S2 验收发现归档穿透 |
| C-06 | 2026-11-08 | `MuLuJiaGouShuoMing.md` 节结构以 S4 定稿为准；S2 骨架按提示词七节占位，S4 按 S0 八类落定，如需合并成七节须用户明示（本条仅记录，不追溯修改文件） | S2 D-05 属越界自合并，改由 S4 裁决 |
| C-07 | 2026-11-10 | ruff `N999` 定向豁免，仅 `XiangMuYuanMa/CeShi/**`，`app/` 不豁免 | S3-04 收尾：冻结命名要求包目录大写拼音，与 ruff 模块名规范冲突 |
| C-08 | 2026-11-10 | `requires-python` 由 `>=3.10` 收紧为 `>=3.14` | 项目路径含中文触发 Python ≤3.12 的 `site.py` cp936 fatal（S3-01），当前无法迁移路径，诚实声明 |
| C-09 | 2026-11-10 | 归档迁移逻辑 S3 已实现但未实测，列为 **S4 必测项**：临时 `retention_days=1` + 构造 2 天前目录 → `init_logging()` → 断言迁入 `GuiDang/` | S3-03 未闭环，S4 补验 |
| C-10 | 2026-11-10 | 本环境 pytest 统一用 `python -m pytest`（`pytest.exe` 被应用控制策略拦截，`os error 4551`）；S4 写入 `MuLuJiaGouShuoMing.md` 报告说明段 | S3-02 记录在案 |
| C-11 | 2026-11-10 | 技能层新增路径 ASCII 前置检查（`SKILL.md` 环境前置检查、guide 环境约束节）；决定：未来新项目强制，现有项目按 `requires-python >=3.14` 声明保持 | 来源 S3-01 中文路径致 `site.py` fatal |
| C-12 | 2026-11-10 | `.gitignore` 补 `.pytest_cache/`、`.ruff_cache/`、`.mypy_cache/`、`.coverage`、`htmlcov/`、`*.egg-info/`；实测 `git check-ignore` 六条均命中 | S4/P-06：S3 未覆盖常见缓存，`.pytest_cache/` 与 `.ruff_cache/` 实际存在且此前未被忽略 |
| C-13 | 2026-11-10 | 新增 `.gitattributes`（`* text=auto eol=lf`，甲方案）。`git add --renormalize .` 后 `git diff --cached --stat` 为**空**、`git diff --cached --ignore-cr-at-eol` 为**空**，即行尾规范化**零文件变更**（仓库索引原本已全 LF），故未产生 renormalize 提交；`.gitattributes` 自身以独立提交 `c09c82f` 落库（1 file changed, 1 insertion） | S5/Q2：行尾统一为 LF；首次 renormalize 无变更属预期 |
| C-14 | 2026-11-10 | 技能规则补强：guide 顶部新增归属判定决策树（P1）；SKILL R5 自检五项→六项，新增"文档已同步"（P2） | S5 反馈清单 P1/P2；决策树与职责表一一对应，无冲突 |
| C-15 | 2026-11-10 | SKILL.md R2 措辞由"按职责表定位"改为"按归属判定决策树定位"，与 guide 权威声明对齐；P1 正式闭环 | S6 遗留观察 O-1；不改其他规则，不改 guide |
