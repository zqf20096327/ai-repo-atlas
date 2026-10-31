# shootthesound/torch-nvenc-compress

⭐ 32 · Python · NOASSERTION · 推送 2026-05-16 · [GitHub](https://github.com/shootthesound/torch-nvenc-compress) · 个人维护

**用 GPU 空闲 NVENC 单元压缩神经网络状态的编解码库**

面向 ML 训练/推理的神经状态编解码库：将扩散模型激活、LLM KV cache、梯度张量量化为 uint8 并投影到 PCA 低秩基，经 HEVC（QP=10–28）编码为紧凑码流，再在对端解码，供跨机传输时降低线缆带宽占用。读取 Nvidia GPU 上 ML 计算期间空闲的 NVENC 专用编码单元，实测 FLUX 激活 6.1× 无损压缩、KV cache 3×、专用硅上单帧亚毫秒级延迟。给分布式训练/推理开发者做跨机池化显存用；README 明言端到端 Thunderbolt 训练总耗时未实测，框架集成胶水层仍是待完成工作。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 量化+PCA+HEVC 的张量编解码，激活 6×、KV cache 3× 无损压缩（实测）
- 复用 ML 计算期间空闲的 NVENC 专用编码单元，单帧亚毫秒（0.180ms 编码/0.262ms 解码）
- 独立 CUDA stream 并行路径机制，编解码延迟可被计算掩盖
- 下游应用 comfyui-mesh 用其跨两 GPU 分割 FLUX.2 模型

## 适用场景

- 两台消费级 GPU 机器经 Thunderbolt 直连池化 48–128 GB 显存跑大模型
- 跨机 LoRA 微调时压缩梯度同步流量
- 多 GPU 分布式推理中压缩层间激活以加速 prefill

## 场景标签

 · 领域:ML 基础设施/分布式计算

## 证据(README 行号)

> L3: > A **reusable codec library** for neural-network state — diffusion model activations, LLM KV cache, gradients — usi
> L7: The mechanism is straightforward. Quantize the tensor to uint8 with per-channel scaling, project onto a low-rank PCA
> L82: 6. **The codec:** wrap your gradient pack/unpack (or activation pack/unpack) with `nvenc_compress.direct.DirectBack

## 星数曲线

```mermaid
xychart-beta
    title "shootthesound/torch-nvenc-compress 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-31 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `319e37a0f2d9` · [字段定义](../../DATASET.md)*
