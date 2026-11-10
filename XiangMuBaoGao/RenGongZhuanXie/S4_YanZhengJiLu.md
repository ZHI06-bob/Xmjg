# S4 验证记录

日期：2026-11-10
阶段：S4 验证与文档冻结
环境：Windows 10/11 + PowerShell 5 + Python 3.14.8 + uv 0.13.7

## 一、归档迁移实测（P-03 / C-09）

验证目标：`init_logging()` 按 `retention_days` 把过期日期目录迁入 `RiZhiWenJian/GuiDang/`。

步骤与结果：

| 步骤 | 操作 | 实际结果 |
| --- | --- | --- |
| 1 | 临时将 `HuanJingYiLai/rizhi.yaml` 的 `retention_days` 改为 `1` | 已改，截止日为 2026-11-09 |
| 2 | 构造 `RiZhiWenJian/2026-11-08/app.log`（内容：`占位内容 S4 归档测试`） | 目录与文件创建成功 |
| 3 | 调用 `init_logging()` | 输出 `init_logging OK`，无异常 |
| 4 | 断言原目录不存在 | `RiZhiWenJian/2026-11-08` → False ✓ |
| 5 | 断言归档目录存在 | `RiZhiWenJian/GuiDang/2026-11-08` → True ✓ |
| 6 | 断言归档文件与内容完整 | `GuiDang/2026-11-08/app.log` → True，内容 `占位内容 S4 归档测试` ✓ |
| 7 | 恢复 `retention_days = 7` | 已恢复，`retention_days: 7` |
| 8 | 清理临时归档目录 | `GuiDang/2026-11-08` 已删除，`GuiDang/` 仅剩 `.gitkeep` |

结论：归档迁移逻辑正确，P-03 闭环。当日目录 `RiZhiWenJian/2026-11-10/` 未被误迁。

## 二、端到端全链路验证

干净环境：`uv sync --reinstall`（卸载 13 个包后重装 13 个包，2.66 秒）。

| # | 验证项 | 命令 | 结果 |
| --- | --- | --- | --- |
| 1 | 依赖同步 | `uv sync --reinstall` | ✓ `Installed 13 packages in 722ms`，`Resolved 13 packages` |
| 2 | 冒烟测试 | `uv run python -m pytest -q` | ✓ `2 passed in 0.11s` |
| 3 | 自动报告 | `uv run python -m pytest --html=XiangMuBaoGao/ZiDongShengCheng/ceShiBaoGao.html --self-contained-html` | ✓ 报告生成，33,940 字节 |
| 4 | 入口运行 | `bash XiangMuQiDongRuKou/QiDong.sh --env dev` | ✓ 退出码 0，输出 `env=dev / host=127.0.0.1 / port=8000 / workers=1` |
| 5 | 日志写入 | 读取 `RiZhiWenJian/2026-11-10/app.log` | ✓ 末行 `2026-11-10 18:24:48,571 INFO __main__ 启动入口 env=dev 参数={'host': '127.0.0.1', 'port': 8000, 'workers': 1}` |
| 6 | 日志被忽略 | `git check-ignore RiZhiWenJian/2026-11-10/app.log` | ✓ 退出码 0；`error.log` 同为 0 |
| 7 | 报告被忽略 | `git check-ignore XiangMuBaoGao/ZiDongShengCheng/ceShiBaoGao.html` | ✓ 退出码 0 |
| 8 | 占位可跟踪 | `git check-ignore` 三处 `.gitkeep` 与 `.env.example` | ✓ 均为退出码 1（未被忽略） |

## 三、缓存目录忽略（P-06 / C-12）

检查发现 `.pytest_cache/`、`.ruff_cache/` 存在于项目根且未被忽略，已补入 `.gitignore`：
`.pytest_cache/`、`.ruff_cache/`、`.mypy_cache/`、`.coverage`、`htmlcov/`、`*.egg-info/`。

实测 `git check-ignore`（退出码 0 表示命中）：

| 路径 | 退出码 |
| --- | --- |
| `.pytest_cache/README.md` | 0 ✓ |
| `.ruff_cache/CACHEDIR.TAG` | 0 ✓ |
| `.mypy_cache/x.json` | 0 ✓ |
| `.coverage` | 0 ✓ |
| `htmlcov/index.html` | 0 ✓ |
| `XiangMuYuanMa/app.egg-info/PKG-INFO` | 0 ✓ |

## 四、附带说明

- 归档迁移为真实执行，非推理结论。
- 本环境 `pytest` 统一以 `python -m pytest` 调用；`pytest.exe` 被应用控制策略拦截（`os error 4551`），已记入 C-10 与架构说明第 5 节。
- 技能触发验证（S1 遗留「未实测」项）仍未实测：当前运行环境为 TraeCode，不加载 `.claude/skills` 目录，且本机无 `claude` CLI。状态维持「未实测」，未改写为已验证。
