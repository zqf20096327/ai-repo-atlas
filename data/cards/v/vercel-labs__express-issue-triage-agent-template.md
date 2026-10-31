# vercel-labs/express-issue-triage-agent-template

⭐ 15 · TypeScript · Apache-2.0 · 推送 2026-06-17 · [GitHub](https://github.com/vercel-labs/express-issue-triage-agent-template) · 组织维护

**给开源维护者的 GitHub issue AI 分诊代理模板**

基于 Express 与 Vercel AI SDK 的模板项目：GitHub webhook 触发后校验签名，用 generateObject 按预定义 Zod schema 对新 issue 分类，再经 Octokit 打标签并发布维护者回复；判定为垃圾的 issue 只打标签不回复，失败时回退打 needs-triage 标签。应用无状态、无数据库，一键部署到 Vercel 单函数。默认模型经 Vercel AI Gateway 调用 claude-haiku-4.5（免费档），也可改用任意 Gateway 支持的模型或直连 Anthropic API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- webhook → generateObject 分类 → Octokit 打标签与回复的分诊流程
- Zod schema 约束分类输出，提示词与返回字段均可编辑
- 无状态、无数据库，一键部署为 Vercel 单函数
- 失败回退打 needs-triage 标签，不静默失败

## 适用场景

- 自动给新建 issue 打标签并生成维护者回复
- 自动识别并标注垃圾 issue
- 作为模板定制自己的 GitHub webhook AI 代理

## 场景标签

 · 领域:开发工具/AI 自动化

## 证据(README 行号)

> L3: An AI agent that triages new GitHub issues. When an issue is opened, a GitHub webhook calls this Express app, the AI
> L11:   → waitUntil: generateObject (AI SDK) classifies the issue

## 星数曲线

```mermaid
xychart-beta
    title "vercel-labs/express-issue-triage-agent-template 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `c372ef2c5aa9` · [字段定义](../../DATASET.md)*
