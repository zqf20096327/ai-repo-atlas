# srezai-team/srezai-web-search-pro-skill

⭐ 3 · JavaScript · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/srezai-team/srezai-web-search-pro-skill) · [官网](https://srezai.ru/docs/mcp) · 组织维护 · 中文 README

**给 AI agent 提供 web 搜索/读取/验证的技能与 CLI**

为 Claude Code、Cursor、Codex 等 agent 提供六个 SKILL.md 技能与零依赖 CLI，通过 srezai web API 实现网页搜索、页面/PDF/Office 文件读取、站点抓取、schema 抽取、带引用的声明核查、综合回答、deep research 与 YouTube 字幕。相比 MCP 全量 schema 每请求约 10.8k token，技能描述合计约 440 token，CLI 将工具 schema 移出上下文窗口。按 credit 计费（1 credit=0.10 ₽），支持免费试用与注册获取 key；Runet（俄语 web）覆盖优先。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六个窄技能+CLI，将工具 schema 从上下文窗口移出（≈440 vs ≈10.8k token）
- verify_claim 逐条引用与页面原文比对，未验证内容如实标注
- 读取 PDF/Word/Excel/PowerPoint/EPUB 并转为 Markdown
- 无 shell 的宿主回退到 MCP（Claude Desktop、ChatGPT connectors、n8n）

## 适用场景

- 让 Claude Code 等编码 agent 直接搜索和读取网页
- 对事实声明做带引用的核查（fact-checking）
- 多步深度研究并输出带来源的成稿回答
- 获取 YouTube 视频字幕与摘要

## 场景标签

`网页抓取` `科研工具` · 领域:效率与自动化

## 证据(README 行号)

> L1: # srezai skills — web access for AI agents, without burning the context
> L3: Six narrow skills plus a zero-dependency CLI for the srezai web API:
> L44: is not. CLI repo: srezai-team/srezai-cli.

## 星数曲线

```mermaid
xychart-beta
    title "srezai-team/srezai-web-search-pro-skill 星数(近 2 点)"
    x-axis ["2026-10-20", "2026-11-22"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-20 3 → 2026-11-22 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `97bfbb6152c4` · [字段定义](../../DATASET.md)*
