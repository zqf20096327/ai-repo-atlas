# licheng-xu-echo/RXNGraphormer

⭐ 60 · Jupyter Notebook · MIT · 推送 2026-08-24 · [GitHub](https://github.com/licheng-xu-echo/RXNGraphormer) · [官网](https://www.nature.com/articles/s42256-025-01098-4) · 组织维护 · 中文 README

**化学反应预测与合成规划的预训练深度学习框架**

论文官方实现：将图神经网络与 Transformer 结合，从 1,300 万反应中预训练，统一处理跨任务反应预测，包括产率与选择性估计（回归）、正/逆合成规划（序列生成）、反应嵌入生成与虚构反应识别。提供 conda 安装流程、figshare 模型权重与数据集下载、训练/评测脚本，支持多 GPU 训练。基于 Python 3.8、PyTorch 1.12.1+cu113、PyG、RDKit，在 Ubuntu 22.04 测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GNN+Transformer 统一架构捕获分子内与分子间信息
- 1,300 万反应预训练模型
- 同时支持回归（产率/选择性）与序列生成（正逆合成）任务
- 提供反应嵌入生成与虚构反应识别功能

## 适用场景

- 预测化学反应产率与区域/对映选择性
- 进行正向与逆合成路线规划
- 生成反应嵌入用于反应类型分析
- 在自有数据上微调或复现论文结果

## 场景标签

`模型训练` `微调` · 领域:训练与推理

## 证据(README 行号)

> L7: Official implementation of *"A unified pre-trained deep learning framework for cross-task reaction performance predi
> L16: - **Cross-task Reaction Prediction**: Simultaneous handling of:
> L18:  - Forward- and retro-synthesis planning (sequence generation)

## 星数曲线

```mermaid
xychart-beta
    title "licheng-xu-echo/RXNGraphormer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 59 --> 61
    line [60, 60]
```

2026-10-18 60 → 2026-10-26 60（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b280c4ad33cf` · [字段定义](../../DATASET.md)*
