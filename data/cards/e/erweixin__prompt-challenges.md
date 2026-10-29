# erweixin/prompt-challenges

⭐ 51 · TypeScript · 推送 2026-04-10 · [GitHub](https://github.com/erweixin/prompt-challenges) · [官网](https://prompt-challenges.pages.dev) · 个人维护 · 中文 README

**面向普通用户的 LLM 提示词到 Agent 学习路径站点**

基于 Astro 5 构建的双语学习站点，内容为 Markdown 挑战题，按 foundation→prompt→tools→mcp→skills→harness 等阶段组织，覆盖清晰提示、工具使用、Cursor 式 IDE 协作、MCP、Skills 与 harness 驱动的本地 agent 工作流。练习页通过 POST /api/score 调用 OpenRouter（或 OpenAI 兼容接口）评分；部署面向 Cloudflare Pages（静态页 + Worker）。旧 Next.js 站点仅作参考归档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按 foundation→harness 阶段组织的双语挑战与练习内容
- Cloudflare Pages 部署（静态页 + /api/score Worker）
- 支持 OPENROUTER_API_KEY 与自定义 OpenAI 兼容 base URL

## 适用场景

- 普通用户系统学习从提示词到 agent 工作流的 LLM 技能
- 在本地或 Cloudflare 上运行带 LLM 评分的练习站点
- 中英双语学习 MCP、Skills 等本地 agent 相关主题

## 场景标签

`提示工程` `教程课程` · 领域:Agent 开发

## 证据(README 行号)

> L3: A **learning path** for everyday users: from one-shot chatbot queries to Cursor-style IDE collaboration and OpenClaw
> L5: - **Live content** lives in `src/content/challenges/` (Markdown + frontmatter; organized by `foundation → prompt → t
> L6: - **Learning resources** on the home page `#resources` are grouped by stage: structured prompting, tools / IDE colla

## 星数曲线

```mermaid
xychart-beta
    title "erweixin/prompt-challenges 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-29 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f893d1cc1fad` · [字段定义](../../DATASET.md)*
