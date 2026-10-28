# microsoft/new-copilot-studio-tech-guide

⭐ 20 · Astro · MIT · 推送 2026-10-27 · [GitHub](https://github.com/microsoft/new-copilot-studio-tech-guide) · [官网](https://microsoft.github.io/new-copilot-studio-tech-guide/) · 组织维护

**Copilot Studio 代理与工作流示例的展示站与一键部署包**

微软官方仓库，包含 Astro 文档站（场景讲解与落地页）和可部署示例：四个代理（旗舰 Store Associate Assistant、自助退货与服务代理、两个连接代理）与四个内联 MCP 连接器，全部运行在 Power Platform 内、无需外部服务器。支持 curl/PowerShell 一行命令免克隆部署，也可克隆后用 node deploy/deploy.mjs 引导部署；需要 Node 18+、pac CLI 与 az CLI。另附历史迭代存档与两个演示场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 个代理 + 4 个内联 MCP 连接器的可部署示例，全跑在 Power Platform 内
- curl / PowerShell 一行命令免克隆部署
- 克隆后可用 node deploy/deploy.mjs 引导式部署
- Astro 文档站含场景讲解，部署到 GitHub Pages

## 适用场景

- 快速在 Power Platform 环境中搭建 Copilot Studio 代理演示
- 学习 Copilot Studio 代理与 MCP 连接器的实现方式
- 参考技术指南站了解 Agents 与 Workflows 体验

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: A showcase site and deployable sample for the Agents and Workflows experience in Microsoft Copilot Studio.
> L17: Four agents (flagship Store Associate Assistant, self-serve Returns & Service Assistant,
> L18: and two connected agents) and four inline MCP connectors (Membership, Order Management,

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/new-copilot-studio-tech-guide 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `813b342aa96a` · [字段定义](../../DATASET.md)*
