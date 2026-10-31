# Memel06/mnemonio

⭐ 19 · TypeScript · MIT · 推送 2026-04-03 · [GitHub](https://github.com/Memel06/mnemonio) · [官网](https://mnemonio.com) · 个人维护

**给 LLM agent 的持久化文件式记忆层（MCP/CLI/库）**

面向开发者工作流的持久化结构记忆层：以带 YAML frontmatter 的 markdown 文件存储记忆，通过 MANIFEST.md 作为入口并自动截断以控制 token。提供 MCP 服务器、CLI 与 TypeScript 库三种形态，含语义搜索、会话事实自动抽取与定期合并精简。LLM 操作由用户传入回调实现，自动识别 OpenAI/Anthropic/OpenRouter 及任意 OpenAI 兼容端点。支持提交到仓库的共享只读团队记忆目录，并有路径遍历防护。基础方法无需 LLM。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- markdown+YAML frontmatter 文件式记忆与 MANIFEST.md 入口（自动截断控制 token）
- MCP 服务器 / CLI / TypeScript 库三种交付形态
- LLM 通过回调注入，自动识别 OpenAI/Anthropic/OpenRouter 及 OpenAI 兼容端点
- 共享只读团队记忆目录，含路径遍历安全校验

## 适用场景

- 让 AI 编码助手跨会话保留项目记忆
- 团队共享编码规范与上下文的基线记忆
- 从对话中自动抽取持久事实并定期合并精简

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: Persistent structured memory layer for LLM agents. Mnemonio gives your agent a
> L10: It ships as an MCP server, a CLI, and a TypeScript library. LLM operations use

## 星数曲线

```mermaid
xychart-beta
    title "Memel06/mnemonio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `0e944e723df3` · [字段定义](../../DATASET.md)*
