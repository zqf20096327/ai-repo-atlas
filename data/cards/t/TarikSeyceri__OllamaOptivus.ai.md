# TarikSeyceri/OllamaOptivus.ai

⭐ 20 · JavaScript · MIT · 推送 2026-04-30 · [GitHub](https://github.com/TarikSeyceri/OllamaOptivus.ai) · 个人维护

**视频分析 AI 服务：OCR/物体检测/语音转录后经 Ollama 生成摘要**

基于 Node.js/Express 与 Python 的视频处理 API 服务：上传 .mp4 后，用 FFmpeg 抽取音频、Whisper 转录语音、OpenCV 逐帧抽取画面、YOLOv8 检测物体、EasyOCR 识别帧内文字，再将结果组装为提示词发送给本地 Ollama LLM（默认 deepseek-r1，支持 llama3.2 等），按可自定义的 JSON schema 返回摘要与事件。支持 Docker 或手动安装（Node v18 + Python 3.11 + ffmpeg），提供上传/列表/删除/处理 REST 端点、文件保留期定时清理与日志轮转。转录语言当前仅支持英语和土耳其语。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Whisper 语音转录 + YOLOv8 物体检测 + EasyOCR 帧内文字识别的组合视频分析管线
- 分析结果转发 Ollama LLM 生成摘要，模型可配置（默认 deepseek-r1）
- REST API（上传/列表/删除/处理），支持 Swagger 文档与自定义 JSON 响应 schema
- 定时清理过期视频/音频/中间文件（默认保留 2 天）

## 适用场景

- 通过 API 上传视频并获取内容摘要与事件分析
- 批量处理监控或通话录像并结构化提取信息
- 在本地 Ollama 环境下私有化运行视频理解服务

## 场景标签

`语音识别` `目标检测` `OCR` · 领域:感知与多模态

## 证据(README 行号)

> L7: Ollama Optivus is a video processing AI based solution designed to analyze and extract meaningful information from v
> L25: 3. **Audio Transcription**: Whisper transcribes the extracted audio to text.
> L29: 5. **Object Detection**: YOLOv8 detects objects in each frame of the video.
> L31: 6. **Text Detection**: EasyOCR detects any text in each frame.

## 星数曲线

```mermaid
xychart-beta
    title "TarikSeyceri/OllamaOptivus.ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `0b1d83cd34e7` · [字段定义](../../DATASET.md)*
