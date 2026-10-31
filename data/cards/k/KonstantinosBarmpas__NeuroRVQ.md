# KonstantinosBarmpas/NeuroRVQ

⭐ 54 · Python · NOASSERTION · 推送 2026-08-06 · [GitHub](https://github.com/KonstantinosBarmpas/NeuroRVQ) · [官网](https://neurorvq.github.io) · 组织维护

**面向 EEG/EMG/ECG/PPG 的多尺度生物信号分词器与基础模型**

NeuroRVQ 是官方实现的多尺度生物信号分词器家族：将 EEG/EMG/ECG/PPG 多变量时序经多尺度时序卷积分解为频率特异表示，编码为分层 RVQ 码本生成神经 token，并用相位感知损失保持 Fourier 相位信息，可高保真重建输入信号。配套为每种模态训练掩码 token 预测基础模型（NeuroRVQ-FM，6M 参数），可迁移到下游 BCI 任务。预训练模型托管于 HuggingFace，通过 conda 环境与 pip 安装依赖运行，提供各模态分词与微调示例代码。

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

- 多尺度时序卷积 + 分层 RVQ 码本的信号分词，支持 EEG/EMG/ECG/PPG 四种模态
- 相位感知训练损失，保持 Fourier 相位的循环拓扑
- 各模态配套 6M 参数掩码 token 预测基础模型，可微调迁移到下游 BCI 任务
- 预训练模型（76M/144M 分词器）从 HuggingFace 下载

## 适用场景

- 对 EEG/EMG/ECG/PPG 信号做 token 化与高保真重建
- 在运动想象、ERP、睡眠分期等下游 BCI 任务上微调基础模型
- 作为生成式基础模型研究的生物信号分词组件

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L17: This is the official implementation of **NeuroRVQ**, a foundation model for biosignals powered by a state-of-the-ar
> L23: Biosignals such as electroencephalography (EEG), electrocardiography (ECG), and electromyography (EMG) encode physi
> L27: **NeuroRVQ Foundation Model** operates on the tokenized representation, using masked-token prediction with symmetri

## 星数曲线

```mermaid
xychart-beta
    title "KonstantinosBarmpas/NeuroRVQ 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-31 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `e794f0c87490` · [字段定义](../../DATASET.md)*
