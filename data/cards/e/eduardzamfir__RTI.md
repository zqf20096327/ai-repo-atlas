# eduardzamfir/RTI

⭐ 16 · Python · MIT · 推送 2026-09-10 · [GitHub](https://github.com/eduardzamfir/RTI) · 组织维护

**像素空间扩散 Transformer 的弹性 token 压缩方法官方代码（RTI）**

arXiv 论文 "Elastic Token Compression for Pixel-Space Diffusion Transformers" 的官方实现：提出 Region Token Interface（RTI），将冻结的 MiniT2I 主干中间块在少量区域 token 上运行——沿 Hilbert 曲线排序 patch 并在特征变化最大处切分，Read 软池化、Write 散射回写；仅训练 LoRA 与小接口，微调时每步随机抽取区域数 R，使单一检查点覆盖 64–1024 全部预算，推理时用 --budget 在质量/算力曲线上调节。提供采样、评测（GenEval/MJHQ-30K）与微调脚本，检查点仅含适配器（B/16 62MB）。面向计算机视觉研究者，依赖 conda 环境与多卡训练。

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

- Hilbert 曲线切分 + 软池化的区域 token 压缩，单检查点覆盖 64–1024 全预算
- 在冻结 MiniT2I 主干上仅训练 LoRA 与接口（62–137MB 适配器）
- 提供采样、GenEval/MJHQ-30K 评测与 torchrun 多卡微调脚本
- 论文结果在此代码库中可复现（results/reproduction/）

## 适用场景

- 用同一检查点按 --budget 调节文生图质量与算力
- 复现论文的 GenEval 与 FID 评测结果
- 在自己的数据上微调 RTI 接口与 LoRA

## 场景标签

`图像生成` `微调` · 领域:内容生成

## 证据(README 行号)

> L34: A frozen MiniT2I backbone runs its middle blocks on `R ≪ N` region tokens:
> L44: and the small interface are trained, and **`R` is drawn per step during fine-tuning, so a
> L108: |RTI-B/16|3–13|64 – 1024|`eduardzamfir/RTI` → `rti_b16_40k.pt`|

## 星数曲线

```mermaid
xychart-beta
    title "eduardzamfir/RTI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `6c39a36a8463` · [字段定义](../../DATASET.md)*
