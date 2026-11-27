# alexei-led/pi-model-router

⭐ 11 · TypeScript · MIT · 推送 2026-11-19 · [GitHub](https://github.com/alexei-led/pi-model-router) · 个人维护

**Pi 编码 agent 的四档模型路由扩展**

以扩展形式运行于 Pi 编码 agent 的模型路由工具：随任务变化在不同模型与推理档位间自动选择，覆盖 tool-loop 之间的切换。提供 cost/balanced/quality 三种路由模式、按 profile/project/session 的配置层级、fallback 顺序与手动 pin；可选接入注册在 Pi 的文本分类器（Jev、Clef、OpenAI Decisions、本地 Ollama/llama.cpp）作为建议方，需按 profile 显式批准。提供 /router 检查面板查看当前路由与用量。生成回答的是被选中的模型，而非建议方。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四档路由模式（cost/balanced/quality），按 profile、项目或会话配置
- 可选分类器建议方，支持本地 Ollama/llama.cpp 分类器
- /router 面板查看活动、模型、档位与用量，历史记录可选开启
- 确定性基线路由与 fallback 顺序、手动 pin 控制

## 适用场景

- 在 Pi 编码 agent 中用单一 profile 组合低成本与高档模型
- 控制 token 开销的同时在关键任务上使用更强模型
- 排查当前会话实际使用的路由与模型档位

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L10: `pi-model-router` can select a different model and reasoning effort as the task changes, including between tool-loo
> L28: Use Jev, Clef/Clef Flash/Clef Omni, OpenAI Decisions, or a local Ollama or llama.cpp classifier registered in Pi.
> L126: pi install npm:@alexeiled/pi-model-router

## 星数曲线

```mermaid
xychart-beta
    title "alexei-led/pi-model-router 星数(近 3 点)"
    x-axis ["2026-10-28", "2026-11-12", "2026-11-27"]
    y-axis "stars" 9 --> 12
    line [10, 11, 11]
```

2026-10-28 10 → 2026-11-27 11（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `968faf6c94ae` · [字段定义](../../DATASET.md)*
