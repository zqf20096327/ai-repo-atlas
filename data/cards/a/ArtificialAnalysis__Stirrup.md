# ArtificialAnalysis/Stirrup

⭐ 666 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/ArtificialAnalysis/Stirrup) · [官网](https://stirrup.artificialanalysis.ai) · 组织维护

**给开发者的轻量级 Python agent 构建框架**

ArtificialAnalysis 维护的轻量级 Python 框架，可作为包或起始模板构建自定义 agent。核心机制：Agent 运行循环、Pydantic 参数定义的 Tool 接口、session() 上下文管理工具生命周期。内置能力包括本地/Docker/E2B 沙箱代码执行、网页搜索抓取（需 BRAVE_API_KEY）、MCP 客户端、文档输入输出、技能系统、人工反馈工具、上下文自动摘要与多模态处理。模型接入通过 OpenAI 兼容 API、LiteLLM 或自建客户端。另有 TypeScript 实现 StirrupJS。

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

- 代码执行支持本地、Docker 与 E2B 沙箱三种模式
- MCP 客户端支持连接 MCP 服务器的工具与资源
- 上下文接近上限时自动摘要对话历史
- 通用 Tool 接口（Pydantic 参数）与 ToolProvider 生命周期管理

## 适用场景

- 以包或模板为起点构建自定义 AI agent
- 接入 OpenAI 兼容端点或经 LiteLLM 使用多供应商模型
- 为 agent 挂载代码执行、网页搜索与 MCP 工具

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7:  The lightweight foundation for building agents
> L11: Stirrup is a lightweight framework, or starting point template, for building agents. It differs from other agent fr

## 星数曲线

```mermaid
xychart-beta
    title "ArtificialAnalysis/Stirrup 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 659 --> 665
    line [660, 662, 664]
```

2026-10-18 660 → 2026-10-22 664（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `8a2ccf70139f` · [字段定义](../../DATASET.md)*
