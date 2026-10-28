# Kuanhao-Chao/OpenSpliceAI

⭐ 55 · Python · GPL-3.0 · 推送 2026-10-26 · [GitHub](https://github.com/Kuanhao-Chao/OpenSpliceAI) · [官网](https://khchao.com/OpenSpliceAI/) · 组织维护

**剪接位点预测框架：跨物种预测剪接与变异影响**

基于 PyTorch 的剪接位点预测开源框架，是 SpliceAI 的重新实现与扩展。面向基因组学研究人员，提供数据预处理（FASTA/GFF 转 HDF5）、残差卷积网络训练、迁移学习、模型校准、FASTA 序列预测（输出 BED）与 VCF 变异 delta 评分等子命令。内置更新到 GRCh38/MANE 注释的人源预训练模型及小鼠、拟南芥、蜜蜂、斑马鱼模型，可在单 GPU 上进行全基因组预测。由 Johns Hopkins University 团队开发，有 eLife 论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 人源 GRCh38/MANE 预训练模型及小鼠、拟南芥、蜜蜂、斑马鱼等多物种模型
- 变异子命令计算 delta 评分，评估 SNP/INDEL 对剪接的影响并预测隐匿剪接位点
- create-data/train/transfer/calibrate/predict/variant 完整工具链
- 单 GPU 支持大基因组区域与全基因组预测

## 适用场景

- 预测 DNA 序列中的剪接位点（供体/受体）
- 评估遗传变异对剪接的影响并预测隐匿剪接位点
- 在非模式物种数据上重训练或迁移学习自定义剪接预测模型

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L9:  OpenSpliceAI is an open‐source, efficient, and modular framework for splice site prediction. It is a reimplementati
> L42:  Prediction ( predict ):

## 星数曲线

```mermaid
xychart-beta
    title "Kuanhao-Chao/OpenSpliceAI 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 53 --> 56
    line [54, 55, 55]
```

2026-10-18 54 → 2026-10-28 55（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f1c11a9dd979` · [字段定义](../../DATASET.md)*
