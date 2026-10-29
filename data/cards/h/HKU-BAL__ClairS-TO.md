# HKU-BAL/ClairS-TO

⭐ 98 · Python · BSD-3-Clause · 推送 2026-09-09 · [GitHub](https://github.com/HKU-BAL/ClairS-TO) · 组织维护

**长读长肿瘤-only 体细胞小变异检测的深度学习工具**

HKU-BAL 维护的 Clair 系列工具，面向无匹配正常样本的肿瘤样本，检测长读长（ONT、PacBio HiFi）及 Illumina 数据中的体细胞 SNV 与 Indel。核心机制为肯定式（AFF）与否定式（NEG）两个神经网络的集成，结合先验概率计算后验；再经九种硬过滤、多个 Panel of Normals 及基于肿瘤纯度与拷贝数图谱的 verdict 统计分类模块进行后过滤。提供预训练模型（SS/SSRS 两类）与自定义训练流程，单命令运行，输出 VCF。论文发表于 Nature Communications。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AFF+NEG 双神经网络集成区分体细胞与胚系变异及背景噪音
- 支持 ONT、PacBio Revio、Illumina 三平台，提供 SS/SSRS 预训练模型
- 九种硬过滤、多个 PoN 与基于 CNA/肿瘤纯度的 verdict 分类模块
- 提供合成样本/真实样本训练流程供用户自训模型

## 适用场景

- 仅有肿瘤样本时做长读长体细胞 SNV/Indel 检测
- 用自有的肿瘤样本训练适配特定癌种的模型
- 肿瘤样本 Illumina 数据的体细胞变异检出

## 场景标签

 · 领域:生物信息学/基因组变异检测

## 证据(README 行号)

> L3: # ClairS-TO - a deep-learning method for long-read tumor-only somatic small variant calling
> L12: ClairS-TO (Somatic Tumor-Only) is a tool in the Clair series to support long-read tumor-only somatic small variant 
> L16: In ClairS-TO, we use an ensemble of two disparate neural networks that were trained from the same samples but for t

## 星数曲线

```mermaid
xychart-beta
    title "HKU-BAL/ClairS-TO 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 97 --> 99
    line [98, 98]
```

2026-10-18 98 → 2026-10-29 98（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `abd893dcb572` · [字段定义](../../DATASET.md)*
