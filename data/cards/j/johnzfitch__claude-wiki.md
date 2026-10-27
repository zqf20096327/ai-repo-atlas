# johnzfitch/claude-wiki

⭐ 24 · NOASSERTION · 推送 2026-10-24 · [GitHub](https://github.com/johnzfitch/claude-wiki) · [官网](https://www.platform.claude.com) · 个人维护

**Anthropic Claude 官方文档的非官方 Markdown 镜像，供检索与模型上下文使用**

将 Claude API 平台、Claude Code、Agent SDK、MCP、帮助中心、新闻与研究等页面对应为每页一个 .md 文件的镜像库，带 YAML frontmatter（source_url/fetched_at 等），按 22 个编号主题目录组织。每目录含 INDEX.md 与 llms.txt（拼接全文，可直接放入模型上下文），顶层提供 TAGS.md、7/90 天变更日志及 tags/crossrefs/manifest/changelog 四个 JSON 文件。上游每日定时同步，内容归 Anthropic 条款所有，非官方、无 Anthropic 背书。通过 git clone 获取，适合 grep、diff、RAG 索引或直接投喂模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每上游页面一个 .md 文件，含 source_url/fetched_at frontmatter
- 每类目录提供 llms.txt 单文件拼接版，可直接放入模型上下文
- TAGS.md 与 tags/crossrefs/manifest/changelog 四个机器可读 JSON 索引
- 定时任务每日检查上游并以 Sync commits 发布变更

## 适用场景

- 离线阅读与 grep 检索 Claude 全部官方文档
- 为 RAG 系统提供带来源引用的文档语料（按标题分块、保留 source_url 元数据）
- 快速为单主题查询组装 LLM 上下文（llms.txt）

## 场景标签

 · 领域:AI 文档/知识聚合

## 证据(README 行号)

> L1: # Claude Wiki
> L3: An unofficial Markdown mirror of Anthropic's Claude documentation: the Claude API platform docs, Claude Code docs, t

## 星数曲线

```mermaid
xychart-beta
    title "johnzfitch/claude-wiki 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `8a23c8a6e146` · [字段定义](../../DATASET.md)*
