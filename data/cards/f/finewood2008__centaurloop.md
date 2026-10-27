# finewood2008/centaurloop

⭐ 66 · TypeScript · MIT · 推送 2026-06-02 · [GitHub](https://github.com/finewood2008/centaurloop) · [官网](https://www.centaurloop.com/) · 个人维护 · 中文 README

**构建 AI 员工的最小工作单元（循环工作流）框架**

TypeScript/React 实现的开源框架与本地工作台 MVP，把岗位拆解为可治理、可组合的循环工作流：目标→上下文→AI 执行→人工关卡→反馈→记忆→下一周期。提供确定性 demo 运行时（无需 API key），并支持 OpenAI 兼容端点及 Ollama、vLLM、LM Studio、llama.cpp 本地运行时探测；内置内容增长、客服、产品迭代三个起步数字员工。README 自述为早期 MVP，尚非稳定库 API。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 循环状态机（loopEngine）在人工关卡处暂停
- 确定性 demo 运行时，无需 API key 即可运行
- 支持 OpenAI 兼容端点与 Ollama/vLLM/LM Studio/llama.cpp 本地运行时连接器
- 内置内容增长、客服、产品迭代三个起步数字员工

## 适用场景

- 把内容运营岗位拆成可由 AI 执行、人工审核的循环工作流
- 在本地工作台中试验 AI 员工的计划-执行-反馈-记忆闭环
- 探索对 AI 执行环节保留人工审批与治理的工作流结构

## 场景标签

`Agent 框架` `Agent 记忆` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L11: **Centaur Loop is an open-source framework for building AI employees from governable work loops.**
> L76: |**Loop Runtime**|The execution layer: model, agent, workflow, or external runtime.|
> L123: |`src/adapters/*`|Runtime, model, tool, feedback, and memory boundaries.|

## 星数曲线

```mermaid
xychart-beta
    title "finewood2008/centaurloop 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-27"]
    y-axis "stars" 65 --> 74
    line [73, 66, 66]
```

2026-10-18 73 → 2026-10-27 66（-7）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9749444c145e` · [字段定义](../../DATASET.md)*
