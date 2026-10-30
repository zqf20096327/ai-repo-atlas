# ybouane/dash-p

⭐ 23 · TypeScript · 推送 2026-09-11 · [GitHub](https://github.com/ybouane/dash-p) · [官网](https://ybouane.com/) · 个人维护

**让开发者以脚本驱动真实 Claude Code TUI 会话的 CLI/TS 库**

CLI 与 TypeScript 库，通过伪终端启动官方 claude 命令的交互式 TUI，以程序化方式注入输入、经无头终端模拟器读取渲染屏幕，并抽取为文本或与 @anthropic-ai/claude-agent-sdk 形状一致的结构化消息（含 tool_use/tool_result）。不绕过认证、不伪造请求，非 Claude Code 替代品。屏幕抓取受渲染保真上限约束（按 Claude Code 2.1.x 校准），可选用 --enrich-from-session 从磁盘会话转录读取精确文本。需本机已安装并登录官方 claude CLI，Node ≥ 20。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- PTY 驱动真实 claude TUI，注入输入并读取输出
- query() 接口与 @anthropic-ai/claude-agent-sdk 形状一致，代码可迁移
- TUI 识别规则存放于版本化 profiles/，支持新版本自校准
- --enrich-from-session 可从会话转录读取精确文本与 token 用量

## 适用场景

- 在脚本/流水线中以可组合方式调用本机 Claude Code 会话
- 把使用 claude-agent-sdk query() 的代码切换到 TUI 驱动方式
- 以 CLI 替代 claude -p 获得交互式会话的可编程接口

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L14: dash-p is a CLI and TypeScript library that makes Claude Code scriptable by driving the real Claude TUI process you
> L94: The `query()` shape matches `@anthropic-ai/claude-agent-sdk`, so code ports over:

## 星数曲线

```mermaid
xychart-beta
    title "ybouane/dash-p 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b7ff73ec3856` · [字段定义](../../DATASET.md)*
