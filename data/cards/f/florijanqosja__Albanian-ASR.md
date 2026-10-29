# florijanqosja/Albanian-ASR

⭐ 18 · Jupyter Notebook · MIT · 推送 2026-07-19 · [GitHub](https://github.com/florijanqosja/Albanian-ASR) · [官网](https://uneduashqiperine.com) · 个人维护

**阿尔巴尼亚语语音转写工具：ASR 转录与语音数据标注平台**

面向阿尔巴尼亚语的 AI 转写工具，包含标注与校验语音数据的 React Web 界面和处理音频的 FastAPI 后端。上传媒体经 ffmpeg 解码为 16kHz 单声道后，用 Silero VAD（内置 ONNX 模型，CPU 上经 onnxruntime 运行）检测语音段，组装为 1–15 秒的标注用话语并过滤静音/ clipping 段。标注语料可导出为 NeMo 风格 JSONL 或 LJSpeech 风格 CSV 训练清单，附数据集管理工具与训练 notebook。通过 Docker Compose 部署，需先配置 .env 环境变量。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 阿尔巴尼亚语自动语音识别
- Silero VAD（ONNX，CPU 运行，无 torch 依赖）做语音分段，输出 1–15 秒话语
- Web 界面标注与校验语音数据，含数据集管理工具
- 语料可导出为 NeMo JSONL / LJSpeech CSV 训练清单

## 适用场景

- 把阿尔巴尼亚语音频自动转写为文本
- 构建和标注阿尔巴尼亚语语音数据集
- 导出训练清单用于 ASR 模型训练

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L5: This project is an AI-based transcription tool for the Albanian language. It includes a web interface for labeling a
> L9: - Automatic speech recognition for Albanian language.

## 星数曲线

```mermaid
xychart-beta
    title "florijanqosja/Albanian-ASR 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `c57c4f21e665` · [字段定义](../../DATASET.md)*
