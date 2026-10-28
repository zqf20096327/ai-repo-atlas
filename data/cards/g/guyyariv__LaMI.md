# guyyariv/LaMI

⭐ 20 · Python · MIT · 推送 2026-07-04 · [GitHub](https://github.com/guyyariv/LaMI) · [官网](https://guyyariv.github.io/LaMI/) · 个人维护

**论文官方实现：测试时生成多图并晚融合，增强 LLM 视觉常识推理**

ACL 2026 Oral 论文 LaMI 的官方 PyTorch 实现：针对纯文本 LLM 缺乏视觉接地的问题，在测试时用 SDXL-Turbo 从文本提示并行采样生成多张图像，经 CLIP 视觉编码后，通过投影层与单层融合 Transformer 在最终预测前与文本 LLM 的预测概率做晚融合。训练时冻结基础 LM 与 CLIP 编码器，只训练投影与融合模块。支持 GPT-2、Gemma、LLaMA 3 与 BERT 系基座，提供统一训练与评测入口，覆盖 ImageNetVC、PIQA、SIQA、ARC 等基准。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 测试时从文本提示生成 k 张图像（SDXL-Turbo）并做晚融合
- 只训练投影层与 1 层融合 Transformer，基础 LM 与 CLIP 编码器冻结
- 支持 GPT-2 / Gemma / LLaMA 3 / BERT 系基座，自动识别模型家族
- 统一评测入口覆盖 ImageNetVC、常识推理、SQuAD v2、QuAC、BoolQ 等基准

## 适用场景

- 复现论文的视觉常识推理与 NLP 基准实验
- 在冻结文本 LLM 上注入视觉信号以提升视觉接地任务表现
- 研究多图像测试时融合方法对 LLM 推理的影响

## 场景标签

`多模态` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: This repo contains the official PyTorch implementation of *LaMI: Augmenting Large Language Models via Late Multi-Ima
> L7: Commonsense reasoning often requires both textual and visual knowledge, yet Large Language Models (LLMs) trained sol
> L76: - `--generate_images` — generate `k` images per prompt with SDXL-Turbo and late-fuse them.

## 星数曲线

```mermaid
xychart-beta
    title "guyyariv/LaMI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a0e1a55338f7` · [字段定义](../../DATASET.md)*
