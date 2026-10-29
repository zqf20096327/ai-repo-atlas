# Tencent-Hunyuan/GEAR

⭐ 68 · Python · NOASSERTION · 推送 2026-08-07 · [GitHub](https://github.com/Tencent-Hunyuan/GEAR) · 组织维护 · 中文 README

**端到端共训 VQ tokenizer 与自回归生成器的图像合成方法**

腾讯混元与北京大学团队的图像合成研究项目（PyTorch 官方实现）。GEAR 通过软分配桥接让自回归生成器的梯度引导 tokenizer 训练，宣称 ImageNet gFID 收敛提速约 10 倍，适用于 VQ/LFQ/IBQ 量化器与文生图场景。发布物以 tokenizer 权重为核心（三种量化器各含 warm-up 基线与端到端版本），另含一个可在冻结 GEAR-VQ 上直接运行的文生图 AR 模型（LlamaGen-1B、Qwen3-1.7B 文本编码器）。训练分三阶段脚本，默认单机 8 GPU，提供推理与 GenEval/DPG-Bench/WISE 等评测驱动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- VQ tokenizer 与自回归生成器端到端共训（硬/软双读出解耦优化）
- 兼容 VQ/LFQ/IBQ 三种量化器与文生图任务
- 在 Hugging Face Hub 发布 tokenizer 权重与文生图 AR 模型 GEAR-T2I-GPIC-1B
- 提供三阶段训练脚本、推理脚本与多基准评测驱动

## 适用场景

- 在冻结 GEAR tokenizer 上训练自己的类条件 ImageNet 自回归模型
- 直接下载 GEAR-T2I-GPIC-1B 进行文生图推理
- 复现论文中的 tokenizer 重建与 gFID/GenEval 等评测结果

## 场景标签

`图像生成` `模型训练` · 领域:内容生成

## 证据(README 行号)

> L29: > 🚀 **GEAR co-trains a VQ tokenizer and an autoregressive (AR) generator end-to-end** — the tokenizer feels the gra
> L67: GEAR's core contribution is the **tokenizer**, so that is what we release. Train your own AR
> L89: Besides the tokenizers, we also release one **ready-to-run text-to-image AR** so you can

## 星数曲线

```mermaid
xychart-beta
    title "Tencent-Hunyuan/GEAR 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 67 --> 69
    line [68, 68]
```

2026-10-18 68 → 2026-10-29 68（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `9a4634fdefaf` · [字段定义](../../DATASET.md)*
