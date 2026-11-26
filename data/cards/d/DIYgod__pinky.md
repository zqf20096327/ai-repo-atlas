# DIYgod/pinky

⭐ 2,782 · Go · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/DIYgod/pinky) · 个人维护 · 中文 README

**让 MCP agent 在你监督下操作 iPhone/Android 手机**

Pinky 是一个跨平台桌面应用，通过 MCP 让 Claude Code、Claude Desktop、Codex、Cursor 或任意脚本 agent 操作真实的 iPhone 或 Android 手机：用户在电脑上观看镜像、批准风险步骤（支付、发送、删除等默认等待确认）、随时接管并查看含截图与录屏的分步记录。安全规则在 Pinky 网关侧强制执行，agent 无法自我批准；银行/钱包类应用默认不可见。手机端 App 可脱离电脑独立执行任务，支持 DeepSeek、Qwen、Kimi、GLM、Claude、GPT、Gemini 及 Ollama/LM Studio 本地模型。当前为 pre-alpha 状态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- 通过 MCP 接入任意 agent，桌面覆盖 macOS/Windows/Linux
- 网关侧强制审批：支付、发送、删除等操作等待用户确认
- Android 13+ 支持隐藏第二屏幕，agent 与用户互不干扰
- 手机端 App 无需电脑，可选多模型独立执行任务

## 适用场景

- 让 Claude Code 等 agent 代我在手机上完成操作并逐步审批
- 手机不在身边时通过电脑远程操作手机
- 定时执行手机任务并在条件满足时收到通知

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L7: Pinky lets any agent (Claude Code, Claude Desktop, Codex, Cursor or a script) operate a real iPhone or Android phone
> L11: - **Any agent, one click.** Settings › Agents connects Claude Code, Claude Desktop, Codex, Cursor and more, and any

## 星数曲线

```mermaid
xychart-beta
    title "DIYgod/pinky 星数(近 12 点)"
    x-axis ["2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 2008 --> 2852
    line [2078, 2139, 2208, 2287, 2373, 2458, 2535, 2585, 2637, 2675, 2717, 2782]
```

2026-11-13 2,078 → 2026-11-26 2,782（+704）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `a73cab34e7ba` · [字段定义](../../DATASET.md)*
