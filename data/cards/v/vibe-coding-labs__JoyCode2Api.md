# vibe-coding-labs/JoyCode2Api

⭐ 216 · Go · Apache-2.0 · 推送 2026-07-14 · [GitHub](https://github.com/vibe-coding-labs/JoyCode2Api) · 组织维护 · 中文 README

**给开发者的代理：把 JoyCode 私有协议译成 Anthropic/OpenAI 兼容 API**

Go 编写的 API 协议翻译代理：读取京东 JoyCode（AI 编程助手）背后的模型（GLM、Kimi、MiniMax、豆包、Claude-Opus 等），对外同时暴露 Anthropic Messages 与 OpenAI Chat Completions 两套端点，使 Claude Code、Cursor、Codex 可直接调用。工具调用、SSE 流式、上下文截断均做翻译。自带 Web Dashboard 管理多 JD 账号（扫码/OAuth/手动，每账号独立 API Key）、查看用量与请求记录。前端打包进单文件 Go 二进制，支持 Docker 与系统服务部署。README 声明仅供个人学习研究、禁止商业转售，最多配置 10 个账号。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同时实现 Anthropic Messages 与 OpenAI Chat Completions 双协议
- Dashboard 支持扫码/OAuth/手动添加最多 10 个 JD 账号，每账号独立 API Key
- Tool Use、SSE 流式输出、智能上下文截断完整翻译
- 单文件 Go 二进制部署，纯 Go 驱动 SQLite 无需 C 工具链

## 适用场景

- 让 Claude Code / Cursor / Codex 通过标准协议调用 JoyCode 模型
- 多账号管理与用量、请求记录监控
- 在服务器上以 Docker 或系统服务长期运行代理

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L18: JoyCode（京东 AI 编程助手）背后挂了 GLM、Kimi、MiniMax、Doubao、Claude-Opus 等模型，但它的 API 是私有协议，主流编程工具接不上。JoyCode2Api 在中间做协议翻译，对外同时暴露
> L26: - **Anthropic Messages API** (`/v1/messages`) — Claude Code 走这个
> L27: - **OpenAI Chat Completions API** (`/v1/chat/completions`) — Cursor / Codex 走这个

## 星数曲线

```mermaid
xychart-beta
    title "vibe-coding-labs/JoyCode2Api 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-24"]
    y-axis "stars" 211 --> 217
    line [212, 213, 216, 216]
```

2026-10-18 212 → 2026-10-24 216（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `2124d1103a0e` · [字段定义](../../DATASET.md)*
