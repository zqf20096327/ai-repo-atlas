# openai/openai-go

⭐ 3,549 · Go · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/openai/openai-go) · 组织维护

**OpenAI API 的 Go 语言官方 SDK**

官方维护的 Go 库，为 Go 应用提供对 OpenAI REST API 的访问。覆盖 Responses API 的文本生成、多轮对话、流式输出、工具调用与结构化输出，并支持 Responses WebSockets 连接（含 lane、恢复、压缩机制）与 Realtime WebSockets 会话。要求 Go 1.26 及以上，旧 Go 版本需锁定历史 SDK 版本，js/wasm 环境下 WebSocket 连接不可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Responses API：文本生成、多轮对话、流式输出、工具调用、结构化输出
- Responses WebSockets 连接：lane 并发、token 刷新、显式恢复与重连
- Realtime WebSockets 会话支持
- 提供 api.md 的完整 API 参考与可运行示例

## 适用场景

- 在 Go 服务端集成 OpenAI 模型生成文本
- 构建需要流式输出与工具调用的 Go 应用
- 通过 WebSocket 维护多轮长连接对话

## 场景标签

 · 领域:LLM 基础设施/SDK

## 证据(README 行号)

> L5: The OpenAI Go library provides convenient access to the OpenAI REST API
> L6: from applications written in Go.

## 星数曲线

```mermaid
xychart-beta
    title "openai/openai-go 星数(近 20 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-13", "2026-11-14", "2026-11-16", "2026-11-19", "2026-11-20", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 3500 --> 3553
    line [3504, 3505, 3508, 3511, 3515, 3517, 3519, 3505, 3531, 3534, 3535, 3534, 3535, 3539, 3541, 3542, 3544, 3545, 3547, 3549]
```

2026-10-24 3,504 → 2026-11-26 3,549（+45）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `8b158c33e962` · [字段定义](../../DATASET.md)*
