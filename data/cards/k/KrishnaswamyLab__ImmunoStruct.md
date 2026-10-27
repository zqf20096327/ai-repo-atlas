# KrishnaswamyLab/ImmunoStruct

⭐ 53 · Python · NOASSERTION · 推送 2026-10-05 · [GitHub](https://github.com/KrishnaswamyLab/ImmunoStruct) · [官网](https://www.nature.com/articles/s42256-025-01163-y) · 组织维护

**多模态深度学习框架：预测多等位基因 class-I pMHC 免疫原性**

面向免疫学与计算生物学研究者的科研代码库：整合 peptide-MHC 的序列、结构与生化性质三类模态，基于 26,049 条 peptide-MHC 数据联合建模，预测感染性疾病表位与癌症新表位的免疫原性；引入癌症-野生型对比学习提升新表位检测特异性，并提供免疫原性亚结构基础的解释性分析。安装需 conda 环境、CUDA GPU 与 Weights & Biases 账户；数据与预训练权重通过 HuggingFace 下载，结构数据由 AlphaFold2 生成（提供现成 PyG 图，或按本地 MSA 流程自行折叠）。预训练模型权重与多模态数据已开源，端到端工具尚标注为 TODO。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 整合序列、结构与生化性质的多模态建模，覆盖 26,049 条 peptide-MHC
- 癌症-野生型对比学习用于新表位检测
- 预训练权重与多模态数据集在 HuggingFace 开放下载
- 提供生化元属性（Mprop1/Mprop2）与 foreignness 分数计算脚本（Luksza et al. 2017 模型）

## 适用场景

- 预测候选肽段（传染病表位或癌症新表位）的免疫原性
- 对新肽段数据集生成生化元属性与 foreignness 分数
- 基于 AlphaFold2 结构自定义图构建逻辑

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L71: ImmunoStruct is a multimodal deep learning framework that integrates sequence, structural, and biochemical informat
> L77: * **Multimodal Integration**: Combines peptide-MHC protein sequence, structure, and biochemical properties

## 星数曲线

```mermaid
xychart-beta
    title "KrishnaswamyLab/ImmunoStruct 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26", "2026-10-27"]
    y-axis "stars" 50 --> 54
    line [51, 52, 53, 53]
```

2026-10-18 51 → 2026-10-27 53（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `3310b15f2bae` · [字段定义](../../DATASET.md)*
