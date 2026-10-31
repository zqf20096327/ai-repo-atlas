# mnielLab/NetTCR-2.2

⭐ 15 · Python · NOASSERTION · 推送 2026-02-02 · [GitHub](https://github.com/mnielLab/NetTCR-2.2) · 组织维护

**深度学习模型：基于序列预测肽-TCR 结合特异性**

NetTCR-2.2 是用卷积神经网络预测给定 TCR 是否结合特定肽的深度学习模型，基于 Keras 构建，使用配对链数据（peptide 与六个 CDR 序列）。提供 pan、peptide、pretrained 三种训练/预测模式，训练输出 .h5 与 .tflite 模型文件，附带公开数据集（含 IEDB/VDJdb/10X 来源）、冗余消减数据集及论文最终模型，另有配套在线服务器与本地复现脚本。许可证限学术非商业用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CNN 预测 TCR-肽结合，支持 pan/peptide/pretrained 三种模式
- 输入为 peptide 与六个 CDR 序列，输出结合预测 CSV
- 附带论文所用数据集、训练好的模型与负对照百分位排名机制
- 提供 TCRbase 整合的类 webserver 本地预测脚本

## 适用场景

- 免疫学研究者在本地预测 TCR 对特定肽的结合
- 用自有数据训练 pan 或 peptide 特异性模型
- 复现论文实验或与 IMMREP 2022 基准对比

## 场景标签

 · 领域:生物信息学/免疫信息学

## 证据(README 行号)

> L2: NetTCR-2.2 is a deep learning model used to predict TCR specificity. Like NetTCR-2.1 [1], NetTCR-2.2 uses convolutio
> L12: The model architectures were built in Keras [2], and are located in `src/nettcr_archs.py`.

## 星数曲线

```mermaid
xychart-beta
    title "mnielLab/NetTCR-2.2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `9757099c39f4` · [字段定义](../../DATASET.md)*
