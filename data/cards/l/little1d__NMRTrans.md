# little1d/NMRTrans

⭐ 18 · Python · MIT · 推送 2026-08-10 · [GitHub](https://github.com/little1d/NMRTrans) · [官网](https://arxiv.org/pdf/2602.10158) · 组织维护

**从实验 NMR 谱解析分子结构的 Set Transformer 框架**

KDD 2026 论文官方代码：基于 Set Transformer（ISAB/PMA）将无序 NMR 峰集合编码为模态表示，可与分子式约束融合，经 T5 解码器自回归生成 SMILES，实现从实验谱到分子结构的解析。提供预训练 checkpoint（Hugging Face，六种输入特征组合）、训练/推理代码与数据集；训练默认配置面向 4 GPU（batch 1024），可缩减到单 GPU；新模态（如 2D NMR）微调需改动数据管线与模型接口。以源码形式安装（conda/uv）。

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

- Set Transformer（ISAB/PMA）编码无序 NMR 峰集合，处理置换不变性
- T5 解码器自回归生成 SMILES，可选分子式约束
- 发布六种输入组合的预训练 checkpoint 与 21,298 样本测试集结果
- 训练曲线与实验参数在 SwanLab 开源以供复现

## 适用场景

- 用实验 C/H-NMR 谱（可加分子式）推断分子结构并输出 SMILES
- 复现论文训练与评测结果
- 以已有 checkpoint 为初始化，在同格式 1D NMR 数据上继续训练

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L1: # 🤓 [KDD 2026] NMRTrans: Structure Elucidation from Experimental NMR Spectra via Set Transformers
> L7: NMRTrans is a transformer-based framework that performs structure elucidation from experimental NMR spectra. By leve

## 星数曲线

```mermaid
xychart-beta
    title "little1d/NMRTrans 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `a449eda3ee7f` · [字段定义](../../DATASET.md)*
