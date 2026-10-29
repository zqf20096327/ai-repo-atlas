# bpbonker/npurun

⭐ 34 · Rust · Apache-2.0 · 推送 2026-07-23 · [GitHub](https://github.com/bpbonker/npurun) · [官网](https://github.com/bpbonker/hexrun) · 个人维护

**面向骁龙 X 系列 Windows-on-ARM 笔记本的 NPU 本地 LLM 运行时**

用 Rust 封装 Qualcomm Genie SDK/QNN，使 Snapdragon X 系列的 Hexagon NPU 可用于本地 LLM 推理。提供 Ollama 风格 CLI（pull/run/serve/bench/ps）与 OpenAI、Ollama 兼容的 HTTP 服务器，内置模型注册表支持 sha256 校验与断点续传下载，多轮对话基于 Genie KV-cache rewind。限制：仅支持 Windows 11 24H2+ ARM64 与骁龙 X 系列硬件，需手动安装不可再分发的 QAIRT SDK 及 Rust/MSVC 工具链，通过 cargo 从源码构建；并发请求按单许可串行，超出返回 HTTP 429。自述状态为 working preview。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- OpenAI 与 Ollama 兼容 HTTP 服务器（SSE/NDJSON 流式、CORS、bearer 认证）
- 内置模型注册表：sha256 校验、可续传下载、自动注入多图切换配置
- 多轮对话经 Genie KV-cache rewind 只对新 token 付 prefill 成本
- 提供三种独立方法核验是否真实运行在 NPU 上（非 CPU 回退）

## 适用场景

- 在骁龙 X Elite 笔记本上让本地 LLM 跑在 Hexagon NPU 而非 CPU
- 用现有 OpenAI/Ollama 客户端（如 Open WebUI）接入局域网内的 NPU 推理服务
- 以 Rust 库形式把 Genie NPU 推理嵌入自己的项目

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L14: **npurun is the open Rust path.** Same Genie SDK that Qualcomm's own
> L16: `serve` / `bench` / `ps`) and an OpenAI- and Ollama-compatible HTTP
> L66: |**npurun**|NPU (Genie, native Rust FFI)|MIT / Apache-2.0|Open Rust crate, embeddable as a library; doesn't gate on

## 星数曲线

```mermaid
xychart-beta
    title "bpbonker/npurun 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-29"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-29 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c0e94b123479` · [字段定义](../../DATASET.md)*
