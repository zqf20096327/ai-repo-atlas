# yiamcb/TAFN

⭐ 16 · Jupyter Notebook · 推送 2026-03-18 · [GitHub](https://github.com/yiamcb/TAFN) · 组织维护

**EEG-fNIRS 分类的时序注意力融合网络模型代码**

论文配套代码库，实现 TAFN 深度学习模型及其自定义损失函数，用于 EEG–fNIRS 脑机接口数据的认知与运动意图分类。模型在 LSTM 与时序卷积层中引入注意力机制，损失函数组合类别权重与非对称损失项以处理类别不平衡。仓库提供模块化脚本：模型定义、自定义损失、数据增强、EEG/fNIRS 特征提取、信号分帧与带通滤波。README 未给出安装命令，仅提示需自行安装依赖；引用 Journal of Neural Engineering 2024 论文并列出所用公开数据集。

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

- LSTM 与时序卷积层中引入注意力机制的 TAFN 模型
- 组合类别权重与非对称损失项的自定义损失函数
- EEG/fNIRS 特征提取、信号分帧、带通滤波等模块化脚本
- 基于多个公开数据集（Shin、Buccino 等）的论文配套实现

## 适用场景

- 复现 EEG-fNIRS 认知/运动意图分类的论文结果
- 在公开脑机接口数据集上训练时序注意力融合模型
- 复用 EEG/fNIRS 信号预处理与特征提取模块

## 场景标签

 · 领域:生物医学信号处理/脑机接口

## 证据(README 行号)

> L4: This study proposes a novel temporal attention fusion network (TAFN) with a custom loss function. The TAFN model inc
> L11: 1. **Model.py**: Defines a deep learning TAFN model suitable for EEG and fNIRS data.

## 星数曲线

```mermaid
xychart-beta
    title "yiamcb/TAFN 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `0c06ccea41bf` · [字段定义](../../DATASET.md)*
