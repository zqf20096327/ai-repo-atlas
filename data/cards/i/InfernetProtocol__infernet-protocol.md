# InfernetProtocol/infernet-protocol

⭐ 31 · JavaScript · ISC · 推送 2026-10-28 · [GitHub](https://github.com/InfernetProtocol/infernet-protocol) · [官网](https://infernetprotocol.com) · 组织维护

**P2P 分布式 GPU 推理算力市场协议，跑在 c0mpute 之上**

构建在 c0mpute P2P 基座（libp2p Kad-DHT + gossipsub）之上的去中心化 GPU 算力市场：GPU 节点安装 infernet 插件后以 Nostr 签名（secp256k1/BIP-340）注册并承接推理、批量任务（嵌入/分类）、LoRA 微调与异步分布式训练；提供 chat/completions API、流式聊天 playground、多引擎适配（Ollama、vLLM、Mojo+MAX）与多币种加密支付。控制面为 Next.js 仪表盘 + Supabase，可自托管或用官方云。定位为无需 NVLink 的单卡 7B–70B 推理与请求级并行市场，不覆盖紧耦合 100B+ 从头训练。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | ISC |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GPU 节点以 Nostr 签名请求认证，节点不持有数据库凭证、可仅出站运行
- 多引擎推理适配：Ollama / vLLM / Mojo+MAX（IPIP-0009），支持 Ray 多机多卡 vLLM
- 批量任务分解 fan-out 到多个提供方（IPIP-0013），训练编排包含 DeepSpeed/OpenRLHF/OpenDiLoCo/Petals 后端
- 一键 GPU 部署：铸造 24h bearer 后一行 user-data 完成安装注册，兼容 RunPod/Vast.ai/Lambda 等

## 适用场景

- 把闲置 GPU 服务器接入推理市场赚取加密货币
- 按需租用 P2P 网络中的 GPU 跑模型推理或批量嵌入任务
- 通过 /deploy 一键在云主机上部署推理提供节点

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L5: A decentralized GPU compute marketplace for **inference and distributed training**, running as a workload plugin on 
> L7: **Infernet runs on c0mpute.** The peer discovery + auction substrate (libp2p Kad-DHT + gossipsub) lives in c0mpute, 
> L95: - **Multi-engine inference** — pluggable adapter (IPIP-0009) over Ollama (any GPU + Apple Silicon + CPU), vLLM (NVI

## 星数曲线

```mermaid
xychart-beta
    title "InfernetProtocol/infernet-protocol 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-28 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `f1a12f73310d` · [字段定义](../../DATASET.md)*
