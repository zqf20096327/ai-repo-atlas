# huggingface/flux-fast

⭐ 173 · Python · 推送 2026-01-05 · [GitHub](https://github.com/huggingface/flux-fast) · [官网](https://pytorch.org/blog/presenting-flux-fast-making-flux-go-brrr-on-h100s/) · 组织维护

**Flux 图像生成管线的 GPU 加速配方集合（约 2.5x 提速）**

Hugging Face 维护的 Flux.1（Schnell/Dev/Kontext Dev）推理加速配方仓库，非库亦非开箱即用方案，需用户 fork 代码自行修改。优化以纯 PyTorch 为主：bfloat16、torch.compile、合并 qkv 投影、channels_last、Flash Attention v3、float8 动态量化、AOTI 导出与 CUDAGraphs、cache-dit 缓存。除 float8 量化外均无损。支持 NVIDIA H100 与 AMD MI300X，部分优化可用于 CPU。导出的二进制仅限 Linux 且依赖相近硬件环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Flux.1-Schnell/Dev 报告约 2.5x 提速，Kontext Dev 同样适用
- AMD MI300X 通过 AITER fp8 kernel 支持
- float8 量化外其余优化均无损；量化可关闭
- 提供 gen_image.py 生成图像与 run_benchmark.py 基准脚本

## 适用场景

- 我在 H100/MI300X 上加速 Flux 文生图推理
- 我需要可复现的逐项优化对比基准
- 我想用 AOTI 导出跳过编译开销

## 场景标签

 · 领域:AI 基础设施/推理优化

## 证据(README 行号)

> L2: Making Flux go brrr on GPUs. With simple recipes from this repo, we enabled ~2.5x speedup on Flux.1-Schnell and Flux
> L93: For hardware, we used a 96GB 700W H100 GPU and 192GB MI300X GPU. Some of the optimizations applied (BFloat16, torch

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/flux-fast 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 172 --> 174
    line [173, 173]
```

2026-10-18 173 → 2026-10-22 173（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `d028c98e31ca` · [字段定义](../../DATASET.md)*
