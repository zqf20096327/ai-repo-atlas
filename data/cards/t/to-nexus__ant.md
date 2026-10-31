# to-nexus/ant

⭐ 16 · TypeScript · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/to-nexus/ant) · 个人维护

**自托管 AI 工程平台：声明式上下文驱动 PRD→设计→代码→验证**

自托管的 agent 平台，把软件开发组织为状态机式的流水线：PRD 经 planner 澄清后生成系统设计与 UI 设计，代码任务基于设计产出，且每个代码任务内嵌并行任务与最终验证门，失败会生成修复任务再验证。核心机制是『上下文声明而非搜索』：任务只接收预先解析的产物集合，聊天记录与 LLM 上下文分离，任务只获取 4–12k token 的前序工作摘要，每次任务结束输出按模型划分的 token/费用明细。另有实验性 Workspace 形态，用文件定义工作 agent 并按 cron 调度、经 MCP 接入系统。需 Node.js 22+、pnpm、Docker（Redis）与自有 LLM key；自述 pre-alpha、单人开发，多项功能标注 Experimental。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 声明式上下文：任务执行前可见进入 prompt 的产物集合，禁止整仓遍历
- 每个代码任务自带验证门，失败门自动生成修复任务并重验证
- 两种项目形态（codespace/workspace）共享同一运行时、Redis 总线与加密凭证存储
- 按模型的 token/费用/缓存命中逐任务结算

## 适用场景

- 在自托管环境里从 PRD 出发生成设计文档与代码
- 以 spec 为单元迭代既有代码库并强制验证
- 用文件定义组织内工作 agent，按 cron 调度并经 MCP 连接系统

## 场景标签

`Agent 框架` `编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5:  The same runtime builds your product — PRD → design → code, every code job verifying itself — and runs your process
> L35: - **You see what enters the prompt, before the job runs.** Every job executes
> L97: 1. Write the **PRD**. The `planner` agent helps you clarify it.

## 星数曲线

```mermaid
xychart-beta
    title "to-nexus/ant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `43d69c6279b4` · [字段定义](../../DATASET.md)*
