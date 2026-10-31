# HKU-BAL/ClairS

⭐ 117 · Python · BSD-3-Clause · 推送 2026-09-11 · [GitHub](https://github.com/HKU-BAL/ClairS) · 组织维护

**长读长肿瘤-正常配对体细胞小变异检测的深度学习方法**

ClairS 是面向配对样本（主要 ONT 长读长，另支持 PacBio Revio/HiFi 与 Illumina）的体细胞 SNV/Indel 检测工具：利用 Clair3 的 pileup 与 full-alignment 双模型集成并结合规则与后过滤，去除 germline 变异；提供 ss 与 ssrs 两类模型，支持性别染色体感知 calling、中间分型（WhatsHap/LongPhase）、基于 CNV 与肿瘤纯度的 Verdict 分类模块，以及合成样本/真实样本训练工作流。以 Docker 镜像与源码方式发布，论文发表于 Nature Methods。

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

- 集成 Clair3 pileup 与 full-alignment 模型并配规则和后过滤进行体细胞 calling
- 支持 ONT/PacBio Revio/HiFi/Illumina 多平台模型，含 ss 与 ssrs 两种训练类型
- Verdict 模块可基于 CNV 与肿瘤纯度将变异分类为 germline/somatic/亚克隆 somatic
- 支持性别染色体 ploidy 感知与 LongPhase 体细胞单倍型后过滤集成

## 适用场景

- 肿瘤-正常配对样本的长读长体细胞 SNV/Indel 检测
- 液体肿瘤或低覆盖样本场景选用专用模型 calling
- 在已有 pipeline 中利用预分型 BAM 跳过中间分型步骤

## 场景标签

 · 领域:生物信息学/基因组变异检测

## 证据(README 行号)

> L3: # ClairS: a deep-learning method for long-read tumor–normal pair somatic small variant calling
> L12: ClairS is a somatic variant caller designed for paired samples and primarily ONT long-read. It uses Clair3 to elimi

## 星数曲线

```mermaid
xychart-beta
    title "HKU-BAL/ClairS 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-31"]
    y-axis "stars" 115 --> 118
    line [116, 117, 117]
```

2026-10-18 116 → 2026-10-31 117（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `4d3874bb0f32` · [字段定义](../../DATASET.md)*
