# HorizunGroup/naviscoord-mcp

⭐ 20 · C# · MIT · 推送 2026-10-24 · [GitHub](https://github.com/HorizunGroup/naviscoord-mcp) · [官网](https://horizunhub.com/ia/) · 组织维护

**连接 Navisworks 与 AI 客户端的 MCP 服务器：BIM 碰撞分析与协调计划**

由原生 Navisworks 插件与开源 MCP 服务器组成的 BIM 协调工具：通过 ChatGPT Desktop Work、Claude Desktop、Claude Code、Codex 四种客户端以自然语言查询碰撞问题，返回排序议题、空间分组、根因假设、变更对比、工作包与 PDF 报告，并可执行带验证的写回操作。引擎运行在本地 Windows 工作站，打包版本无需安装 Python、API key 或构建工具。需要 Windows 与 Autodesk Navisworks Manage 2024-2026 许可证；独立分析引擎也可处理已保存的导出文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 53 个工具，支持 4 种 AI 客户端接入
- 确定性评分的议题排序与根因假设分析
- 打包本地服务器：无需 Python 安装、API key 或构建工具
- 带文档/版本检查与读回验证的定向写回

## 适用场景

- BIM 协调会议前用对话获取优先议题与工作计划
- 对比两次交付之间的碰撞变化
- 生成带证据与责任划分的协调报告

## 场景标签

 · 领域:建筑/工程/施工（AEC）BIM 协调

## 证据(README 行号)

> L5: **Connect Autodesk Navisworks to ChatGPT Desktop Work, Claude Desktop, Claude Code and Codex. Ask what matters, insp
> L22: NavisCoord pairs a native Navisworks add-in with an open-source MCP server. The engine runs on your Windows worksta
> L36: **53 tools. One server. Four clients.** Explore the tool guide.

## 星数曲线

```mermaid
xychart-beta
    title "HorizunGroup/naviscoord-mcp 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25", "2026-10-29"]
    y-axis "stars" 17 --> 21
    line [18, 19, 20, 20]
```

2026-10-18 18 → 2026-10-29 20（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `64d436199e43` · [字段定义](../../DATASET.md)*
