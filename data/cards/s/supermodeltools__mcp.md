# supermodeltools/mcp

⭐ 17 · TypeScript · MIT · 推送 2026-05-12 · [GitHub](https://github.com/supermodeltools/mcp) · [官网](https://supermodeltools.com/trial) · 组织维护

**给 AI 编码代理提供代码图理解能力的 MCP 服务器**

基于 Model Context Protocol 的服务器，通过 Supermodel API 为 AI 代理提供代码库级理解：预计算调用图、依赖图，支持符号查询（定义、调用者/被调用者、领域归属）、BFS 调用图遍历与跨子系统分析，实现亚秒级响应以降低代理 token 消耗。给使用 Claude Code、Cursor 等 MCP 客户端的开发者使用。提供 npm/npx 安装与 setup.sh 脚本，支持 precache 预计算与缓存；首次无缓存分析需 API 调用（大仓库约 5-15 分钟），GraphRAG 模式标注为实验性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- symbol_context 工具：返回符号定义、调用者/被调用者、领域归属
- 实验性 GraphRAG 模式：explore_function 做调用图 BFS 遍历与跨子系统标记
- precache 预计算图缓存，运行时亚秒响应、无 API 调用
- 支持 Claude Code CLI 一条命令接入与 Cursor 配置

## 适用场景

- 让 AI 编码代理在大型代码库中快速定位符号与调用关系
- 通过预计算图缓存减少代理的 token 消耗
- 分析代码修改的影响范围与跨子系统依赖

## 场景标签

 · 领域:开发者工具/代码分析

## 证据(README 行号)

> L7: MCP server that gives AI agents instant codebase understanding via the Supermodel API. Pre-computed code graphs enab
> L128: ### `symbol_context` (Default Mode)

## 星数曲线

```mermaid
xychart-beta
    title "supermodeltools/mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `14f2f0fceb61` · [字段定义](../../DATASET.md)*
