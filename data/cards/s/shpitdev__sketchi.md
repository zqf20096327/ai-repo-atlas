# shpitdev/sketchi

⭐ 13 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/shpitdev/sketchi) · [官网](https://sketchi.app) · 组织维护

**面向人与 AI agent 的提示词生成可编辑图表工具**

Sketchi 将自然语言提示转换为经验证的类型化中间表示，再经确定性布局转换为可编辑的 Excalidraw 场景与托管 PNG，支持流程图、思维导图、时序图、甘特图等 16 类图表。模型输出不被视为最终图：需经解析、校验、代码化布局后生成工件。提供 npm CLI（含离线确定性创作、加密快照分享）、公开 Code Mode MCP 端点（供 Codex/Claude Code/Agy/OpenCode 调用，无需登录或 API key）及 Playground、图标浏览器等网页面。仓库为 Nx + Cloudflare Workers 单仓。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模型输出解析为类型化 IR 并校验，布局与场景转换在代码中确定性完成
- 支持 16 类原生图表类型，不支持类型明确报错而非回退模板
- CLI 的 create/patch/show 等命令完全离线且无需凭证；generate/share/pull 为无凭证网络命令
- 公开 Code Mode MCP 端点供 Codex/Claude Code/Agy/OpenCode 创建托管图表，无需登录

## 适用场景

- 用一句话生成可编辑的 Excalidraw 流程图或时序图
- 让编码 agent 通过 MCP 端点创建和修改托管图表
- 离线确定性创作、版本化与导出图表工件

## 场景标签

 · 领域:开发工具/图表生成

## 证据(README 行号)

> L5:  Typed, deterministic diagrams for people and AI agents.
> L26: - Creates hosted flowcharts, mindmaps, sequence diagrams, timelines, state machines, Gantt charts, ER diagrams, UML
> L108: Codex, Claude Code, Agy, and OpenCode can create hosted diagrams through the

## 星数曲线

```mermaid
xychart-beta
    title "shpitdev/sketchi 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `ed65202c9eb3` · [字段定义](../../DATASET.md)*
