# crlandsc/torch-l1-snr

⭐ 45 · Python · MIT · 推送 2026-09-01 · [GitHub](https://github.com/crlandsc/torch-l1-snr) · 个人维护

**音频源分离训练用的 L1 SNR 损失函数 PyTorch 库**

面向音频源分离/增强模型训练者的 PyTorch 损失函数包：提供 L1SNRLoss（基于 arXiv:2309.02539）、带自适应电平匹配正则的 L1SNRDBLoss、多分辨率 STFT 频谱域变体以及时域+频域组合的 MultiL1SNRDBLoss。附加功能包括 l1_weight 混合标准 L1、grad_scale 梯度缩放、NaN/inf 处理与短音频回退。依赖 PyTorch 与 torchaudio，支持 CPU/CUDA/MPS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 种时域/频域 L1SNR 损失函数，基于 3 篇论文并含扩展
- l1_weight 混合标准 L1 以软化 SNR 类损失的全有全无行为
- grad_scale 梯度缩放与 dBRMS 电平匹配正则防止静音塌缩
- 兼容 (batch, samples)/(batch, channels, samples)/(batch, num_sources, channels, samples) 张量形状

## 适用场景

- 训练音频源分离模型时替换 L1/MSE/SI-SDR 损失
- 音乐分离（如鼓与人声）训练管线中组合时域与频域目标
- 防止模型在不确定时塌缩为静音输出

## 场景标签

 · 领域:音频/机器学习工具库

## 证据(README 行号)

> L5: L1 Signal-to-Noise Ratio (SNR) loss functions for audio source separation in PyTorch. This package provides four los
> L7: The core `L1SNRLoss` is based on the loss function described in [[1]](https://arxiv.org/abs/2309.02539). `L1SNRDBLos

## 星数曲线

```mermaid
xychart-beta
    title "crlandsc/torch-l1-snr 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-31 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4b8588fc726e` · [字段定义](../../DATASET.md)*
