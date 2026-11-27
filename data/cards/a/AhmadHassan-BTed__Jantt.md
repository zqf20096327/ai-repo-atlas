# AhmadHassan-BTed/Jantt

⭐ 6,239 · TypeScript · MIT · 推送 2026-11-26 · [GitHub](https://github.com/AhmadHassan-BTed/Jantt) · [官网](https://ahmadhassan-bted.github.io/Jantt/) · 个人维护

**无代码 AI 甘特图工具：自然语言生成与编辑项目计划**

一个甘特图/时间线应用，MIT 开源，浏览器端运行无需注册，也可通过 GitHub 登录创建多人云端协作房间。核心机制：内置 AI Copilot，用户用自然语言描述计划，输出经 JSON Schema 校验并以 diff 预览呈现后一键应用，支持撤销/重做；AI 调用采用 BYOK，密钥存于浏览器 localStorage，可接 10 家云端 provider 或本地 Ollama。项目管理侧提供工作日历 CPM、EVM、Monte Carlo 模拟、MS Project/P6 导入导出与 6 种同步视图。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言生成计划，AI 输出经 schema 校验并显示增/改/删 diff 预览
- BYOK 接入 10 个 provider，密钥仅存浏览器，或经 Ollama 离线运行
- 工作日历感知的关键路径计算、DCMA-14 审计、EVM 与 Monte Carlo 模拟
- 官方 MCP Server 提供 6 个调度工具，供 Claude Desktop/Cursor 等 agent 调用

## 适用场景

- 把会议记录粘贴给 Copilot，生成带负责人和依赖的任务甘特图
- 规划论文、申请或搬家等个人时间线并在清单视图逐日勾选
- 导入 MS Project/P6 文件在浏览器中查看和调整项目排期
- 为 AI agent 配置 MCP Server 实现程序化的计划读取与调整

## 场景标签

 · 领域:项目管理/可视化工具

## 证据(README 行号)

> L34: |**No Code Needed**|Drag bars visually, resize deadlines, connect arrows, or describe your plan in plain English to
> L87: - **No More Expensive Legacy Viewer Seats:** Import and export **Microsoft Project `.xml`** and **Oracle Primavera 
> L92: - **Official MCP Server (`@jantt/mcp`):** Connect Claude Desktop, Cursor, Gemini, or custom AI agents directly to 6

## 星数曲线

```mermaid
xychart-beta
    title "AhmadHassan-BTed/Jantt 星数(近 3 点)"
    x-axis ["2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 6238 --> 6241
    line [6240, 6239, 6239]
```

2026-11-25 6,240 → 2026-11-27 6,239（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `d1200566bdd7` · [字段定义](../../DATASET.md)*
