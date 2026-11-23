# tuoxie2046/GenAI-DrawIO-Creator

⭐ 10 · TypeScript · Apache-2.0 · 推送 2026-04-06 · [GitHub](https://github.com/tuoxie2046/GenAI-DrawIO-Creator) · [官网](https://genai-drawio-creator.vercel.app) · 个人维护

**面向开发者的自然语言对话式 draw.io 图表生成工具**

基于 Next.js 的 Web 应用，通过自然语言命令创建、修改 draw.io 图表。采用 plan–tool–reflect 的 agent 循环，提供四个结构化工具（生成/编辑/读取/查形状库），内置结构校验（11 项检查+24 步自动修复）、可选 VLM 视觉校验与语义验证。支持 34+ 形状库（AWS/GCP/Azure/Kubernetes 等）、图片与 PDF 上传生成图表、按 cell ID 的非破坏性编辑。提供在线演示、桌面应用、Docker、源码与 Vercel 部署方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- plan–tool–reflect agent 循环与四个结构化图表工具
- 34+ 形状库：AWS、GCP、Azure、Kubernetes、BPMN、UML、Cisco 等
- 非破坏性迭代：按 cell ID 编辑，保留用户已有调整
- MCP Server 可接入 Claude Desktop、Cursor、VS Code

## 适用场景

- 用自然语言生成云架构图（AWS/GCP/Azure）
- 上传现有架构图或 PDF 文档让 AI 复刻生成图表
- 通过 Claude Code 等客户端调用 MCP 服务创建流程图

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L14: A Next.js web application that integrates AI capabilities with draw.io diagrams. Create, modify, and enhance diagra
> L45: - **LLM-Powered Diagram Creation**: Leverage Large Language Models to create and manipulate draw.io diagrams direct
> L175: The application runs a **plan–tool–reflect** agentic loop:

## 星数曲线

```mermaid
xychart-beta
    title "tuoxie2046/GenAI-DrawIO-Creator 星数(近 2 点)"
    x-axis ["2026-10-21", "2026-11-23"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-21 10 → 2026-11-23 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `54edc7b792ed` · [字段定义](../../DATASET.md)*
