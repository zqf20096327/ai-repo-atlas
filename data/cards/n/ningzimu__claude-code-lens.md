# ningzimu/claude-code-lens

⭐ 31 · JavaScript · 推送 2026-05-17 · [GitHub](https://github.com/ningzimu/claude-code-lens) · 个人维护 · 中文 README

**给 Claude Code 用户的本地流量监控代理，浏览器中查看提示词与调用记录**

在 Claude Code 与上游服务之间运行 Anthropic 兼容代理，记录系统提示词、消息历史、工具定义、工具调用、流式响应与 token 用量，并在浏览器可视化界面中检视。支持两种模式：cclens 一次性启动带监控的 Claude Code 会话（不修改其设置文件），或 cclens proxy 长期运行代理并通过 settings.json 或环境变量接入。另含 cclens trace 命令行会话追踪导出、附带的 Claude Code Skill 供 agent 自主分析，敏感请求头在日志中脱敏。运行数据存储于 ~/.claude-code-lens/。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Anthropic 兼容本地代理，记录系统提示词、消息、工具定义、工具调用与流式响应
- 一次性模式不修改 Claude Code 设置，参数透传；长期模式通过生成的 settings.json 接入
- 浏览器可视化界面按输入上下文、模型输出与资源拆分每个请求
- cclens trace 支持无浏览器的会话检索、Lead/Subagent 检查与 Markdown 导出

## 适用场景

- 调试 Claude Code 发出的提示词、工具与 MCP 定义
- 持续监控 Claude Code 会话的 token 用量与 API 交互
- 分析多 agent 会话行为并导出 Markdown 报告

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L7: Claude Code Lens is a local observability tool for Claude Code. It runs an Anthropic-compatible proxy between Claude
> L161: |`cclens trace`|Lists, inspects, and exports session traces without the browser UI|Find a session by ID or time cl

## 星数曲线

```mermaid
xychart-beta
    title "ningzimu/claude-code-lens 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-28 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5d8dc2bb9359` · [字段定义](../../DATASET.md)*
