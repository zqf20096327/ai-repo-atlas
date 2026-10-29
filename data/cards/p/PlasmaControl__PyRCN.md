# PlasmaControl/PyRCN

⭐ 100 · Python · BSD-3-Clause · 推送 2026-07-22 · [GitHub](https://github.com/PlasmaControl/PyRCN) · 组织维护

**储备计算 Python 框架：实现 ESN/ELM 的分类与回归**

轻量级 Python 3 储备计算（Reservoir Computing）框架，基于 numpy/scipy 等科学计算包，API 完全兼容 scikit-learn，现有 scikit-learn 代码无需重构即可调用其估计器，也可直接使用 scikit-learn 的参数优化与示例数据集。当前实现 Echo State Networks（ESN）与 Extreme Learning Machines（ELM）的 Classifier/Regressor 变体，开发方向包括与 sktime/hmmlearn 交互及 LSM、PNN 等架构。已被 TU Dresden 与 Ghent 大学团队用于音乐信息检索、时间序列预测、语音与音素识别等研究任务，提供 pip 安装、示例 Notebook 与 Binder 在线运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- API 完全兼容 scikit-learn，可复用其参数优化与数据集
- 实现 ESN 与 ELM 的 Classifier/Regressor 变体
- 提供 Jupyter Notebook 示例与 Binder 在线运行入口
- 配套多篇音乐信息检索与时间序列方向的发表论文

## 适用场景

- 在手写数字识别、Mackey-Glass 等时序任务上训练 ESN/ELM 模型
- 复用已有 scikit-learn 流水线替换估计器为储备计算模型
- 音乐多音高追踪、音符起始检测等音频研究实验

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L7: PyRCN ("Python Reservoir Computing Networks") is a light-weight and transparent Python 3 framework for Reservoir Com
> L14: Currently, it implements Echo State Networks (ESNs) by Herbert Jaeger and Extreme Learning Machines (ELMs) by Guang

## 星数曲线

```mermaid
xychart-beta
    title "PlasmaControl/PyRCN 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 99 --> 101
    line [100, 100]
```

2026-10-18 100 → 2026-10-29 100（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `b0dc9bcbd8e3` · [字段定义](../../DATASET.md)*
