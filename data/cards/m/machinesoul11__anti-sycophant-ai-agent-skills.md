# machinesoul11/anti-sycophant-ai-agent-skills

⭐ 34 · MIT · 推送 2026-07-20 · [GitHub](https://github.com/machinesoul11/anti-sycophant-ai-agent-skills) · 个人维护

**三个让 AI 助手不再默认附和的产品创意检验技能**

面向 Claude、Gemini、Codex/ChatGPT、Cursor 等接受系统提示或规则文件的 AI 助手的技能包，包含三个 SKILL.md 文件：prove-the-premise 在动手前压测创意前提并指出缺失买家，hobby-or-business 区分兴趣项目与有真实买家的生意，one-real-conversation 拒绝点赞/问卷等验证表演并推动与真实潜在买家对话。每个技能在 frontmatter 中写明触发条件与关闭条件。以纯 Markdown 文件分发，按工具各有安装文档，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个技能按触发短语自动激活，各带明确关闭开关
- 技能为纯 Markdown SKILL.md 文件，可嵌入任意规则/系统提示工具
- 提供 /validate-idea 与 /reality-check 两个斜杠命令入口
- README 给出 30 秒安装验证方法与通过/失败判据

## 适用场景

- 让 AI 助手在我提出产品创意时先质疑前提而非直接给技术栈
- 区分自己是在做兴趣项目还是在做有买家的生意
- 避免用点赞数、问卷和 AI 角色扮演代替真实用户对话

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L16: This pack ships three skills that interrupt that default. They work in Claude, Gemini, Codex/ChatGPT, Cursor, and a
> L143: Every skill is one file: `skills/<name>/SKILL.md`, with YAML frontmatter on top.

## 星数曲线

```mermaid
xychart-beta
    title "machinesoul11/anti-sycophant-ai-agent-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-28 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `388d79b89ea8` · [字段定义](../../DATASET.md)*
