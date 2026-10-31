# apache/seatunnel-tools

⭐ 44 · Java · 推送 2026-02-27 · [GitHub](https://github.com/apache/seatunnel-tools) · [官网](https://seatunnel.apache.org/) · 组织维护 · 中文 README

**Apache SeaTunnel 辅助工具集：AI 技能、MCP 服务与配置转换**

Apache 基金会维护的 SeaTunnel 辅助工具仓库，含三个工具：面向 Claude Code 的 SeaTunnel Skill（查询文档、生成配置示例、错误分析助手）、面向 LLM 系统的 SeaTunnel MCP Server、以及将 DataX 等配置转换为 SeaTunnel 格式的 x2seatunnel。README 同时大量覆盖 SeaTunnel 核心引擎的安装（二进制/源码/Docker）、连接器清单、批流/CDC 作业配置示例与故障排查。Skill 通过复制到 ~/.claude/skills/ 安装，MCP Server 提供英文/中文文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Claude Code 集成的 SeaTunnel Skill：文档查询、配置生成、错误分析
- 面向 LLM 系统的 SeaTunnel MCP Server（Model Context Protocol）
- x2seatunnel：DataX 等配置到 SeaTunnel 格式的转换器
- README 覆盖 SeaTunnel 核心安装、100+ 连接器与批流/CDC 配置示例

## 适用场景

- 在 Claude Code 中查询 SeaTunnel 文档并生成作业配置
- 通过 MCP 让 LLM 系统接入 SeaTunnel 操作
- 把存量 DataX 配置迁移为 SeaTunnel 格式

## 场景标签

 · 领域:数据集成/AI 工具生态

## 证据(README 行号)

> L5: Auxiliary tools for Apache SeaTunnel focusing on developer/operator productivity around configuration, conversion, L
> L11: |**SeaTunnel Skill**|Claude AI integration for SeaTunnel operations|✅ New|
> L12: |**SeaTunnel MCP Server**|Model Context Protocol for LLM integration|✅ Available|

## 星数曲线

```mermaid
xychart-beta
    title "apache/seatunnel-tools 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 42 --> 45
    line [43, 44, 44]
```

2026-10-18 43 → 2026-10-31 44（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `c99bfbaeac65` · [字段定义](../../DATASET.md)*
