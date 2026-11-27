# mannysz/neuron-engine

⭐ 10 · JavaScript · MIT · 推送 2026-11-26 · [GitHub](https://github.com/mannysz/neuron-engine) · 个人维护

**为 AI 编码代理提供本地持久记忆的 CLI 工具**

neuron-engine 是面向 AI 编码代理的本地优先持久记忆 CLI，将项目记忆以 Markdown 和 JSON 存储于 .memory/ 目录，无需云服务或数据库。记忆分三层：Active Focus 跟踪当前主题、Topic Graph 以节点存储工作流、Daily Logs 追加式日志与搜索。通过 npx skills 或各 harness 插件方式安装，跨 Claude Code、Codex、Cursor 等工具共享同一份项目记忆；可选 qmd 集成提供向量+关键词混合搜索，未安装时回退到本地文本搜索。

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

- 三层记忆结构：Active Focus、Topic Graph、Daily Logs
- 本地运行无云服务，读取延迟低于 15ms
- 同一份记忆跨多个 AI 编码工具共享
- 可选 qmd 集成提供混合向量+关键词搜索

## 适用场景

- AI 编码会话压缩或新会话启动后恢复项目上下文
- 多工具（Claude Code/Codex/Cursor）共享同一项目记忆
- 按主题组织调试历史与架构决策记录

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: A local-first persistent memory CLI for AI coding agents. Use whichever harness and model you want (**Claude Code**,
> L7: AI coding agents lose track of architecture decisions, debugging history, and project conventions whenever a chat co


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `ea688affa736` · [字段定义](../../DATASET.md)*
