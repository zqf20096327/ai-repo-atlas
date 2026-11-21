# USDepartmentofLabor/soii_neural_autocoder

⭐ 23 · Python · 推送 2026-11-18 · [GitHub](https://github.com/USDepartmentofLabor/soii_neural_autocoder) · 组织维护

**职业伤病调查文本的职业/伤病代码神经网络自动编码器**

美国劳工部发布的 SOII（职业伤病调查）自动编码神经网络：读取含职业文本、事故叙述（事件/性质/来源等）、机构名、NAICS/SOC 代码等 24 列的 CSV 训练数据，训练模型为伤病分配 OIICS 性质/部位/事件/来源代码。实现自论文 Deep neural networks for worker injury autocoding 所述模型的近似版本，通过拼接全部文本输入实现更高效的批量处理。依赖 Python 3.6、TensorFlow 1.8、Keras 2.1.6 等旧版本库。

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

- 对事故叙述文本预测 OIICS 性质/部位/事件/来源代码
- 拼接全部文本输入的批量处理方式提升训练速度
- 提供含虚拟训练集的示例脚本可开箱运行
- 训练 checkpoint 与日志自动保存

## 适用场景

- 将职业伤病事故叙述自动编码为 OIICS 代码
- 复现论文所述的工伤自动编码模型训练

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L2: >**END OF LIFE NOTICE:** This project has reached end-of-life and is no longer maintained. No further updates or sec
> L6: Contains the code used to train a close relative of the neural network autocoder
> L37: |nature_code|The 2.01 OIICS nature code|1233|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `bfcf10ae8f5a` · [字段定义](../../DATASET.md)*
