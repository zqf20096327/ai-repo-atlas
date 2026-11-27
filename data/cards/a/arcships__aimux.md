# arcships/aimux

⭐ 295 · Rust · MIT · 推送 2026-11-26 · [GitHub](https://github.com/arcships/aimux) · 个人维护

**给开发者一套 Rust 统一 API，接入 329 家 LLM 服务商**

Rust 实现的统一 LLM 服务接入层，把各家服务商的 HTTP API 折叠为单一 `dyn LanguageModel` 接口，覆盖文本、流式、工具调用、嵌入、图像、语音、转录、视频、重排序等多模态操作。明确不做 agent 循环、RAG 或编排。内置 JSONL 请求录制与离线回放、路由回退与 MoA 组合模型、实时转录会话；通过 C ABI 提供 Node、Python、Swift、Kotlin、Flutter、Go、Java、C 共 8 种语言绑定，另附浏览器端模型调用测试控制台。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 329 个 provider 名称：282 个 OpenAI 兼容预设 + 47 个 vendor 包
- 支持实时 WebSocket 转录会话与 prompt-cache 命中追踪
- JSONL 录制/离线回放，测试无需网络与 API key（2,800+ cassettes）
- 单一 Rust 核心生成 8 种语言绑定

## 适用场景

- 在 Rust 或多语言项目中用同一接口调用多家 LLM 服务商
- 本地切换/回退 Ollama、vLLM 等本地引擎与云端服务商
- 录制请求响应用于回归测试与事后取证
- 在 Flutter 移动端嵌入统一的 LLM 调用能力

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L24: aimux is a Rust implementation of a unified LLM provider access layer. It
> L28: Unlike **rig** or **langchain**, aimux does **not** build agent loops, RAG, or
> L36: - **329 provider names** — 282 registry-backed OpenAI-compatible presets

## 星数曲线

```mermaid
xychart-beta
    title "arcships/aimux 星数(近 6 点)"
    x-axis ["2026-10-25", "2026-10-29", "2026-11-06", "2026-11-08", "2026-11-26", "2026-11-27"]
    y-axis "stars" 195 --> 304
    line [204, 205, 204, 243, 268, 295]
```

2026-10-25 204 → 2026-11-27 295（+91）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `a87ef1d5710d` · [字段定义](../../DATASET.md)*
