# NakamuraIA/HanaNakamura-VTuber-OSS

⭐ 30 · Python · AGPL-3.0 · 推送 2026-08-28 · [GitHub](https://github.com/NakamuraIA/HanaNakamura-VTuber-OSS) · 个人维护

**本地运行的 AI VTuber 助手：说话、听话、有记忆，数据不出机器**

面向终端用户的桌面 AI 伴侣应用：Python 后端 + React/Tauri 前端，支持语音（TTS/STT）、Live2D 风格 VTuber 形象、终端/文件/屏幕操作等 33 个工具，可接入 Discord。核心机制是三层记忆：短-term 对话、长-term 事实（FTS5/BM25 RAG 检索）、固定规则，存于本地 SQLite，备份即复制 runtime 目录。LLM 可选 DeepSeek/Gemini/Groq/OpenRouter/Qwen/Maritaca 等，TTS 含免费的 Edge。API 仅监听 127.0.0.1，AGPL-3.0-only，角色商标另行保护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三层记忆架构（短/长/固定）存于本地 SQLite，长记忆用 FTS5/BM25 做 RAG
- 33 个工具：终端命令、文件读写、屏幕感知、TTS/STT、图像生成、Discord 应答
- Skills 自学习：使用中把经验笔记写回技能文档
- 多 provider 可切换（LLM/语音/搜索），统一思考控制旋钮

## 适用场景

- 在本机运行一个有持续记忆的 AI 伴侣/VTuber
- 通过对话让 AI 代为执行终端命令与文件操作
- 在 Discord 上与自己的本地 AI 对话

## 场景标签

`AI 助手` `聊天机器人` `语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L23: Você baixa. Roda. E ela **te conhece** — porque a memória dela é um arquivo no
> L105: |💬 **Curta**|a conversa recente|automático|as últimas N falas, **isoladas por canal**|
> L215: |DeepSeek · Gemini · Groq|Edge _(grátis, sem chave)_|Tavily|

## 星数曲线

```mermaid
xychart-beta
    title "NakamuraIA/HanaNakamura-VTuber-OSS 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-31 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `3a60de5d3547` · [字段定义](../../DATASET.md)*
