# black-yt/ExtremeCast

⭐ 28 · Python · 推送 2026-03-17 · [GitHub](https://github.com/black-yt/ExtremeCast) · 组织维护

**面向科研者的极端天气预报增强模型：Exloss 损失 + ExBooster 模块**

数据驱动全球中期天气预报研究代码，针对 ML 模型低估极端值的问题提供两项组件：Exloss 非对称损失函数（论证对称损失如 MSE 导致预测偏差）与训练无关的 ExBooster 极值增强模块（通过多次随机采样捕捉预测不确定性，提高低概率极端事件命中率）。推理在 GPU 上运行 run.py，需从 GoogleDrive 申请权限下载数据与 checkpoint，输入输出为 69 通道气象变量。附 arXiv 论文与 BibTeX 引用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Exloss 非对称损失，针对 MSE 低估极端值的问题
- 训练无关的 ExBooster 极值增强模块，多次随机采样捕捉不确定性
- 提供 ONNX 与 PyTorch checkpoint 及 GPU 推理脚本 run.py

## 适用场景

- 研究极端天气预报的预测精度改进方法
- 复现论文实验与极端天气预测指标评估
- 在已有全球天气预报模型上叠加极值增强模块

## 场景标签

`科研工具` `模型训练` · 领域:学习与行业

## 证据(README 行号)

> L5: Data-driven weather forecast based on machine learning (ML) has experienced rapid development and demonstrated super
> L47: Run run.py on GPU device.

## 星数曲线

```mermaid
xychart-beta
    title "black-yt/ExtremeCast 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `33110d5d34ac` · [字段定义](../../DATASET.md)*
