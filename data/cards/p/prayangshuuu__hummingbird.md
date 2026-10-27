# prayangshuuu/hummingbird

⭐ 61 · C · NOASSERTION · 推送 2026-07-31 · [GitHub](https://github.com/prayangshuuu/hummingbird) · 个人维护

**零依赖 C17 LLM 推理运行时：统一 SSD/RAM/VRAM 跑超大 MoE 模型**

用可移植 C17 编写的零第三方依赖推理引擎，面向在消费级硬件上运行稠密与 MoE 大模型。核心机制是将 SSD、RAM、VRAM 统一为单一托管内存层级：常驻权重留内存，路由专家权重按需从磁盘流式读取并带学习缓存。当前 CPU 推理已可用（hb CLI 支持生成与 serving），流式引擎、SIMD 内核、CUDA/Metal 后端仍在开发或规划中；已实现 Safetensors 解析与 GPT-OSS 适配器，GGUF 解析尚未提供。可通过稳定 C ABI 嵌入其他应用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- SSD/RAM/VRAM 统一内存层级，专家权重按需流式读取
- 零第三方运行时依赖的 C17 实现，含稳定 C ABI 供嵌入
- hb CLI 支持一次性生成与 serving（CPU 推理已可用）
- fp16/bf16/mxfp4 量化元数据与 Safetensors 解析，已交付 GPT-OSS 适配器

## 适用场景

- 在内存有限的家用电脑上运行数百 B 参数的 MoE 开源模型
- 用 hb CLI 做本地文本生成或模型 serving
- 通过 C ABI 将推理能力嵌入自己的应用

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L8:  A zero-dependency C17 runtime for running massive open-source LLMs,
> L49: Once the frontends are built, you can use the `hb` CLI for inference and serving (CPU inference is now fully functi

## 星数曲线

```mermaid
xychart-beta
    title "prayangshuuu/hummingbird 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 59 --> 62
    line [60, 61, 61]
```

2026-10-18 60 → 2026-10-27 61（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `43ebad1629d2` · [字段定义](../../DATASET.md)*
