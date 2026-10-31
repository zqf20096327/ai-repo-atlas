# machinelearningZH/audio-transcription

⭐ 102 · Python · MIT · 推送 2026-08-19 · [GitHub](https://github.com/machinelearningZH/audio-transcription) · 组织维护 · 中文 README

**本地部署的音频/视频转写工具，带 HTML 转写编辑器**

面向苏黎世州行政机关等机构的自托管转写应用：用 Whisper v3 large（非量化）模型在本地 GPU 上转写音频/视频文件，支持说话人分离（pyannote）、自定义热词、多文件上传，输出 TXT/SRT/HTML 及与音视频同步的浏览器编辑器。提供 REST API 供程序化调用，可选接入本地 llama-cpp-python 语言模型做摘要。推荐 CUDA 显卡（8GB 起 VRAM），需 conda 环境、ffmpeg 与 Hugging Face 访问令牌，也提供 Docker 安装方式；MacOS MPS 路径存在内存泄漏问题需重启 worker。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Whisper v3 large 非量化模型本地转写，支持瑞士德语
- 说话人分离与编辑器内说话人命名、片段增删
- 输出 TXT/SRT/HTML，编辑器与源音视频同步播放
- REST API：上传转写、查询状态、下载结果，可选 API key 鉴权

## 适用场景

- 我需要对机密录音/会议做本地转写而不外传数据
- 为视频生成字幕并在同步编辑器里校对说话人与文本
- 通过 API 把转写能力集成进自己的应用流程

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L209: - Speaker Diarisation: Automatic identification and differentiation of speakers within the audio.

## 星数曲线

```mermaid
xychart-beta
    title "machinelearningZH/audio-transcription 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 101 --> 103
    line [102, 102]
```

2026-10-18 102 → 2026-10-31 102（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `42f7708d51e8` · [字段定义](../../DATASET.md)*
