# google/deepsomatic

⭐ 325 · BSD-3-Clause · 推送 2026-03-05 · [GitHub](https://github.com/google/deepsomatic) · 组织维护

**深度学习体细胞变异检测流程：从肿瘤测序数据产出 VCF**

DeepVariant 的扩展流程：读取肿瘤-正常或仅肿瘤的比对数据（BAM/CRAM），生成 pileup 图像张量，经卷积神经网络分类后在标准 VCF/gVCF 中报告体细胞变异，并通过 FILTER 字段区分体细胞、胚系、参照等类别。代码与 DeepVariant 集成，提供 make_examples、call_variants、postprocess 等核心脚本。官方以 Docker 镜像方式运行，要求 Unix-like 系统与 Python 3.10，不可在 Windows 上运行。覆盖 Illumina/PacBio/ONT 及 FFPE 样本的多组案例研究。

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

- CNN 分类 pileup 图像张量进行体细胞变异检测
- 支持 tumor-normal 与 tumor-only 两种模式
- 输出标准 VCF/gVCF，FILTER 区分 GERMLINE/RefCall/PASS 等类别
- 覆盖 Illumina、PacBio、ONT 与 FFPE 样本的案例研究

## 适用场景

- 肿瘤-正常配对测序数据的体细胞变异检测
- 仅肿瘤样本的变异检测
- 不同测序平台产出的 BAM/CRAM 数据分析

## 场景标签

 · 领域:生物信息学/基因组学

## 证据(README 行号)

> L7: DeepSomatic is an extension of deep learning-based variant caller
> L10: tensors from them, classifies each tensor using a convolutional neural network,

## 星数曲线

```mermaid
xychart-beta
    title "google/deepsomatic 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 324 --> 326
    line [325, 325]
```

2026-10-18 325 → 2026-10-23 325（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `46176153e83a` · [字段定义](../../DATASET.md)*
