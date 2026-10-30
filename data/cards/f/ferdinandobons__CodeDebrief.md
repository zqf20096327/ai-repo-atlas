# ferdinandobons/CodeDebrief

⭐ 42 · Python · Apache-2.0 · 推送 2026-06-22 · [GitHub](https://github.com/ferdinandobons/CodeDebrief) · [官网](https://ferdinandobons.github.io/CodeDebrief/) · 个人维护

**为编码 agent 生成源码级工作流图的本地静态分析 MCP 工具**

对本地代码库做静态分析，映射入口、分支、调用、异常与结果，生成确定性的工作流图与可复用导航产物，通过 MCP 服务器（agent_context 返回带源码范围的 workflow_slice）供编码 agent 查询、展开与渲染 Mermaid 图。支持 codex、claude、gemini、cursor 四种 agent 客户端配置。分析器、产物、查看器与 MCP 服务器均为本地运行，不需要 LLM provider key。定位为工作流导航层，非文档生成器或缺陷查找器。当前为 pre-1.0 alpha，schema 与 MCP 载荷在 1.0 前可能变化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 静态分析生成确定性工作流流图与稳定图哈希
- MCP agent_context 返回带源码范围、调用关系与省略说明的 workflow_slice
- 本地优先，无需 LLM provider key
- setup 命令为 codex/claude/gemini/cursor 写入对应配置与技能文件

## 适用场景

- 让编码 agent 回答代码路径与状态处理问题时基于源码产物
- 调试或规划改动前查看受影响的工作流
- 手动浏览项目交互式工作流查看器

## 场景标签

 · 领域:开发者工具/代码分析

## 证据(README 行号)

> L16: CodeDebrief turns a local codebase into deterministic workflow flowcharts that coding
> L22: The analyzer, artifacts, viewer, and MCP server are local-first and do not require an LLM
> L198: Once `setup` has configured the project MCP server and agent instructions, supported

## 星数曲线

```mermaid
xychart-beta
    title "ferdinandobons/CodeDebrief 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-30 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c5a3d645d1f6` · [字段定义](../../DATASET.md)*
