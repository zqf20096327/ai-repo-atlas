# raytone-lab/agentcanvas

⭐ 19 · TypeScript · MIT · 推送 2026-10-16 · [GitHub](https://github.com/raytone-lab/agentcanvas) · 组织维护 · 中文 README

**可视化配置并导出 Agent 前端 React 工程的生成器**

面向开发者/设计者的 Agent 前端设计时工具：在可视化编辑器中组合对话流、推理披露、工具调用卡片、审批、artifacts、输出与 Git 面板等界面元素，可用内置离线事件流回放预览，也可接内置 Pi 运行时真实运行；一键导出为独立 React 项目（zip，npm install 后即可运行，无 AgentCanvas 运行时依赖）。本体是 Vite/TypeScript 应用，要求 Node.js 22.19+，另提供 docs/ 下的版本化嵌入包与技术文档（含中文指南）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可视化编辑器组合 Agent 界面并实时预览（离线事件流回放或 Pi 运行时）
- 一键导出独立 React 项目，导出物无 AgentCanvas 运行时依赖
- Schema 驱动：预设解析为 AgentFrontendProject 对象，组件独立可导出
- 提供版本化嵌入包（packages/）与导出契约、嵌入边界等文档

## 适用场景

- 不想手写代码地从零搭一个 Agent 聊天前端
- 设计并预览 Agent 的事件呈现方式（推理、工具调用、审批等）
- 导出可自持维护的 React 前端工程用于生产

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L8: A visual UX configurator and scaffold generator for Agent frontends.
> L36: - **Export is a real project.** One click produces a zip that runs with
> L37:  `npm install && npm run dev`. No AgentCanvas runtime dependency, no builder

## 星数曲线

```mermaid
xychart-beta
    title "raytone-lab/agentcanvas 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-30 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `6b3dc30f68da` · [字段定义](../../DATASET.md)*
