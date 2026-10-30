# afeef/zabt-ai

⭐ 21 · Python · AGPL-3.0 · 推送 2026-10-16 · [GitHub](https://github.com/afeef/zabt-ai) · [官网](https://zabt.ai) · 个人维护

**自托管 AI 会议智能：转录、说话人分离与 LLM 纪要**

部署在用户自有基础设施上的会议处理系统：上传录音或由机器人加入通话（Teams 可选），经 faster-whisper 转录、pyannote 说话人分离，再由任意 OpenAI 兼容模型生成摘要；提供带时间戳的说话人标注转录查看/编辑器、摘要模板、YouTube 链接导入、PDF 导出与邮件/Telegram 通知。面向希望数据不出本机的团队与个人。安装方式为 git clone 后 docker compose up，捆绑 Postgres/MinIO/转录 worker/Web UI；GPU 转录需 NVIDIA GPU，支持 CPU-only 与 RunPod 云端拆分拓扑，pyannote 权重需自行在 Hugging Face 接受条款下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- faster-whisper 转录 + pyannote 说话人分离生成标注转录
- 任意 OpenAI 兼容 LLM 端点（OpenRouter/Ollama/vLLM 等）生成摘要
- docker compose 单机部署，捆绑 Postgres/Redis/MinIO/Web UI
- 单机 / CPU-only / RunPod 云端拆分三种部署拓扑

## 适用场景

- 在自有服务器上转录并总结会议录音，数据不出本机
- 生成带说话人标签和时间戳的会议记录并导出 PDF
- 无 GPU 环境下以 CPU 模式或 RunPod 云端 GPU 完成转录

## 场景标签

`语音识别` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: **Self-hosted AI meeting intelligence.** zabt.ai transcribes, diarizes, and summarizes
> L6: let the bot join a call), and get an accurate, speaker-labeled transcript and an LLM-written

## 星数曲线

```mermaid
xychart-beta
    title "afeef/zabt-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `23b3c02185dc` · [字段定义](../../DATASET.md)*
