# huggingface/is-it-agentic-enough

⭐ 25 · Python · Apache-2.0 · 推送 2026-08-27 · [GitHub](https://github.com/huggingface/is-it-agentic-enough) · 组织维护

**评测编码 agent 使用库库方式的工具：跨模型与版本运行任务**

agent-eval 度量编码 agent 使用某个库的方式：不只看答案对错，还记录是否用 CLI 还是手写 Python、token 与耗时、出错频率。同一任务在库的多个修订版本与多个开放模型间以 YAML 矩阵形式作为 Hugging Face Jobs 启动运行，结果渲染为可托管为 HF Space 的静态 HTML 报告。环境与任务套件由 profile 定义（transformers 为参考研究、mock 为无 agent 的快速体验）。transformers profile 会绕过权限执行任意修订版本的代码，README 声明仅限可信本地使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模型 × 修订版本 × 辅助层级（bare/clone/skill）矩阵评测
- 静态 HTML 报告含 Overview/Coverage/Results 三个标签页
- 以 Hugging Face Jobs 启动运行，崩溃不丢失已完成结果
- 五个子命令：batch/report/sync/upload/setup

## 适用场景

- 评估编码 agent 在不同库版本下的表现与开销
- 比较不同开放模型完成同一任务套件的路径与错误率
- 将评测结果发布为可共享的静态报告页

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: `agent-eval` measures how a coding agent uses a library. Not just whether it gets
> L8: tasks across library revisions and models, and renders the results as a static HTML

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/is-it-agentic-enough 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `a4d115d9cd08` · [字段定义](../../DATASET.md)*
