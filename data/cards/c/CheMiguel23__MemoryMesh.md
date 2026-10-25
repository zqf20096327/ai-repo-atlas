# CheMiguel23/MemoryMesh

⭐ 354 · TypeScript · MIT · 推送 2026-03-01 · [GitHub](https://github.com/CheMiguel23/MemoryMesh) · 个人维护

**为 AI 模型提供结构化记忆的 MCP 知识图谱服务器**

基于 Model Context Protocol 的本地知识图谱服务器，源自 MCP servers 仓库的 Knowledge Graph Memory Server，面向文本 RPG 与交互叙事等场景，帮助 AI 在多轮对话间维持一致的结构化记忆。核心机制：用户以 JSON schema 定义数据结构，系统据此自动生成 add/update/delete 工具；节点带类型、元数据与权重，边表达关系，数据默认存于 dist/data/memory.json。内置 11 个 RPG 预置 schema、SchemaManager 可视化编辑器与独立的 Memory Viewer 网页查看器。以 TypeScript 编写，需 Node.js 18+，git clone 后 npm install 并 npm run build，通过 Claude Desktop 的 mcpServers 配置接入。

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

- schema 驱动自动生成 add/update/delete 动态工具
- 节点/边结构化存储，元数据引导 AI 建图
- 内置 11 个文本 RPG 预置 schema
- SchemaManager 可视化编辑与 Memory Viewer 图谱查看器

## 适用场景

- 文本 RPG 中让 AI 记住角色、地点与物品关系
- 为 Claude Desktop 等 MCP 客户端添加持久结构化记忆
- 自定义 schema 管理社交网络模拟或组织规划类结构化数据

## 场景标签

`知识图谱` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7: MemoryMesh is a knowledge graph server designed for AI models, with a focus on text-based RPGs and interactive story
> L11: MemoryMesh MCP server
> L17: **v0.3.0 Update:** The MCP SDK has been updated from v1.0.4 to v1.25.2 to comply with the current Model Context Pro

## 星数曲线

```mermaid
xychart-beta
    title "CheMiguel23/MemoryMesh 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 353 --> 355
    line [354, 354]
```

2026-10-18 354 → 2026-10-25 354（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `1372baa6ec37` · [字段定义](../../DATASET.md)*
