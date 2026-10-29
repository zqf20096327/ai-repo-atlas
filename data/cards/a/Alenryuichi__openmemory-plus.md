# Alenryuichi/openmemory-plus

⭐ 20 · TypeScript · MIT · 推送 2026-03-01 · [GitHub](https://github.com/Alenryuichi/openmemory-plus) · 个人维护 · 中文 README

**让多个 AI Agent 共享统一记忆的 MCP 管理框架**

为 AI Agent 设计的统一记忆管理框架，作为 mem0/openmemory MCP 的增强层：采用 xMemory 四层记忆架构（L3 主题聚类 / L2 语义 / L1 情节 / L0 原始消息），基于 BGE-M3 向量检索与 Qdrant 存储，对话结束自动触发记忆提取，按项目级（_omp/memory/，Git 版本控制）与用户级双层分类存储。完整支持 Augment、Claude Code、Cursor、Gemini CLI 四种 IDE，需先安装 mem0/openmemory MCP。通过 npx 安装，Docker Compose 模式下 Docker 为唯一必需系统依赖；记忆分类可选用 DeepSeek、Ollama 等 6 种 LLM Provider。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- xMemory 四层记忆架构与 Top-down 自适应检索
- 对话结束自动触发记忆提取，双层存储（项目级+用户级）
- Augment/Claude Code/Cursor/Gemini CLI 四种 IDE 配置自动生成
- 敏感信息过滤（API Key/密码/私钥/个人信息自动阻止存储）
- ROT 记忆清理与 Ebbinghaus 遗忘曲线衰减

## 适用场景

- 同时使用 Cursor、Claude、Augment 等工具时共享同一份记忆
- 让 Agent 记住项目部署配置与技术决策，避免重复说明
- 跨项目同步个人技术偏好与技能
- 团队项目配置版本化，新成员 Agent 自动获取上下文

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L34: **OpenMemory Plus** 是一个为 AI Agent 设计的统一记忆管理框架，采用 **xMemory 四层记忆架构**：
> L405: |协议|MCP (Model Context Protocol)|Agent 通信协议|
> L471: **A:** OpenMemory Plus 是 mem0 的**增强层**，不是替代品。

## 星数曲线

```mermaid
xychart-beta
    title "Alenryuichi/openmemory-plus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `715ed511ca59` · [字段定义](../../DATASET.md)*
