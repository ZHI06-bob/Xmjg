# 目录职责维护表

> 本文件是项目目录职责的**维护源**；项目根的 `MuLuJiaGouShuoMing.md` 由本文件派生同步，二者不一致时以本文件为准。

## 目录职责表

| 目录/文件 | 职责 | 放什么 / 不放什么 | 维护规则 |
| --- | --- | --- | --- |
| `MuLuJiaGouShuoMing.md` | 项目目录架构说明（含安装说明） | 放：架构树、目录职责、安装步骤；不放：临时笔记、自动生成报告 | 架构变化后由本表派生同步 |
| `pyproject.toml` | 项目定义、依赖、构建与 pytest 配置 | 放：project 元数据、dependencies、dev 组、hatch packages、pytest 配置；不放：密钥、环境变量真实值 | 依赖或配置变更时同步本表 |
| `uv.lock` | uv 依赖锁定文件 | 放：uv 生成的锁定结果；不放：手写内容 | 仅由 uv 生成或更新 |
| `.gitignore` | 版本控制忽略规则 | 放：日志内容、自动报告等不入库路径；不放：应入库的源码与配置 | 与 `.gitkeep` 占位保持一致 |
| `HuanJingYiLai/` | 环境依赖一级项 | 放：依赖说明与辅助文件；不放：`pyproject.toml`、`uv.lock` | 一级项，变化时才改 `SKILL.md` |
| `HuanJingYiLai/YunXingYiLai/` | 运行期依赖说明与辅助文件 | 放：运行期依赖清单与说明；不放：开发期依赖、日志 | 内容变更时同步本表 |
| `HuanJingYiLai/KaiFaYiLai/` | 开发期依赖说明与辅助文件 | 放：开发与测试工具依赖说明；不放：运行期依赖 | 内容变更时同步本表 |
| `HuanJingYiLai/HuanJingBianLiang/` | 环境变量配置目录 | 放：环境变量样例与说明；不放：真实密钥、实际 `.env` | 变量增删时同步本表 |
| `HuanJingYiLai/HuanJingBianLiang/.env.example` | 环境变量样例 | 放：键名与示例值；不放：真实凭据 | 变量增删时同步本表 |
| `HuanJingYiLai/rizhi.yaml` | 日志配置值 | 放：日志级别、路径、保留天数等配置值；不放：代码逻辑 | 配置变更时同步本表 |
| `XiangMuYuanMa/` | 项目源码根，不参与 import | 放：`app/` 与 `CeShi/`；不放：依赖配置、日志、报告、启动脚本 | 一级项，变化时才改 `SKILL.md` |
| `XiangMuYuanMa/app/` | 可 import 的包根 | 放：业务包与公共模块；不放：测试代码、非代码文件 | 保持小写拼音命名；`app/` 及其每个子包目录需含 `__init__.py`（可空），用于 editable 安装与 pytest 导入稳定 |
| `XiangMuYuanMa/app/mokuai_a/` | 业务模块 A | 放：A 域业务代码；不放：跨模块通用逻辑（归 `gongyong/`） | 新增子包须登记；需含 `__init__.py`（可空） |
| `XiangMuYuanMa/app/mokuai_b/` | 业务模块 B | 放：B 域业务代码；不放：跨模块通用逻辑（归 `gongyong/`） | 新增子包须登记；需含 `__init__.py`（可空） |
| `XiangMuYuanMa/app/gongyong/` | 公共模块包 | 放：跨模块复用代码；不放：具体业务逻辑 | 新增子包须登记；需含 `__init__.py`（可空） |
| `XiangMuYuanMa/app/gongyong/rizhi.py` | 日志模块 | 放：日志初始化与写入封装；不放：业务处理 | 日志机制变更时同步本表 |
| `XiangMuYuanMa/CeShi/` | 测试目录 | 放：pytest 测试；不放：业务代码、运行期资源 | 与 `app/` 平级，不被 import；含 `__init__.py`（可空），用于 pytest 包结构一致与同名测试模块导入稳定 |
| `RiZhiWenJian/` | 日志文件目录 | 放：日期子目录与级别文件、`GuiDang/`；不放：源码、报告 | 目录入库，内容不入库 |
| `RiZhiWenJian/GuiDang/` | 日志归档目录 | 放：超过保留天数而迁移的日志；不放：当前日志 | 归档策略变更时同步本表 |
| `RiZhiWenJian/YYYY-MM-DD/` | 按日期生成的日志子目录 | 放：`app.log`、`error.log`；不放：人工文档 | 运行时生成，不入库 |
| `XiangMuBaoGao/` | 项目报告一级项 | 放：人工与自动报告；不放：源码、日志 | 一级项，变化时才改 `SKILL.md` |
| `XiangMuBaoGao/RenGongZhuanXie/` | 人工撰写报告 | 放：人工报告与文档；不放：pytest-html 等自动产物 | 入库 |
| `XiangMuBaoGao/ZiDongShengCheng/` | 自动生成报告 | 放：pytest-html 等自动产物；不放：人工文档 | 不入库，保留 `.gitkeep` 占位 |
| `XiangMuQiDongRuKou/` | 启动入口一级项 | 放：入口脚本与启动参数；不放：业务代码 | 一级项，变化时才改 `SKILL.md` |
| `XiangMuQiDongRuKou/QiDongRuKou.py` | 唯一启动入口 | 放：装配与启动逻辑；不放：业务实现 | 唯一入口，`--env` 区分开发/生产 |
| `XiangMuQiDongRuKou/QiDong.sh` | Shell 启动脚本 | 放：调用入口的脚本；不放：业务逻辑 | 变更时同步本表 |
| `XiangMuQiDongRuKou/QiDongCanShu.yaml` | 启动参数 | 放：启动参数配置；不放：密钥 | 参数变更时同步本表 |

## 工具层目录

> 工具元数据，非业务结构，不计入六个一级项。

| 目录/文件 | 职责 | 放什么 / 不放什么 | 维护规则 |
| --- | --- | --- | --- |
| `.claude/skills/project-structure/` | 团队共享技能目录（进项目版本控制） | 放：`SKILL.md` 与 `references/directory-guide.md`；不放：业务代码、运行期产物 | 技能文件变更须同步 S0 变更记录 |
| `.claude/skills/project-structure/SKILL.md` | 技能触发入口与规则总纲 | 放：触发时机、标准目录框架、命名规则、技术栈约束、使用规则、维护依据；不放：目录职责明细（归 guide） | 技能文件变更须同步 S0 变更记录 |
| `.claude/skills/project-structure/references/directory-guide.md` | 目录职责维护源 | 放：目录职责表、工具层登记、维护依据；不放：`MuLuJiaGouShuoMing.md` 副本 | 技能文件变更须同步 S0 变更记录 |

## 环境约束

- 项目根路径必须纯 ASCII；含非 ASCII 时 Python 3.10–3.13 会因 `site.py` 以 locale(cp936) 读 `.pth` 而 fatal。
- 本项目现状：路径含中文，`requires-python >=3.14`。

## 维护依据

1. 新增目录必须登记于本表，未登记不得创建。
2. 一级项增删：同步更新本表的结构与 `SKILL.md`，并注明变更原因。
3. 配置或依赖变更：同步更新本表对应行。
