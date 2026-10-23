# M3-org/discord-summarizer

⭐ 97 · Python · 推送 2025-12-07 · [GitHub](https://github.com/M3-org/discord-summarizer) · 组织维护

**用本地 LLM 分析 Discord 聊天导出并生成摘要的 Python 脚本**

读取 Discord 聊天导出 JSON，经分块后调用通过 Ollama 运行的本地 LLM（默认 phi3-chat），生成结构化 Markdown 报告：技术讨论摘要、FAQ 汇编、求助互动跟踪与分类行动项（技术任务/文档需求/功能请求）。提供 rich CLI 进度显示、CTRL+C 优雅退出与分块错误恢复。使用需自备 Ollama 与模型，通过 pip 安装依赖后以命令行运行；Modelfile 默认配置为 Linux 系统，其他系统需自行修改。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分块处理 Discord 导出并生成分类摘要报告
- 经 Ollama 运行本地模型（默认 phi3-chat），不依赖云端 API
- Markdown 结构化输出：摘要/FAQ/求助互动/行动项
- 提供 DiscordChatExporter JSON 的预处理脚本以压缩 token

## 适用场景

- 社区管理员回顾 Discord 频道讨论并提取行动项
- 从历史聊天中汇总常见问答供文档使用
- 本地离线分析聊天记录，不外发数据

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: A powerful Python script that analyzes Discord chat exports and generates comprehensive summaries using local LLM mo
> L15:  - Uses local LLM models via Ollama

## 星数曲线

```mermaid
xychart-beta
    title "M3-org/discord-summarizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 96 --> 98
    line [97, 97]
```

2026-10-18 97 → 2026-10-23 97（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d10c85375dc5` · [字段定义](../../DATASET.md)*
