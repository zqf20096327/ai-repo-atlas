# 0xchamin/mcptube

⭐ 163 · Python · 推送 2026-04-13 · [GitHub](https://github.com/0xchamin/mcptube) · [官网](https://0xchamin.github.io/mcptube/) · 个人维护

**将 YouTube 视频转为可复利积累的知识库的 MCP 服务器**

mcptube-vision 把 YouTube 视频转化为持久化结构化 wiki：摄取时提取字幕（youtube-transcript-api/yt-dlp）、用 ffmpeg 场景切换检测抽帧并交视觉 LLM 描述，再由 LLM 提取 video/entity/topic/concept 四类知识对象写入 JSON 文件与 SQLite FTS5 索引；查询走两阶段——FTS5 关键词检索加 LLM/客户端模型推理合成带引用的回答。以 MCP 服务器与 CLI 双形式提供，供 Claude、Copilot、Gemini 等 MCP 客户端调用；需 Python 3.12/3.13 与 ffmpeg，视觉与摄取阶段需自带 API key（Anthropic/OpenAI/Google）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 字幕 + 场景切换帧视觉分析双信号摄取，构建持久 wiki
- 四类知识对象与 append-only 合并语义，知识随视频积累
- FTS5 全文检索 + LLM agent 两阶段混合检索
- MCP 服务器采用 passthrough 模式，客户端模型负责推理，无需服务端 API key

## 适用场景

- 把收藏的 YouTube 教程/讲座沉淀为可检索、可交叉综合的知识库
- 在 Claude/Copilot 等 MCP 客户端中对话式查询视频内容
- 导出 wiki 为 markdown/HTML 做知识整理

## 场景标签

`知识库管理` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L136: #### 5. MCP Server
> L138: Exposes all subsystems as tools consumable by any MCP-compatible client. Report and synthesis tools use a **passth
> L80: In CLI mode (BYOK), the agent is an LLM call that synthesizes the final answer with source citations. In MCP server

## 星数曲线

```mermaid
xychart-beta
    title "0xchamin/mcptube 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 161 --> 164
    line [162, 163, 163]
```

2026-10-18 162 → 2026-10-24 163（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b9a12c3cc388` · [字段定义](../../DATASET.md)*
