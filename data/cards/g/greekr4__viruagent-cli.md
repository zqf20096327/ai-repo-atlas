# greekr4/viruagent-cli

⭐ 42 · JavaScript · MIT · 推送 2026-09-15 · [GitHub](https://github.com/greekr4/viruagent-cli) · 个人维护

**供 AI agent 调用的博客与社交平台自动发布 CLI**

面向 AI agent（非人类直接使用）的命令行工具：通过 CLI 命令加技能文件（viruagent.md）的方式，让 agent 编排登录、发布、点赞、评论、关注等操作，覆盖 Tistory、Naver Blog/Cafe、Instagram、X、Reddit、Threads 七个平台。技术栈包含 Playwright 浏览器自动化（仅 Tistory/Naver）、Instagram 纯 HTTP API、X 的 GraphQL 内部 API，并以 JSON 文件管理会话、按用户持久化速率限制计数。需 Node.js >= 18，通过 npx 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 7 个博客与社交平台的发布/互动操作
- 技能文件（viruagent.md）定义 agent 工作流，可自行编辑定制
- Playwright 浏览器自动化与纯 HTTP API 混合实现
- 按用户持久化速率限制计数器与随机延迟

## 适用场景

- 让 AI agent 代我在 Tistory/Naver Blog 写作并发布博文
- 通过对话指令批量点赞、评论、关注 Instagram/X 账号
- 自动化 Naver Cafe 加 入与发帖流程

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L14: **A CLI tool where AI agents write, publish, and engage across blog & social platforms automatically.**
> L16: Designed not for humans, but for **AI agents**.
> L32: Operates via **CLI + skill files**. The CLI handles the interface; the skill file (`viruagent.md`) instructs the AI

## 星数曲线

```mermaid
xychart-beta
    title "greekr4/viruagent-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-31 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ce29fbd79bf5` · [字段定义](../../DATASET.md)*
