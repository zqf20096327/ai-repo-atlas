# vivek100/oneShotCodeGen

⭐ 252 · TypeScript · 推送 2026-01-05 · [GitHub](https://github.com/vivek100/oneShotCodeGen) · 个人维护

**通过对话生成企业应用配置的 agent 系统（FastAPI+React）**

模块化 agent 流系统：用户在聊天界面描述需求，主 agent 决策后执行创建/编辑应用的流程，AI 步骤（调用 OpenAI API）生成用例、实体模型、界面规格与数据模型，工具调用步骤负责实体重组、合并与校验；用 JSON Schema 与 Pydantic 模型做结构化生成，SQLite 存储，WebSocket 实时更新。面向需要快速生成企业/ERP 应用配置的开发者。需自行配置 OpenAI API 环境变量，前后端分别以 Python 和 Node.js 从源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 主 agent 路由 + 创建/编辑应用的多流程编排
- JSON Schema 与 Pydantic 双重结构化生成校验
- 步骤级 Replay 引擎用于调试单个 AI 步骤
- WebSocket 实时聊天与流程状态更新

## 适用场景

- 用自然语言描述需求，生成完整应用配置
- 对已生成的应用配置做局部修改与合并
- 调试和重放 agent 流程中的单个 AI 步骤

## 场景标签

 · 领域:应用生成/agent 工具

## 证据(README 行号)

> L3: A modular agent-based system for generating and editing app configurations through AI-driven steps organized in flow
> L164: 4. **AI Steps**: These steps use large language models (via OpenAI's API) to:
> L176: 6. **Structured Generation**: The system uses both JSON schema validation and Pydantic models to ensure consistent

## 星数曲线

```mermaid
xychart-beta
    title "vivek100/oneShotCodeGen 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 251 --> 253
    line [252, 252]
```

2026-10-18 252 → 2026-10-24 252（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `23d9fdcfd52e` · [字段定义](../../DATASET.md)*
