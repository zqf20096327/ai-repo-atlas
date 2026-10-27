# Azure-Samples/azure-ai-agents-javascript

⭐ 27 · TypeScript · MIT · 推送 2026-03-03 · [GitHub](https://github.com/Azure-Samples/azure-ai-agents-javascript) · 组织维护

**用 Azure AI Agent Service 构建 JS agent 的演示项目**

基于 Azure AI Agent Service QuickStart 代码扩展的 JavaScript 演示：展示无工具计算、Function Calling、代码解释器（含 CSV 分析与图表生成）、基于 AI Search 的 RAG、Bing Grounding 实时网页数据以及 token 用量统计等 agent 工具能力。面向使用 Azure AI Foundry 的开发者，需先创建 AI Foundry 项目并配置端点、AI Search 连接与 Bing 连接等环境变量，再通过 npm install 与 npm start 运行并选择要执行的 agent 演示。

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

- 演示 Function Calling 与代码解释器（CSV 检查、分析、图表生成）
- 通过 AI Search 实现 RAG 功能
- Bing Grounding 接入实时公开网页数据
- 返回输入/输出 token 用量统计

## 适用场景

- 学习 Azure AI Agent Service 的各类工具接入方式
- 参考代码解释器做 CSV 分析与图表生成的实现
- 搭建基于 AI Search 的 RAG agent 原型

## 场景标签

`RAG` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L1: # Azure AI Agent Service Demo
> L3: This demo originally started out using the code from the Azure AI Agent QuickStart, but has expanded to show differe
> L18: To use the demo you'll need to create an Azure AI Foundry project by following the QuickStart.

## 星数曲线

```mermaid
xychart-beta
    title "Azure-Samples/azure-ai-agents-javascript 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-27 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `ffdfde702c74` · [字段定义](../../DATASET.md)*
