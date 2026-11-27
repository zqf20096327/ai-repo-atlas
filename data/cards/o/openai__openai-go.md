# openai/openai-go

⭐ 3,554 · Go · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/openai/openai-go) · 组织维护

**在 Go 应用中接入 OpenAI API 的官方 SDK**

OpenAI 官方 Go 库，通过封装 REST API 让 Go 应用调用 OpenAI 模型。提供 Responses API 文本生成、多轮对话、流式响应、工具调用、结构化输出，以及 Responses/Realtime 两类 WebSocket 连接（含 lane 路由、断线恢复、响应累积器与压缩续接）。要求 Go 1.26 及以上（含 HTTP/2 安全补丁版本），旧 Go 版本需固定旧 SDK 版本，旧版不再获得修复。

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

- Responses API：文本生成、多轮对话、流式响应、工具调用、结构化输出
- Responses 与 Realtime WebSocket 连接，支持 lane 路由与显式恢复
- ResponseAccumulator 增量快照与 DetailedSnapshot 元数据投影
- 上下文压缩（compaction）续接与服务限额处理

## 适用场景

- 在 Go 后端服务中调用 OpenAI 模型生成文本
- 构建需要流式输出与工具调用的对话应用
- 通过 WebSocket 维持长连接的多轮 Responses 会话

## 场景标签

 · 领域:LLM 基础设施/SDK

## 证据(README 行号)

> L5: The OpenAI Go library provides convenient access to the OpenAI REST API
> L16: 	"github.com/openai/openai-go/v3" // imported as openai
> L45: The primary API for interacting with OpenAI models is the Responses API. You can generate text from the model with 

## 星数曲线

```mermaid
xychart-beta
    title "openai/openai-go 星数(近 20 点)"
    x-axis ["2026-10-25", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-13", "2026-11-14", "2026-11-16", "2026-11-19", "2026-11-20", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 3501 --> 3558
    line [3505, 3508, 3511, 3515, 3517, 3519, 3505, 3531, 3534, 3535, 3534, 3535, 3539, 3541, 3542, 3544, 3545, 3547, 3549, 3554]
```

2026-10-25 3,505 → 2026-11-27 3,554（+49）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `6d7e3bd11b83` · [字段定义](../../DATASET.md)*
