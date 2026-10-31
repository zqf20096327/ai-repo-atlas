# dropbox/hqq

⭐ 960 · Python · Apache-2.0 · 推送 2026-02-26 · [GitHub](https://github.com/dropbox/hqq) · [官网](https://dropbox.github.io/hqq_blog/) · 组织维护

**大模型免校准量化库：分钟级完成 1-8bit 量化**

Dropbox 官方维护的 Half-Quadratic Quantization（HQQ/HQQ+）实现：一种无需校准数据的模型量化方法，支持 8/4/3/2/1 bit，可用于 LLM 与视觉等任意模型，替代 torch.nn.Linear 层即可完成量化。提供 PyTorch/ATEN 原生反量化后端，以及配合 torch.compile 与外部融合内核的加速推理路径；支持 HuggingFace transformers 集成、peft 训练与 vLLM（需装 GemLite）。HQQ+ 通过可训练低秩适配器提升低 bit 质量。限制：ATEN 后端仅支持 axis=0，优化推理后端仅支持 axis=1，hqq 库保存的模型不兼容 from_pretrained。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无需校准数据的快速量化，支持 8/4/3/2/1 bit
- 与 HuggingFace transformers 集成，可按层设置不同量化配置
- 支持 vLLM 后端与 peft 训练（HQQ+/LoRA）
- 提供 PyTorch/ATEN/torch.compile 多种后端

## 适用场景

- 在不准备校准数据的情况下快速量化大模型以降低显存占用
- 对 LLM 做 4-bit 量化后用融合内核加速推理
- 在量化模型上做 LoRA 低秩训练（HQQ+）

## 场景标签

`模型量化` · 领域:训练与推理

## 证据(README 行号)

> L7:  HQQ is a fast and accurate model quantizer that skips the need for calibration data. Quantize the largest models, w
> L48: To perform quantization with HQQ, you simply need to replace the linear layers ( ```torch.nn.Linear```) as follows:
> L130: ### VLLM

## 星数曲线

```mermaid
xychart-beta
    title "dropbox/hqq 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 959 --> 961
    line [960, 960]
```

2026-10-18 960 → 2026-10-31 960（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `73cf7f2a5740` · [字段定义](../../DATASET.md)*
