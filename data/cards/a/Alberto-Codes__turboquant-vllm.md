# Alberto-Codes/turboquant-vllm

⭐ 51 · Python · Apache-2.0 · 推送 2026-04-10 · [GitHub](https://github.com/Alberto-Codes/turboquant-vllm) · [官网](https://alberto-codes.github.io/turboquant-vllm/) · 个人维护

**vLLM 的 KV cache 压缩插件：3.76x 压缩、非对称 K/V 量化**

以 vLLM 插件形式实现 Google TurboQuant 算法（ICLR 2025）的 KV cache 压缩，通过随机正交旋转、Lloyd-Max 标量量化与 nibble 打包，将每 token 每 head 的 KV 页压缩至 68 字节（FP16 为 256 字节），支持 K/V 位数不对称配置。TQ4 attention backend 经 vLLM 插件系统自动注册，无需改代码；另提供 HuggingFace CompressedDynamicCache 与 verify CLI。在 8 个模型上给出余弦相似度数据；RTX 4090 实验显示 TTFT 降低 25.2%，但 TPOT 增加约 3 倍、吞吐 -7%，README 注明适合显存受限、长上下文等 memory-bound 场景。Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 3.76x KV cache 压缩，支持 K/V 非对称位数（如 K4/V3）
- vLLM 插件系统自动注册 attention backend，无需改代码
- 8 个模型（Llama/Qwen/Mistral/Phi/Gemma 等）的逐层余弦相似度验证
- verify CLI 可对任意模型自测压缩质量

## 适用场景

- 显存受限的消费级 GPU 上跑更大上下文的推理
- 为已部署的 vLLM 服务降低 KV cache 显存占用
- 自验证模型在 3-4 bit KV 量化下的精度损失

## 场景标签

`模型量化` · 领域:训练与推理

## 证据(README 行号)

> L9: TurboQuant KV cache compression as a drop-in vLLM plugin. **3.76x KV cache compression with asymmetric K/V support, 
> L27: The TQ4 attention backend registers automatically via vLLM's plugin system:
> L30: vllm serve meta-llama/Llama-3.1-8B-Instruct --attention-backend CUSTOM

## 星数曲线

```mermaid
xychart-beta
    title "Alberto-Codes/turboquant-vllm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-24 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d670be3d1ebb` · [字段定义](../../DATASET.md)*
