# NTIA/alignnet

⭐ 20 · Python · NOASSERTION · 推送 2026-11-20 · [GitHub](https://github.com/NTIA/alignnet) · 组织维护

**训练跨数据集对齐的无参考语音质量估计模型**

AlignNet 是 Interspeech 2024 论文的配套代码：在用多个独立数据集训练无参考语音质量估计器时，针对不同主观测试量表或量表使用不一致的问题，用 AudioNet 生成中间分数估计，再由 Aligner 将其映射到对应分数区间。AudioNet 可替换，仓库内置 MOSNet（STFT 输入）和多尺度卷积网络（原始音频输入）两种实现。安装依赖 conda 环境文件，训练配置基于 Hydra，支持通过 clearML 记录（可关闭），推理提供 CLI，论文所用 10 个数据集附引用链接。

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

- AudioNet 与 Aligner 分离设计，AudioNet 可自由替换
- 内置 MOSNet 与 MultiScaleConvolution 两种网络实现
- 训练配置基于 Hydra，支持 clearML 日志（可关闭）
- 提供 inference.py CLI 对音频批量输出质量估计

## 适用场景

- 融合多个主观测试数据集训练无参考语音质量估计器
- 对音频文件批量预测质量分数
- 复现论文中的对齐训练实验

## 场景标签

 · 领域:语音处理/质量评估科研

## 证据(README 行号)

> L4: This code corresponds to the paper "AlignNet: Learning dataset score alignment functions to enable better training o
> L7: AlignNet improves the training of NR speech quality estimators with multiple, independent datasets. AlignNet uses an


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `c12646421d63` · [字段定义](../../DATASET.md)*
