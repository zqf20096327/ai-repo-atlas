# arthi-arumugam-git/whatbroke

⭐ 21 · TypeScript · MIT · 推送 2026-09-28 · [GitHub](https://github.com/arthi-arumugam-git/whatbroke) · [官网](https://www.npmjs.com/package/whatbroke-cli) · 个人维护 · 中文 README

**对比 AI agent 两次运行的工具调用与输出差异的 CLI**

面向开发者的 agent 行为 diff 工具：读取 JSONL 格式的运行 trace（LLM 调用、工具调用、参数、成本、延迟、输出），对比两次运行，按 breaking/changed/info 分级报告工具调用消失、参数漂移、成本与延迟变化等；退出码可接入 CI 门禁。trace 可通过本地代理、Node/Python SDK 或导入 OpenTelemetry/Langfuse/LangSmith 生成，另支持行为契约检查、watch 模式与 GitHub Action。确定性离线运行，无需 API key。

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

- 按 id 对齐运行与工具调用，输出 breaking/changed/info 分级差异报告
- 多次采样对比并区分噪声（flaky 降级）
- 支持 OpenTelemetry/Langfuse/LangSmith 既有 trace 导入
- 行为契约（contract）检查与 CI 失败门禁

## 适用场景

- 换模型或改提示词后检查 agent 工具调用行为是否变化
- 在 CI 中对 agent trace 做行为回归门禁
- 为既有 Langfuse/LangSmith trace 生成行为差异报告

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: **Diff your AI agent's behavior between two runs.**
> L50: 4. `whatbroke diff old.jsonl new.jsonl`
> L242: Use both. Evals score each version against a rubric. whatbroke answers a different question: what exactly changed 

## 星数曲线

```mermaid
xychart-beta
    title "arthi-arumugam-git/whatbroke 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `3ff0d6708b7d` · [字段定义](../../DATASET.md)*
