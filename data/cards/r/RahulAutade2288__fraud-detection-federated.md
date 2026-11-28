# RahulAutade2288/fraud-detection-federated

⭐ 110 · Python · 推送 2026-11-26 · [GitHub](https://github.com/RahulAutade2288/fraud-detection-federated) · 个人维护

**银行间联邦学习欺诈检测原型：数据不出行 jointly 训练共享模型**

Python 原型项目，模拟多家银行作为客户端在本地交易数据上训练 Keras 模型，仅上传模型权重，由中央协调器用 TensorFlow Federated 执行 10 轮加权 Federated Averaging 得到全局模型。内置合成交易数据（约 250 条、欺诈率 15.6%）、命令行数据分析、Jupyter 笔记本、评估指标（准确率/精确率/召回率/F1/ROC/PR）及单元测试。面向学习与研究用途，README 明确声明非生产级反欺诈系统。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TensorFlow Federated 实现 10 轮 Federated Averaging，原始数据保留在各客户端
- 提供 accuracy/precision/recall/F1、混淆矩阵、ROC/PR 曲线评估
- 含 Jupyter 笔记本、命令行数据分析与数据完整性单元测试

## 适用场景

- 学习联邦学习在反欺诈场景的运行机制
- 在不共享原始交易数据的前提下模拟多机构联合建模
- 为隐私合规（GDPR/GLBA）背景下的欺诈检测方案做原型验证

## 场景标签

`金融量化` `模型训练` · 领域:学习与行业

## 证据(README 行号)

> L3: A Python prototype showing how several banks could train a shared fraud-detection model **without pooling their tran
> L18: 4. **Aggregate**: TensorFlow Federated runs weighted Federated Averaging over 10 rounds, with SGD on the clients an


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `f07b60c274a9` · [字段定义](../../DATASET.md)*
