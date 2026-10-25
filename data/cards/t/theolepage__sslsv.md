# theolepage/sslsv

⭐ 41 · Python · MIT · 推送 2026-10-06 · [GitHub](https://github.com/theolepage/sslsv) · 个人维护

**说话人验证的自监督学习训练与评测工具包**

基于 PyTorch 的深度学习工具包，将计算机视觉领域的自监督学习框架（SimCLR、MoCo、DINO、BYOL、VICReg、Barlow Twins 等 12 种）适配到说话人表征学习，用于说话人验证。提供 TDNN、ResNet-34、ECAPA-TDNN 等编码器及可接入 WavLM/HuBERT/wav2vec 2.0 的 S3PRL 接口，支持多 GPU 分布式训练、余弦打分与 PLDA 后端评测，在 VoxCeleb 等数据集上给出统一基准。以 pip 包与源码方式安装，面向语音表征研究场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 12 种自监督框架实现（SimCLR/MoCo/DINO/BYOL/VICReg 等）
- 支持 CPU/GPU/多 GPU（DataParallel 与 DDP）训练
- Cosine 打分归一化与 PLDA 评测后端，指标含 EER/minDCF/CLLR
- S3PRL 接口可加载 WavLM/HuBERT/wav2vec 2.0 作为编码器

## 适用场景

- 在 VoxCeleb 上统一训练并比较各 SSL 框架的说话人验证性能
- 复现论文基准或使用作者三项贡献方法（Combiner/Margins/SSPS）
- 在语言、情感等下游任务上评测说话人表征

## 场景标签

`模型训练` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: **sslsv** is a PyTorch-based deep learning toolkit consisting of a collection of **Self-Supervised Learning** (SSL) 
> L5: Its main objectives are to: **(1) provide implementations of state-of-the-art SSL frameworks** by adapting algorithm

## 星数曲线

```mermaid
xychart-beta
    title "theolepage/sslsv 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-25 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `51eeb541f34a` · [字段定义](../../DATASET.md)*
