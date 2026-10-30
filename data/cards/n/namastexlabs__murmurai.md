# namastexlabs/murmurai

⭐ 46 · Python · MIT · 推送 2025-12-17 · [GitHub](https://github.com/namastexlabs/murmurai) · [官网](https://pypi.org/project/murmurai) · 组织维护

**自托管 GPU 转录 API 服务：音频转文字并带说话人分离**

由 Namastex Labs（自称研究实验室）维护的自托管转录 REST API：封装其维护的 WhisperX 分支 murmurai-core，提供说话人分离（pyannote，需 HuggingFace token）、词级时间戳、SRT/WebVTT/TXT/JSON 导出、异步后台任务与 webhook 回调。自称可替代 AssemblyAI、Deepgram、Rev.ai 等付费转录 API。要求 NVIDIA GPU 6GB+ VRAM 与 CUDA 12.x（有 CPU 测试模式），支持 uvx 一键运行、pip、Docker 等安装方式。默认 API key 公开，网络暴露部署需自行更换。

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

- WhisperX 分支核心 + pyannote 说话人分离
- SRT/WebVTT/TXT/JSON 多格式导出与 webhook 回调
- 异步后台任务与进度轮询 API
- audio_url 参数带 SSRF 防护（拦截内网 IP 与云元数据端点）

## 适用场景

- 替换付费转录 API，在自有 GPU 服务器上跑批量音频转写
- 为访谈、会议录音生成带说话人标签和时间戳的字幕
- 通过 REST API 集成到自动化转录流水线

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L30: MurmurAI wraps murmurai-core (our WhisperX fork) in a REST API with speaker diarization, word-level timestamps, and
> L34: - **Speaker Diarization** - Identify who said what with pyannote

## 星数曲线

```mermaid
xychart-beta
    title "namastexlabs/murmurai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-30 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1c71d5b4c897` · [字段定义](../../DATASET.md)*
