# SakethKanchi/parley

⭐ 33 · JavaScript · ISC · 推送 2026-10-07 · [GitHub](https://github.com/SakethKanchi/parley) · [官网](https://sakethkanchi.github.io/parley-landing/) · 个人维护

**自托管 Discord 会议机器人：本地按说话人转录并生成结构化 AI 笔记**

基于 Node.js（discord.js）与 Python faster-whisper sidecar 的自托管 Discord 语音会议记录机器人。利用 Discord 每用户独立音频流实现精确按说话人归属（无需 ML 说话人分离），会议结束后本地转录、合并为带时间戳的说话人标记文稿，送入可插拔的摘要器（Gemini 默认、OpenAI 兼容端点或离线 Ollama），将 TL;DR、议题、决议、行动项与发言时长统计发布到 Discord 讨论串，并附带自托管 Web 管理面板（浏览/搜索/看板/配置）。支持 Docker Compose 一键部署，仅转录文本离开本机。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | ISC |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Discord 独立音频流实现精确按说话人归属，无需 ML 说话人分离
- 可插拔摘要器：Gemini / OpenAI 兼容端点 / 离线 Ollama，按服务器切换
- 本地 faster-whisper sidecar：NVIDIA GPU 自动加速（5–15x）、批处理推理、CPU 回退
- Docker Compose 一键运行机器人 + whisper sidecar + 仪表盘，SQLite FTS5 全文检索

## 适用场景

- 团队在 Discord 语音会议后自动获得结构化纪要与行动项
- 不想用 SaaS 会议笔记服务，自托管并保留全部数据
- 离线场景：本地 whisper + Ollama 实现零云端依赖

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L3:  Parley records your Discord voice meetings, transcribes them per-speaker on your own machine,
> L28:  A live voice meeting becomes a per-speaker transcript, then structured notes — TL;DR, decisions, action items, tal
> L66: - **Pluggable summarizer.** Google Gemini (default, free tier), any OpenAI-compatible endpoint, or fully-offline Ol

## 星数曲线

```mermaid
xychart-beta
    title "SakethKanchi/parley 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-28 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `38bcba3f0618` · [字段定义](../../DATASET.md)*
