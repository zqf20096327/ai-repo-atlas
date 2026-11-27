# Jason26214/omni-computer-use

⭐ 10 · Python · MIT · 推送 2026-09-19 · [GitHub](https://github.com/Jason26214/omni-computer-use) · [官网](https://pypi.org/project/omni-computer-use-mcp/) · 个人维护

**让 AI agent 控制 Windows 桌面的 MCP 服务器**

面向 Windows 的 computer-use MCP 服务器，以 Claude Desktop 内置桌面工具为参照实现 27 个同名工具并新增 2 个，提供截图、鼠标、键盘、多显示器控制。通过进程祖先自动识别宿主客户端，无需为各客户端单独配置。面向在 Claude Code CLI、Codex 等 MCP 客户端中使用 agent 的开发者，典型用途是让 agent 操作正在开发中的桌面应用。需 Windows 与 Python 3.11+，经 uvx 从 PyPI 一行命令安装；所有授权应用默认 full 权限，无权限 GUI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 29 个工具：27 个对齐 Claude Desktop computer-use，另含 deactivate 与 display_overview
- 启动时自动沿进程祖先识别宿主客户端，零配置适配多种 MCP 客户端
- 截图自描述所在显示器，支持多显示器切换与全屏总览图
- 键盘自伤防护：控制窗口持焦点时拦截 type/key

## 适用场景

- 让 agent 启动并操作我正在开发的桌面应用进行测试调试
- 在 Windows 上通过 Claude Code CLI 使用桌面控制能力
- 多显示器环境下让 agent 不迷失目标屏幕
- 通过 computer_batch 执行毫秒级间隔的连续 UI 操作

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L9: It works everywhere because it does not integrate with any of them. It is a plain MCP server. When it starts it walk
> L82: - **29 tools** — 27 matching Claude Desktop's computer-use, plus `deactivate` and `display_overview`; a dev `reload
> L33: Requires Windows and Python 3.11+ (uv / uvx fetch Python for you). The PyPI package name carries an `-mcp` suffix; 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `0fbb910c8c91` · [字段定义](../../DATASET.md)*
