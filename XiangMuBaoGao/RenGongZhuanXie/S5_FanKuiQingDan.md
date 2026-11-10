# S5 反馈清单

日期：2026-11-10
阶段：S5 试运行与反馈闭环
范围：`project-structure` 技能规则在"真实新增模块"场景下的可操作性

> **本项为规则可操作性验证（手工流程模拟），非自动触发实测。**
> 自动触发受环境限制（TraeCode 不加载 `.claude/skills`、本机无 `claude` CLI），已列为已知交付限制。

## 4.1 规则可操作性

评估对象：`.claude/skills/project-structure/SKILL.md` 第 100–106 行「使用规则」五条。

| 规则编号 | 规则摘要（行号） | 评估 | 证据 | 建议 |
| --- | --- | --- | --- | --- |
| R1 | 先输出完整目录树，再生成文件（L102） | 可落地·轻微含糊 | 本次先输出 `app/shili/{__init__.py,demo.py}` + `CeShi/test_shili.py` 增量树，再落盘，顺序可执行 | "完整"未界定范围：写全项目 155 行树成本高，建议明确为"涉及的一级项子树" |
| R2 | 新增文件前先查 guide 并按职责表定位（L103） | 可落地·有缺失 | 实读 guide L20（`app/` 行"放：业务包与公共模块"）即判定 `app/shili/`，无需额外推理 | guide 只有职责表、**无决策树条目**；"按决策树哪一层命中"只能由职责表 + 命名规则推定，建议补三层判定路径 |
| R3 | 新增目录同步登记 guide 与 `MuLuJiaGouShuoMing.md`（L104） | 可落地·已执行 | guide 新增 L23 一行（四列齐全）；`MuLuJiaGouShuoMing.md` L42–44 树、L51 `test_shili.py`、L84 命名说明；两者内容不重复、不冲突 | 未规定两份文档的登记粒度（guide 四列 vs 文档树+一句），建议写明"文档侧只需树 + 一行说明" |
| R4 | 职责争议以 guide 为准（L105） | 可落地·本次未触发 | 试运行全程无归属分歧，未产生需要仲裁的条目 | 无需修改；建议在 guide 增补归属判定路径后，本条才真正有裁决对象 |
| R5 | 生成后五项自检（L106） | 可落地·有缺失 | 逐项执行：①位置=`app/shili/` 且 guide L23 已登记；②import 前缀=`from app.shili.demo import demo`（test_shili.py L3），`demo.py` 无跨包导入；③命名=`shili` 小写拼音；④测试已入 `CeShi/test_shili.py`，`3 passed`；⑤`.gitkeep`/`.gitignore` 无变动且三处占位仍可跟踪 | 自检五项未含"两份文档已同步"，与 R3 存在漏检风险；建议增补为第 6 项 |

汇总：可落地 5/5；含糊 2 处（R1、R3）；缺失 2 处（R2 决策树、R5 文档同步自检）；矛盾 0 处。

## 4.2 摩擦点

| # | 场景 | 现象 | 是否本阶段处理 |
| --- | --- | --- | --- |
| F1 | `.gitattributes` 生效验证（终态校验） | `git add --renormalize .` 后暂存区为空，无法借 diff 证明 `eol=lf` 真的生效 | 已处理：改用 `git check-attr`（`text: auto`、`eol: lf` 三例均命中）+ 工作区字节统计（`CR_COUNT=0`）取证 |
| F2 | PowerShell 下 `git add --renormalize .` | 命令无任何输出，无法判断是否执行成功 | 已处理：按任务要求做双检查（`--stat` 空、`--ignore-cr-at-eol` 空） |
| F3 | 归属判断（步骤 1） | 任务书要求说明"决策树哪一层命中"，但 guide 无决策树，只有职责表 | 未处理：需改技能规则，超出 S5 授权；记入改进项 P1 |
| F4 | 提交次数 vs 最终 clean | 行尾提交、示例模块提交完成后，C-13 与本草单才产出，需第 3 次业务提交（全仓共 4 次） | 未处理：未 amend 已提交历史（避免改写历史），如实记录为偏差 S5-02 |
| F5 | 示例模块被 git 识别为空文件 | `app/shili/__init__.py` 在 `--stat` 中显示 1 insertion（空行），易被误判为"非空" | 已处理：确认为 git 对空文件的标准表示，未做改动 |

## 4.3 改进项

按优先级排序（P1 最高）：

| 优先级 | 改进项 | 处置 |
| --- | --- | --- |
| P1 | `references/directory-guide.md` 增补"新增内容归属判定路径"：一级项 → 包根 `app/` → 子包（业务模块 / 公共模块 / 示例）三层，明确每层的命中条件 | **下阶段修**（改技能规则须用户裁决） |
| P2 | `SKILL.md` 使用规则 R5 自检五项增补第 6 项"两份文档已同步" | **下阶段修**（改冻结技能文件须用户裁决） |
| P3 | R1 将"完整目录树"明确为"涉及的一级项子树"，避免每次新增都重排全树 | **下阶段修** |
| P4 | 行尾规范验证步骤固定为"双检查 + `git check-attr`"，写入手工流程基线 | **本阶段修**（仅记录验证方法，不改规则文件） |
| P5 | `MuLuJiaGouShuoMing.md` 明确"文档侧登记粒度 = 树 + 一行说明"，与 guide 四列表区分 | **下阶段修** |
| P6 | Windows 行尾（CRLF 检出）、TraeCode 不加载 `.claude/skills`、`pytest.exe` 被应用控制策略拦截、无系统 `bash` | **已知限制不修**（环境/平台约束） |

## 4.4 已知交付限制

1. **M2b 自动触发未实测**：环境为 TraeCode，不加载 `.claude/skills` 目录，本机亦无 `claude` CLI，无法产生真实自动触发记录；本次以手工按 `SKILL.md` 走完整流程替代。该替代**不等于**自动触发验证通过。
2. **项目路径含非 ASCII**：`d:\Nemo\...\技能包\Xmjg`，Python 3.10–3.13 的 `site.py` 以 locale(cp936) 读 `.pth` 会 fatal，故 `requires-python` 被迫收紧为 `>=3.14`（C-08/C-11）。
3. **首次 renormalize 零变更属预期**：仓库索引原本即全 LF，`git diff --cached --stat` 与 `--ignore-cr-at-eol` 均为空（C-13）；`.gitattributes` 本身已落库，后续跨平台检出将由 `eol=lf` 统一。
4. **pytest 调用方式**：`pytest.exe` 被应用控制策略拦截（`os error 4551`），统一使用 `uv run python -m pytest`（C-10）。
5. **启动脚本执行方式**：系统 PATH 无 `bash`，需用 Git Bash 绝对路径 `C:\Program Files\Git\bin\bash.exe` 调用 `QiDong.sh`。
6. **ruff `N999` 定向豁免**：`CeShi/` 依冻结命名规则须为包，与 ruff 模块名规范冲突，已仅在 `CeShi/**` 豁免（C-07）。
