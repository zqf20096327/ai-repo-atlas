# codyadam/system-prompt

⭐ 31 · TypeScript · MIT · 推送 2025-12-20 · [GitHub](https://github.com/codyadam/system-prompt) · [官网](https://systemprompt.app) · 个人维护

**浏览器内运行的可视化 AI 工作流构建器，节点式串联 AI 任务**

开源的节点式 AI 工作流构建器（Next.js/React，基于 React Flow）：在无限画布上用拖拽方式创建 Prompt 节点、AI 节点、Markdown 输出节点与注释节点，把节点连接成链式工作流；每个节点带 Run 按钮，AI 节点根据所选模型与系统提示生成 LLM 回复并传给下游节点。用户自带 API key，可搭配任意模型；应用完全在浏览器运行，无需安装，工作流保存在本地存储。面向希望将重复性 AI 任务（如邮件回复、内容创作、数据处理）模板化的个人用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无限画布的节点式工作流构建，拖拽创建与连接节点
- AI 节点使用用户自带 API key，可搭配任意模型
- 完全在浏览器运行，工作流保存于本地存储
- 支持可复用的 AI 模板与多步 AI 操作链式编排

## 适用场景

- 把反复输入的提示词做成可复用的 AI 工作流
- 一次设计模板，为不同平台生成保持品牌语气的内容
- 构建数据清洗、分析、汇报的多步处理链

## 场景标签

`工作流自动化` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L30:  Create reusable AI tasks with drag-and-drop nodes. Fully local, free, and open-source. Use any AI model with your 
> L103: - **AI Nodes**: Take any inputs like prompt nodes and generate an LLM response based those inputs, the AI model yo

## 星数曲线

```mermaid
xychart-beta
    title "codyadam/system-prompt 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 29 --> 32
    line [30, 31, 31]
```

2026-10-18 30 → 2026-10-29 31（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `47a0d664c704` · [字段定义](../../DATASET.md)*
