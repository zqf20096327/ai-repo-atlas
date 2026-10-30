# virtualsteve-star/chat-playground

⭐ 41 · JavaScript · MIT · 推送 2026-05-30 · [GitHub](https://github.com/virtualsteve-star/chat-playground) · [官网](https://virtualsteve-star.github.io/chat-playground/) · 个人维护

**浏览器端 LLM 安全实验场：本地试聊天模型与 guardrails**

零依赖的 HTML/JavaScript 单页应用，配合《The Developer's Playbook for LLM Security》与 OWASP Top 10 for LLM Applications 使用。提供多种聊天模型（本地 ELIZA 式 SimpleBot、OpenAI、Google Gemini，部分模型内置漏洞供测试）、多种 UI 风格、可选输入/输出过滤器（黑名单、正则、限流及 AI 审核），并附含数百条样本提示词的过滤器自动化测试套件与 5 个递进式实验的学习手册。API key 仅存于浏览器本地。克隆仓库后用 python3 http.server 打开 index.html 即可运行。

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

- 零依赖浏览器运行，SimpleBot 本地模型无需 API key 与联网
- 输入/输出双层 guardrails（本地规则过滤与 OpenAI Moderation 等 AI 过滤）
- 部分模型内置漏洞与后门，供安全实验使用
- 含 100 风险+100 良性样本/类别的 guardrails 自动化测试套件

## 适用场景

- 动手实验 prompt injection 与内容过滤等 LLM 安全概念
- 在不写后端代码的情况下对比不同 guardrails 与人格配置的效果
- 测试不同聊天 UI 风格对用户体验的影响

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: A companion project to The Developer's Playbook for Large Language Model Security and the OWASP Top 10 for LLM Appli
> L123: When a user submits a message, it first passes through a series of configurable **Input Filters** (guardrails) tha
> L136: You can run these tests directly in your browser to evaluate the effectiveness of each filter, compare results, an

## 星数曲线

```mermaid
xychart-beta
    title "virtualsteve-star/chat-playground 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-30 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3ddc423548fc` · [字段定义](../../DATASET.md)*
