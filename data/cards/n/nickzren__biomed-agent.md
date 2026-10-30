# nickzren/biomed-agent

⭐ 16 · Python · Apache-2.0 · 推送 2026-10-06 · [GitHub](https://github.com/nickzren/biomed-agent) · 个人维护

**MCP 生物医学数据研究工作区：连接 agent 与生物医学数据库**

面向 Claude Code、Codex 等编码 agent 的 MCP 后端生物医学研究工作区。提供 MCP 服务器注册表、本地路径处理、服务器/工具诊断 CLI（list-servers/list-tools）、跨服务器研究契约与 mcp.json 注册示例，覆盖 OpenTargets、Monarch、MyGene、MyChem、MyDisease 五个数据源，默认要求同级目录存放各 MCP 仓库或用环境变量覆盖路径。以 uv 管理的 Python 项目提供，附 agent skill 安装脚本与 print-only 配置生成；声明仅供科研教育用途，非临床决策系统。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 服务器注册表与本地路径处理
- 诊断 CLI（list-servers / list-tools / doctor）
- 跨服务器 source-backed 研究契约
- 支持 OpenTargets/Monarch/MyGene/MyChem/MyDisease 五个生物医学数据源

## 适用场景

- 为 Claude Code / Codex 等 agent 接入生物医学数据库
- 诊断与检查 MCP 服务器及工具状态
- 按研究契约做靶点、基因、疾病、化合物的跨库检索

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: `biomed-agent` is an MCP-backed biomedical research workspace for Claude Code, Codex, and other coding agents. It pr
> L9: - MCP server registry and local path handling.

## 星数曲线

```mermaid
xychart-beta
    title "nickzren/biomed-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `e154921779e7` · [字段定义](../../DATASET.md)*
