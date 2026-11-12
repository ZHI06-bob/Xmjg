
# 项目工程架构技能 (Project Architecture Skill)
这是一个用于**规范化项目初始化**与**代码文件归属**的 AI 技能包。当要求 AI 新建 Python 项目、生成骨架、或询问“某个文件该放哪”时，该技能会自动激活，强制输出统一的六项一级目录框架与规范的代码结构。

## ✨ 核心特性

- **六项一级框架**：强制统一 `目录说明`、`环境依赖`、`项目源码`、`日志文件`、`项目报告`、`启动入口` 的顶层结构。
- **拼音命名规范**：一级目录与非包文件使用拼音首字母大写（如 `XiangMuYuanMa/`），可被 Python import 的包/模块使用小写拼音（如 `app/`、`mokuai_a/`）。
- **现代 Python 技术栈**：内置 `uv` 依赖管理、`hatchling` 构建、editable 安装模式、`pytest` 测试，以及统一的日志分流（按日期/级别）。
- **归属判定决策树**：内置 9 层归属判定逻辑，AI 遇到新文件时不再乱建目录，找不到归属会主动询问。
- **环境前置检查**：自动识别并警告纯 ASCII 路径要求（规避 Python ≤3.12 在中文路径下的 `site.py` fatal 问题）。
- **六项生成后自检**：AI 生成完毕后，必须自检位置、import 前缀、命名、测试同步、忽略规则及**双文档同步**。

## 📂 技能包目录结构

本技能包严格按照平台要求打包，解压后应包含：

```text
project-structure/
├── SKILL.md                    # 技能触发入口与规则总纲 (核心)
└── references/
    └── directory-guide.md      # 目录职责维护源 (含归属判定决策树)
```

## 🚀 如何安装使用 (以 Trae/Claude 等平台为例)

1. **打包技能**：将 `project-structure` 整个文件夹压缩为 `project-structure.zip`。
   * *注意：ZIP 包内部的第一层必须是 `project-structure/` 文件夹，`SKILL.md` 必须在该文件夹内。*
2. **上传解析**：在平台的“创建技能”面板中，上传该 ZIP 包，等待系统自动解析。
3. **确认保存**：核对系统提取的 `name`（应为 `project-structure`）和 `description`，确认保存并启用。
4. **触发测试**：在新会话中输入“帮我新建一个 Python 项目”，AI 应自动输出六项一级框架的目录树。

## 📁 生成的工程骨架示例

当技能被触发时，AI 会生成如下标准结构（以英文或拼音命名替换 `XiangMuYuanMa` 等为例）：

```text
project-root/
├── MuLuJiaGouShuoMing.md       # 目录架构说明（含安装/启动指南）
├── HuanJingYiLai/              # 环境依赖（YunXingYiLai/、KaiFaYiLai/、环境变量模板、日志配置）
├── XiangMuYuanMa/              # 源码根
│   ├── app/                    # 包根 (editable 安装)
│   │   ├── mokuai_a/           # 业务模块
│   │   └── gongyong/rizhi.py   # 通用组件/日志装配
│   └── CeShi/                  # 测试目录 (pytest 收集)
├── RiZhiWenJian/               # 运行时日志 (按日期/级别分文件，内容不入库)
├── XiangMuBaoGao/              # 报告 (人工文档入库，自动测试报告不入库)
├── XiangMuQiDongRuKou/         # 启动入口 (QiDongRuKou.py / --env 参数)
├── pyproject.toml / uv.lock
└── .gitignore
```

## 🛠️ 维护指南 (For Maintainers)

本技能包的维护遵循“单一数据源”原则，请勿随意更改结构：
- **规则总纲**：修改 `SKILL.md`。仅当顶层目录结构发生重大增减时修改。
- **目录细则与决策树**：修改 `references/directory-guide.md`。日常新增目录职责、调整归属判定逻辑，请只改这里。
- **同步要求**：生成的项目根目录下的 `MuLuJiaGouShuoMing.md` 是派生物，修改技能规则后，需提醒用户同步更新其项目内的说明文档。

## ⚠️ 常见问题 (FAQ)

**Q: 为什么生成的代码里统一用 `python -m pytest`，而不是直接 `pytest`？**
A: 在部分 Windows 环境下（如应用控制策略限制），直接调用 `.venv\Scripts\pytest.exe` 会报 `os error 4551` 拒绝访问。使用 `python -m pytest` 可完美绕过此限制。

**Q: 为什么在中文路径（如 `D:\技能包\demo`）下运行会报错？**
A: Python 3.10~3.13 的 `site.py` 在以 `cp936` (GBK) 编码读取 `.pth` 文件时，遇到中文路径会直接 Fatal 崩溃。请将项目移至纯 ASCII 路径（如 `C:\PythonProjects\demo`），或使用 Python 3.14+。

**Q: 技能解析时提示“zip文件应包含带有 SKILL.md 的文件夹”怎么办？**
A: 请确保你是右键压缩了 `project-structure` 这个文件夹，而不是全选了里面的 `SKILL.md` 和 `references` 再压缩。ZIP 解压后必须有一层文件夹壳。
```

---

### 使用建议：
你可以将这份 README 放在**存放该技能源码的仓库根目录**。如果你打算把它作为模板发给团队的其他成员，这份文档能让他们在 3 分钟内搞懂这个技能是用来干嘛的、怎么打包上传、以及生成的代码长什么样。
