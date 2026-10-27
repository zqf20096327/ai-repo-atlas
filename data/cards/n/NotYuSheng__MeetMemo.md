# NotYuSheng/MeetMemo

⭐ 34 · Python · MIT · 推送 2026-09-13 · [GitHub](https://github.com/NotYuSheng/MeetMemo) · [官网](https://notyusheng.github.io/MeetMemo/) · 个人维护

**离线会议转写 Web 应用：语音转文字、说话人分离与摘要**

完全在本地运行的会议转写 Web 应用：浏览器录音或上传音频，用 faster-whisper（CTranslate2）转写，PyAnnote.audio 做说话人分离，再接入 OpenAI 兼容的本地 LLM 服务（如 LM Studio、Ollama）生成要点与行动项摘要。导出 PDF/Markdown，自带 HTTPS 与 PostgreSQL。通过 Docker Compose 部署，GPU 可选（有 CPU 回退），按 VRAM 自动选择硬件档位；需接受 Hugging Face 模型许可并配置 HF token。

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

- faster-whisper 转写，支持 99+ 语言与自动语言检测
- PyAnnote.audio 说话人分离与时间戳同步播放
- 接入任意 OpenAI 兼容 API（LM Studio/Ollama）做自定义摘要
- Docker Compose 一键部署，按 VRAM 自动选择 cpu/low/balanced/high 档位

## 适用场景

- 会议/访谈/讲课录音本地转写并生成摘要
- 在数据不出内网的前提下处理音频
- 导出带说话人标签的专业 PDF/Markdown 纪要

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L18: A meeting transcription application that runs entirely offline. It converts speech to text, identifies different sp
> L27: |**Speech Recognition**|faster-whisper with CTranslate2 (4x speedup, 99+ languages)|
> L45: |LLM Server|Any OpenAI-compatible API|Summarization (e.g., LM Studio, Ollama, OpenAI)|

## 星数曲线

```mermaid
xychart-beta
    title "NotYuSheng/MeetMemo 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-27"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-27 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c0d7826e6b59` · [字段定义](../../DATASET.md)*
