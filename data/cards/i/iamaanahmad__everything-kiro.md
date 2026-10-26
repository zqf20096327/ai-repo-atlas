# iamaanahmad/everything-kiro

⭐ 31 · 推送 2026-09-04 · [GitHub](https://github.com/iamaanahmad/everything-kiro) · 个人维护

**Kiro IDE 配置集合：agents、skills、hooks、MCP 集成**

面向 Kiro IDE 用户的配置文件合集：提供 8 个自定义 agent（含 tools 权限范围）、steering 文件、10 类触发器的 hooks、基于 YAML 能力的权限规则、EARS 格式的 Spec 工作流文件，以及 Knowledge Base 与 Guided MCP 两类 Power 封装。所有配置随 Kiro IDE 1.0 实际 schema 维护，文档同时说明 AGENTS.md、Agent Focus Mode、Cloud Sessions 等机制。安装方式为 git clone 后复制 .kiro 目录到工作区，需自行填入 MCP 凭据。不包含 Kiro Crew 的 manifest 与编排工作流。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 个自定义 agent，各带 tools 权限范围
- 10 类触发器的 hooks，含可阻断操作的动作（exit code 2）
- YAML 能力权限系统（fs_read/shell/mcp 等，deny>ask>allow）
- EARS 格式三阶段 Spec 工作流（requirements/design/tasks）

## 适用场景

- 把整套 .kiro 配置一键放入工作区获得预设 agent 与 hooks
- 参考 Kiro 当前 schema 编写自己的 steering 文件与权限规则
- 学习 Power 封装与 MCP 服务器接入方式

## 场景标签

`编码 Agent` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L1: # Everything Kiro
> L3: **A collection of Kiro IDE configurations — agents, hooks, steering files, powers, and skills — kept in sync with Ki

## 星数曲线

```mermaid
xychart-beta
    title "iamaanahmad/everything-kiro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-26 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `3f07f920555c` · [字段定义](../../DATASET.md)*
