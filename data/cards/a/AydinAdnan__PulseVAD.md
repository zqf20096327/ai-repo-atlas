# AydinAdnan/PulseVAD

⭐ 64 · Python · MIT · 推送 2026-09-09 · [GitHub](https://github.com/AydinAdnan/PulseVAD) · [官网](https://pypi.org/project/pulsevad/) · 个人维护

**面向微控制器的超小流式语音活动检测模型（2,118 参数）**

PulseVAD 是一个 2,118 参数的严格因果流式语音活动检测器（VAD），读取 16 kHz 单声道音频，以 200 ms 无前瞻窗口输出语音活动判定与时间戳。训练路线为 81k 教师网络 + DepGraph 结构化剪枝 + 知识蒸馏 + 先验偏置校准 + INT8 量化，权重量 2.1 KB。交付形态含 ONNX（INT8/FP32）、TorchScript、PyTorch state dict 与零依赖 C 头文件（面向 ARM Cortex-M、ESP32、STM32、Arduino）。README 同时列明劣势：纯音乐误报率 33%、远场混响环境低于 Silero、200 ms 粒度、需自备 FFT+mel 前端。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 2,118 参数 / 2.1 KB INT8 权重，200 ms 严格因果窗口、零前瞻
- 交付 ONNX、TorchScript、PyTorch state dict 与零依赖 C 头文件（pulsevad_weights.h）
- 提供 get_speech_timestamps 长音频语音区间扫描与实时流式预测接口
- 标注边界：音乐误报 33%、远场噪声低于 Silero、需 64 log-mel 前端

## 适用场景

- 在 SRAM 受限的微控制器上做流式语音活动检测
- 实时通话、语音消息、听写等近讲场景减少 ASR 空转触发
- 长音频文件中定位语音区间生成时间戳

## 场景标签

 · 领域:语音处理/边缘 AI

## 证据(README 行号)

> L3: **27 KB shipped. the smallest neural VAD that actually works.** 2,118 parameters - 2.1 KB of INT8 weights, 26.8 KB a
> L126: Pulsevad takes raw 16 kHz mono audio, computes a 64-channel log-mel spectrogram over a 200 ms causal window, and r

## 星数曲线

```mermaid
xychart-beta
    title "AydinAdnan/PulseVAD 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 62 --> 65
    line [63, 64, 64]
```

2026-10-18 63 → 2026-10-31 64（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b6cc402c32d9` · [字段定义](../../DATASET.md)*
