# weaiw/trove-ai

⭐ 187 · Python · NOASSERTION · 推送 2026-08-23 · [GitHub](https://github.com/weaiw/trove-ai) · [官网](https://github.com/weaiw/trove-ai) · 个人维护 · 中文 README

**面向中文互联网的自托管个人 AI 稍后读与知识库系统**

可自托管的知识管理 Agent：从微信公众号、知乎、抖音、小红书、B 站等中文平台抓取文章、视频与文件，经 trafilatura→无头 Chromium→BeautifulSoup 级联提取正文，存入 PostgreSQL+pgvector 私有库。Agent 支持基于个人库的 RAG 问答（带引用）、自动知识图谱、学习路径生成、经确认后的标签整理。提供微信/飞书 Bot 入口、单向 Obsidian 同步插件、多租户与 JWT 隔离。Docker Compose 部署，LLM 接任意 OpenAI 兼容服务，嵌入有本地 CPU 免费回退方案。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 微信公众号/视频号/知乎/抖音/B 站等 6+ 中文平台深度解析与多格式导入（PDF/DOCX/EPUB 等）
- 基于私有库的 RAG 问答带引用，自动生长的知识图谱与学习路径生成
- 微信/飞书 Bot 入口与 Obsidian 单向同步插件（MIT，配套仓库）
- LLM 接任意 OpenAI 兼容服务，嵌入支持本地 CPU-only 免费回退

## 适用场景

- 把收藏的中文公众号、知乎、B 站等内容积累成可检索的个人知识库
- 通过微信转发链接/文件/语音随手收藏并向 Agent 提问
- 自托管掌控数据，用 Obsidian 插件做本地备份

## 场景标签

`知识库管理` `RAG` `知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L22: **Trove AI is a self-hostable knowledge-management Agent.** The web assistant, WeChat Bot, and Feishu Bot share the
> L37: Ask *"What did I read about prompt engineering?"* → get answer with citations to **your** library, not the public i
> L159: |LLM|Any **OpenAI-compatible**|DeepSeek, 讯飞星辰, OpenAI, SiliconFlow, MiniMax, 智谱, ...|

## 星数曲线

```mermaid
xychart-beta
    title "weaiw/trove-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 186 --> 188
    line [187, 187]
```

2026-10-18 187 → 2026-10-27 187（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `3a090777e16b` · [字段定义](../../DATASET.md)*
