# K-Dense-AI/agentic-data-scientist

⭐ 835 · Python · MIT · 推送 2026-08-18 · [GitHub](https://github.com/K-Dense-AI/agentic-data-scientist) · [官网](https://k-dense.ai) · 组织维护

**面向数据科学家的端到端多智能体分析框架**

基于 Google ADK 与 Claude Agent SDK 的开源多智能体数据科学框架：将规划与执行分离，由 Plan Maker、Coding Agent（Claude Code SDK，加载 143 个科学技能）、Review、Criteria Checker 等八类角色组成工作流，支持迭代规划、持续验证与执行中重规划，最终合成报告。提供 orchestrated 与 simple 两种模式，经 uv/uvx 安装，需配置 Anthropic 与 OpenRouter API key，编排模式涉及较多 API 调用成本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 八类专职 agent 角色的规划-执行-验证工作流
- Coding Agent 经 Claude Code SDK 加载 143 个科学技能（UniProt、RDKit、scanpy 等）
- MCP 集成（Context7 实时库文档）与工作目录沙箱化的内置工具
- orchestrated（完整多智能体）与 simple（直接编码）两种模式

## 适用场景

- 用自然语言发起差异表达分析等完整数据分析流水线
- 让 agent 生成数据脚本、预测模型与可视化报告
- 快速编写合并 CSV、绘制散点图等一次性代码任务

## 场景标签

`多智能体` `数据分析` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L16: **An Adaptive Multi-Agent Framework for Data Science**
> L18: Agentic Data Scientist is an open-source framework that uses a sophisticated multi-agent workflow to tackle complex
> L174: - **Plan Maker**: "What needs to be done?" - Creates comprehensive analysis plans with clear stages and success cr

## 星数曲线

```mermaid
xychart-beta
    title "K-Dense-AI/agentic-data-scientist 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24", "2026-10-25"]
    y-axis "stars" 829 --> 836
    line [830, 832, 835, 835]
```

2026-10-18 830 → 2026-10-25 835（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `8140c70b4fe7` · [字段定义](../../DATASET.md)*
