# techulus/manage-prompt

⭐ 26 · JavaScript · MIT · 推送 2026-08-14 · [GitHub](https://github.com/techulus/manage-prompt) · [官网](https://manageprompt.com) · 组织维护

**本地 LLM 调用调试器：捕获开发期每次 LLM API 调用明细**

由 Go CLI 二进制与 npm 包组成：CLI 在本地运行服务器与 Web UI，npm 包以 wrapLanguageModel 中间件、capture() 包装或 log() 手动记录三种方式对应用插桩，捕获完整请求/响应体、工具调用流程可视化、延迟、token 用量与成本估算（基于 models.dev 定价）。数据经 POST /api/ingest 发送至本地服务器，存入 SQLite 并通过 WebSocket 实时更新界面。面向在开发阶段调试 LLM API 调用的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种插桩方式：AI SDK 中间件、capture() 自动包装、log() 手动记录
- 捕获完整请求/响应、token 用量、成本估算与延迟
- 本地 Go 服务器 + Web UI，数据存 SQLite，WebSocket 实时更新
- 兼容任意 AI SDK provider（OpenAI、Anthropic、Google、Mistral 等）

## 适用场景

- 开发调试 LLM 应用时查看每次调用的完整请求与响应
- 统计开发过程中的 token 消耗与成本
- 可视化追踪工具调用（tool call）流程

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: Local LLM call debugger. Captures every LLM API call during development with full request/response details, token us
> L9: - **CLI (Go binary)** — runs the local server and web UI for viewing captured requests
> L10: - **npm package** — instruments your app to capture and send LLM call data to the server

## 星数曲线

```mermaid
xychart-beta
    title "techulus/manage-prompt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `3cdcf4b2c027` · [字段定义](../../DATASET.md)*
