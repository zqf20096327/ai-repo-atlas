# youngharold/tightwad

⭐ 38 · Python · MIT · 推送 2026-07-02 · [GitHub](https://github.com/youngharold/tightwad) · [官网](https://tightwad.dev) · 个人维护

**混厂牌 GPU 推理集群管理器，带跨机投机解码代理**

面向拥有多台异构机器（NVIDIA+AMD、消费级 GPU、旧硬件）的用户，把分散 GPU 通过 llama.cpp RPC 聚合成单一 OpenAI 兼容 API，并在其上提供应用层投机解码：小模型起草 token、大模型批量验证，宣称输出与大模型单独运行等价。共六种模式：投机解码代理、多起草者共识、RPC 集群、质量门控、P2P 模型分发，以及 MoE 支持（GGUF defuse、按专家放置）。以 PyPI 包与 Docker 镜像分发。限制：协调机需容纳完整模型文件的系统内存（70B Q4 约 44GB RAM）；非环回绑定强制要求代理令牌。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨机器混厂牌 GPU 池化（CUDA+ROCm），单一 OpenAI 兼容 API
- 跨网络服务器的应用层投机解码（token ID 级流量）
- 六种运行模式：投机代理/共识/RPC 集群/质量门控/P2P 分发/MoE
- v0.5 起支持 MoE GGUF defuse 与按专家平衡放置

## 适用场景

- 把家里多台旧机器的 GPU 拼起来跑放不进单机的大模型
- 不改聊天 UI，仅换 URL 即给现有 Ollama/llama.cpp 服务加速
- 多台廉价机器起草、单台 GPU 审核的质量门控部署

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: Mixed-vendor GPU inference cluster manager with speculative decoding proxy. Pools CUDA and ROCm GPUs across machines
> L39: |**Points at**|`http://192.168.1.10:11434` (Ollama on one machine)|`http://192.168.1.10:8088` (Tightwad proxy)|
> L78: Combine GPUs from different machines and vendors into a single OpenAI-compatible API. The coordinator distributes m

## 星数曲线

```mermaid
xychart-beta
    title "youngharold/tightwad 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-29 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `306c4923fc87` · [字段定义](../../DATASET.md)*
