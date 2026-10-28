# liushuangls/go-anthropic

⭐ 175 · Go · Apache-2.0 · 推送 2026-09-21 · [GitHub](https://github.com/liushuangls/go-anthropic) · 个人维护

**非官方 Anthropic Claude API 的 Go 语言 SDK 封装库**

为 Go 开发者提供的 Anthropic Claude API 非官方封装库，以 Go 包形式分发，需 Go 1.21 及以上版本，通过 go get 安装。支持 Completions、Messages 及两者的流式输出、Message Batching、Vision 与 PDF 输入、Tool use（含 computer use）、Prompt Caching 与 Token Counting。内置 beta 特性标识常量与模型常量枚举，覆盖 Google Vertex AI 平台的接入方式，并列出各模型常量的活跃/弃用/退役状态供开发者查阅。Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 Messages/Completions 流式输出与 Message Batching
- Tool use（含 computer use）、Prompt Caching、Token Counting
- 内置 beta 特性标识常量与带退役状态标注的模型常量枚举
- 提供 Google Vertex AI 凭据接入示例

## 适用场景

- 在 Go 服务中集成 Claude Messages 与流式对话
- 实现带工具调用或计算机使用能力的 Claude 应用
- 通过 Vertex AI 平台调用 Claude 模型

## 场景标签

 · 领域:LLM 基础设施/API 客户端

## 证据(README 行号)

> L8: Anthropic Claude API wrapper for Go (Unofficial).
> L24: go get github.com/liushuangls/go-anthropic/v2

## 星数曲线

```mermaid
xychart-beta
    title "liushuangls/go-anthropic 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 173 --> 176
    line [174, 175, 175]
```

2026-10-18 174 → 2026-10-28 175（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `99b79a53e4ef` · [字段定义](../../DATASET.md)*
