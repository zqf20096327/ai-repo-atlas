# golab-ai/Suiren-Property-Prediction

⭐ 12 · Python · NOASSERTION · 推送 2026-07-20 · [GitHub](https://github.com/golab-ai/Suiren-Property-Prediction) · 组织维护 · 中文 README

**面向计算化学研究者的分子性质预测微调框架**

基于 PyTorch 的微调框架，将 Suiren 预训练分子模型适配到回归与分类两类下游性质预测任务（密度、溶解度、ADMET 等）。要求输入含 SMILES 与 value 两列的 CSV 数据集，支持三种数据划分模式、多 GPU 分布式训练与 EMA 权重保存，提供单条 SMILES 与 CSV 批量推理脚本，训练时自动完成预处理并缓存。权重需从 Hugging Face 或 Modelscope 手动下载，Python 3.8+ 与 PyTorch 2.0+ 为必需依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持回归与分类两类分子性质预测任务的微调训练
- Suiren-ConfAvg 嵌入需在加氢环境（Chem.AddHs）下使用
- torch.distributed 多 GPU 训练与 EMA checkpoint 输出
- 权重同时在 Hugging Face 与 Modelscope 提供

## 适用场景

- 在自己的分子数据上微调预训练模型预测密度、熔点等宏观性质
- 小样本数据场景下微调 Suiren-ConfAvg 做性质回归
- 用训练好的 checkpoint 对 CSV 中的 SMILES 批量预测 ADMET 指标

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L10: A PyTorch-based fine-tuning framework for adapting Suiren pre-trained molecular models to various downstream proper
> L25: - **Regression**: Predicting continuous molecular properties (e.g., density, solubility)
> L178: python inference.py {property_name}

## 星数曲线

```mermaid
xychart-beta
    title "golab-ai/Suiren-Property-Prediction 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-20"]
    y-axis "stars" 11 --> 13
    line [12, 12]
```

2026-11-08 12 → 2026-11-20 12（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 mid · 依据 README sha `ad2b26c5007c` · [字段定义](../../DATASET.md)*
