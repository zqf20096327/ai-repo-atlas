# yan-yanko/rainman

⭐ 21 · Python · MIT · 推送 2026-08-23 · [GitHub](https://github.com/yan-yanko/rainman) · [官网](https://yan-yanko.github.io/rainman/) · 个人维护

**给 AI 编码工具的本地项目记忆层：按上下文召回经验**

面向使用 AI 编码助手的开发者的持久记忆层：通过 MCP 服务器与生命周期钩子接入 Claude Code、Cursor、VS Code/Copilot 等宿主，提供 recall/remember/context 等工具，将项目经验记忆在需要时注入上下文。检索不打 LLM 调用、无嵌入、零外部依赖（仅标准库），采用关键词/新近性/重要性/联想四分量打分、两阶段检索、ACT-R 幂律衰减与自动关联图。存储分全局与项目两层，自动脱敏密钥、去重并标注来源；团队同步服务器独立仓库（BSL 1.1）为可选。需 Python 3.10+。

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

- 零 LLM 调用、零外部依赖的本地记忆与检索（关键词/新近性/重要性/联想打分）
- MCP 服务器 + Claude Code 钩子实现跨会话自动学习与压缩恢复时重注入
- 分层存储（全局/项目）、自动链接、自动情感分类与来源溯源
- 密钥自动脱敏，.rainman/ 可提交 git 团队共享

## 适用场景

- 让 Claude Code 等 AI 编码助手记住我修复过的 bug 与架构决策
- 长会话上下文压缩后自动恢复相关记忆
- 团队共享同一仓库的项目记忆（可选自托管同步）

## 场景标签

 · 领域:开发者工具/AI 编码基础设施

## 证据(README 行号)

> L21: Rainman fixes this. It's a persistent memory layer with contextual retrieval that plugs into AI coding workflows vi
> L47: Rainman is **host-agnostic** — it works with any AI coding tool, not just Claude
> L48: Code. Its MCP server speaks standard MCP (so any MCP client can use the

## 星数曲线

```mermaid
xychart-beta
    title "yan-yanko/rainman 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `58c3210ec568` · [字段定义](../../DATASET.md)*
