# Azure-Samples/azure-ai-travel-agents

⭐ 481 · TypeScript · MIT · 推送 2026-10-24 · [GitHub](https://github.com/Azure-Samples/azure-ai-travel-agents) · [官网](https://azure-samples.github.io/azure-ai-travel-agents/) · 组织维护

**旅行社 AI 多智能体参考应用：MCP 工具编排与本地免费预览**

Azure-Samples 出品的模块化企业参考应用：用 LangChain.js、LlamaIndex.TS 和 Microsoft Agent Framework 三种编排方案协调多个 AI 智能体，辅助旅行社员工解析客户咨询、推荐目的地与规划行程；智能体工具以 Python/Node.js/Java/.NET 实现的 MCP 服务器提供。组件全部 Docker 容器化，可部署到 Azure Container Apps，也可经 Docker Model Runner 用 Phi4 14B 模型本地免费预览（需约 16GB 内存），或用 azd 一键部署到 Azure。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种编排方案可选（LangChain.js / LlamaIndex.TS / Microsoft Agent Framework）
- 多语言 MCP 服务器示例（Python、Node.js、Java、.NET）
- 通过 Docker Model Runner + Phi4 14B 本地免费预览
- OpenTelemetry + Aspire Dashboard 监控，azd 一键部署 Azure

## 适用场景

- 学习多智能体与 MCP 编排的参考实现
- 在本地免费预览并扩展自己的 AI agent 应用
- 快速部署一个多智能体示例到 Azure 并估算成本

## 场景标签

`多智能体` `教程课程` · 领域:Agent 开发

## 证据(README 行号)

> L28: The AI Travel Agents is a **modular reference application** that leverages multiple **AI agents** to enhance travel
> L57: - Deployed serverlessly via Azure Container Apps

## 星数曲线

```mermaid
xychart-beta
    title "Azure-Samples/azure-ai-travel-agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 480 --> 483
    line [482, 481]
```

2026-10-18 482 → 2026-10-24 481（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `dfa81a95890d` · [字段定义](../../DATASET.md)*
