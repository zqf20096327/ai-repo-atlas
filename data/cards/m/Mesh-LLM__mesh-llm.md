# Mesh-LLM/mesh-llm

⭐ 4,225 · Rust · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/Mesh-LLM/mesh-llm) · [官网](http://meshllm.cloud/) · 组织维护

**跨机器聚合 GPU 算力，对外暴露 OpenAI 兼容 API**

用 Rust 编写的分布式 LLM 服务程序，将多台机器的 GPU 与内存组成 mesh，统一暴露为 OpenAI 兼容 API（默认端口 9337），并附 Web 控制台（端口 3131）。内含 Skippy 运行时负责模型管理与原生推理（含修补版 llama.cpp），Mesh 层提供节点发现、QUIC 加密传输、路由与插件机制；单机可跑的模型本地执行，过大模型可用 Skippy stage splits 分层跨节点执行。发布版本预编译 CPU/CUDA/ROCm/Vulkan/Metal 等多后端二进制，亦可从源码构建。

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

- 跨节点池化 GPU/内存，暴露单一 OpenAI 兼容 /v1 API
- QUIC 端到端加密的节点间传输，Nostr 公共发现与邀请 token 加入
- Skippy stage splits 支持单机装不下的大模型分层执行
- 支持 GGUF 的多模型家族（Qwen、Llama、DeepSeek、GLM 等）及多模态分片

## 适用场景

- 把家里多台机器的闲置 GPU 拼成一个推理节点池
- 给 Claude Code/Goose/OpenCode 等 agent 提供本地 OpenAI 兼容端点
- 公开或私有发布 mesh，通过付费插件对外提供推理服务

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: Mesh LLM pools GPUs and memory across machines and exposes the result as one
> L6: OpenAI-compatible API at `http://localhost:9337/v1`. Start one node, add more
> L122: - **Mesh routing.** Every node exposes the same `/v1` API. Requests are routed

## 星数曲线

```mermaid
xychart-beta
    title "Mesh-LLM/mesh-llm 星数(近 27 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 3479 --> 4292
    line [3546, 3551, 3552, 3556, 3558, 3590, 3633, 3676, 3703, 3747, 3551, 3985, 4034, 4070, 4094, 4099, 4107, 4123, 4138, 4151, 4163, 4172, 4181, 4189, 4198, 4212, 4225]
```

2026-10-24 3,546 → 2026-11-26 4,225（+679）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `9224b5554b53` · [字段定义](../../DATASET.md)*
