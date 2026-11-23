# Mesh-LLM/mesh-llm

⭐ 4,198 · Rust · Apache-2.0 · 推送 2026-11-22 · [GitHub](https://github.com/Mesh-LLM/mesh-llm) · [官网](http://meshllm.cloud/) · 组织维护

**跨机器共享 GPU 组网为 OpenAI 兼容 API 的分布式 LLM 服务**

用 Rust 编写的分布式 LLM 服务工具：将多台机器的 GPU 与内存汇聚为一个 mesh，对外暴露统一的 OpenAI 兼容 API（默认端口 9337）。内含 Skippy 运行时负责模型管理与原生推理（llama.cpp 补丁运行时、GGUF），Mesh 层提供节点发现（Nostr 公开发现）、QUIC 加密传输、按 model 字段路由、层拆分执行与插件系统。单机可独立运行，大模型可用 stage splits 分片到多节点。支持 brew/安装脚本/多平台二进制包，源码构建需 just/cmake/Rust/Node.js。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多节点组网后对外暴露单一 OpenAI 兼容 API（localhost:9337）
- QUIC 端到端加密的节点间传输与 Iroh 中继
- 大模型 Skippy stage splits 层级拆分与 GGUF 分片包
- 支持 Qwen/Llama/DeepSeek/GLM 等 72 个 P0/P1 模型家族

## 适用场景

- 把家里几台机器的 GPU 拼起来跑单个大模型
- 在局域网内搭建私有推理服务给 agent 工具调用
- 通过公开 mesh 或邀请 token 与他人共享算力

## 场景标签

`推理引擎` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: Mesh LLM pools GPUs and memory across machines and exposes the result as one
> L6: OpenAI-compatible API at `http://localhost:9337/v1`. Start one node, add more
> L121: - **Mesh routing.** Every node exposes the same `/v1` API. Requests are routed

## 星数曲线

```mermaid
xychart-beta
    title "Mesh-LLM/mesh-llm 星数(近 28 点)"
    x-axis ["2026-10-21", "2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23"]
    y-axis "stars" 3459 --> 4265
    line [3526, 3533, 3542, 3546, 3551, 3552, 3556, 3558, 3590, 3633, 3676, 3703, 3747, 3551, 3985, 4034, 4070, 4094, 4099, 4107, 4123, 4138, 4151, 4163, 4172, 4181, 4189, 4198]
```

2026-10-21 3,526 → 2026-11-23 4,198（+672）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `f5c445a3ada6` · [字段定义](../../DATASET.md)*
