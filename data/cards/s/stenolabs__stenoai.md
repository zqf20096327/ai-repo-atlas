# stenolabs/stenoai

⭐ 1,399 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/stenolabs/stenoai) · [官网](https://stenoai.co/) · 组织维护

**面向机密对话的本地 AI 会议记事本，隐私优先**

隐私优先的 AI 会议记事应用：录制会议后在本地完成转录、说话人分离、摘要与问答，默认本地 AI 处理，云端模型为可选项。转录默认使用 Parakeet TDT v3（Apple Silicon MLX），摘要后处理支持 Whisper（99 种语言）；提供实时说话人标签、自动检测会议、聊天问答、图表生成、Cookbook 报告模板、Markdown 导出与 MCP 服务器（供 Claude/Cursor 等读取会议记录）。支持 macOS、Windows（alpha）与 Linux。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 AI 默认处理录音、转录与摘要，外部 provider 可选
- Parakeet TDT v3 实时转录（Apple Silicon），Whisper 支持 99 种语言
- 通过 MCP 服务器向 Claude、Cursor、Codex 等提供只读会议访问
- Actions 连接 Linear、Notion、Jira 等，需逐项批准执行

## 适用场景

- 政府/国防等机密场景下录制并本地摘要会议
- 会议中实时查看带说话人标签的转录
- 用自然语言询问历史会议记录并生成行动项
- 将会议笔记同步到 Obsidian 等 Markdown 工作流

## 场景标签

`语音识别` `知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L15:  StenographAI is a privacy-first AI notepad for confidential conversations. Record, summarise, and query meetings w
> L42: - **Privacy-first**: local AI processes your recordings, transcripts, and summaries on your device. External AI pro
> L43: - **Live speaker labels** — Real-time on-screen text as you speak via Parakeet TDT v3 on Apple Silicon (MLX). Grano

## 星数曲线

```mermaid
xychart-beta
    title "stenolabs/stenoai 星数(近 25 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-28"]
    y-axis "stars" 1343 --> 1404
    line [1348, 1349, 1350, 1349, 1350, 1351, 1353, 1355, 1348, 1356, 1357, 1358, 1377, 1378, 1381, 1383, 1388, 1390, 1391, 1392, 1393, 1394, 1395, 1398, 1399]
```

2026-10-26 1,348 → 2026-11-28 1,399（+51）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `a61dce82bf71` · [字段定义](../../DATASET.md)*
