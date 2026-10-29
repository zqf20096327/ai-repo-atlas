# Mekopa/whisperx-blackwell

⭐ 37 · Python · MIT · 推送 2026-04-23 · [GitHub](https://github.com/Mekopa/whisperx-blackwell) · 个人维护

**让 WhisperX 在 NVIDIA Blackwell GPU 上运行的 Docker 补丁镜像**

针对 NVIDIA Blackwell（SM_121，如 DGX Spark GB10）上 NVRTC 不识别新架构导致 WhisperX/Pyannote GPU 失败的问题，提供 Dockerfile 补丁：将 PyTorch 的 get_device_capability 伪装为 Hopper (9,0)，并改写 torchaudio 源码绕过 Jiterator 路径，使 SM_90 代码在 SM_121 上原生执行。镜像内运行 WhisperX 批处理服务，提供 /transcribe HTTP API，输出词级时间戳、说话人标签与置信度。面向持有 Blackwell 硬件的开发者，属临时方案，NVRTC 官方支持后即过时。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 架构伪装补丁使 SM_90 代码在 Blackwell SM_121 上运行
- 绕过 torchaudio Jiterator 的源码改写
- 提供预构建 Docker 镜像与 /transcribe / /health HTTP API
- 支持 GPU 说话人分离（pyannote），需 HF token

## 适用场景

- 在 DGX Spark 等 Blackwell 设备上运行 GPU 加速语音转录与说话人分离
- 解决 nvrtc: invalid value for --gpu-architecture 报错
- 通过 HTTP API 批量转录音频并获取词级时间戳

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L24: This repository contains the **"Blackwell Bridge Patch"** - a surgical Dockerfile fix that:
> L81: curl -X POST "http://localhost:8003/transcribe" \
> L88: - Word-level timestamps

## 星数曲线

```mermaid
xychart-beta
    title "Mekopa/whisperx-blackwell 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-29 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9519fcc5288c` · [字段定义](../../DATASET.md)*
