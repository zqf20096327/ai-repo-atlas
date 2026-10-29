# MarcSkovMadsen/holoviz-mcp

⭐ 34 · Python · BSD-3-Clause · 推送 2026-10-01 · [GitHub](https://github.com/MarcSkovMadsen/holoviz-mcp) · [官网](https://marcskovmadsen.github.io/holoviz-mcp/) · 个人维护

**为 AI 助手提供 HoloViz 生态文档与组件检索的 MCP 服务器**

面向 MCP 兼容 AI 助手的 Model Context Protocol 服务器：提供 HoloViz 生态（Panel、hvPlot、Lumen、Datashader 等）的文档检索、100+ Panel 组件的参数与用法信息、Panel 扩展检测，以及一个在隔离服务器中执行 Python 代码并生成可分享 URL 的 Display Server。另含 8 个可独立安装的 Agent Skills（panel、hvplot 等），支持 agr、Vercel skills、openskills 等技能管理器安装。注意：默认启用任意 Python 代码执行（可配置）。以 Python 包、Docker 镜像与 conda-forge 形式分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HoloViz 文档与 100+ Panel 组件参数信息的检索工具
- 隔离服务器执行 Python 可视化代码并生成可分享 URL
- 8 个符合 Agent Skills 规范、可脱离 MCP 服务器独立安装的技能
- 支持任何 MCP 兼容 AI 助手，提供 Docker 镜像

## 适用场景

- 让 AI 编程助手在写 Panel/hvPlot 代码时查询组件参数与文档
- 让 AI 助手生成并即时预览交互式数据可视化
- 为 Claude 等 agent 框架单独安装 HoloViz 技能包

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L10: A comprehensive Model Context Protocol (MCP) server that provides intelligent access to the HoloViz ecosystem, enab
> L40: The HoloViz MCP skills follow the Agent Skills specification and can be installed standalone — without running the 

## 星数曲线

```mermaid
xychart-beta
    title "MarcSkovMadsen/holoviz-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-29 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `7d1eae5c577c` · [字段定义](../../DATASET.md)*
