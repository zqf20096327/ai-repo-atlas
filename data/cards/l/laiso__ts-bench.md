# laiso/ts-bench

⭐ 243 · TypeScript · MIT · 推送 2026-08-14 · [GitHub](https://github.com/laiso/ts-bench) · [官网](https://laiso.github.io/ts-bench/) · 个人维护

**在 TypeScript 工作负载上对比 AI 编码 agent 的基准 CLI**

命令行基准工具：运行指定 agent 与模型，执行测试并输出通过/失败，跨模型与提供商对比。内置 v1 数据集（25 个 Exercism TypeScript 练习，无需 Docker）与 v2 数据集（Expensify 单体仓库真实任务，需 Docker），v1 提供冻结基线 tag（v1-final）保证可复现。支持 claude、grok、agy 等 agent，可通过 XAI_API_KEY/GEMINI_API_KEY 或订阅认证运行，结果发布于 GitHub Actions 与 Releases。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 运行 agent→执行测试→输出 pass/fail 的跨模型对比流程
- 两个数据集：v1 Exercism 练习（无 Docker）与 v2 SWE-Lancer 真实任务（需 Docker）
- v1 冻结基线 tag v1-final 用于可复现性
- 订阅认证方式运行 claude/gemini/codex/copilot 等 agent

## 适用场景

- 对比不同模型在 TypeScript 编码任务上的通过率
- 在 CI 中跑基准并追踪结果
- 评估 agent 在真实单体仓库任务上的表现

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Benchmark CLI for comparing AI coding agents on TypeScript workloads. Run an agent, execute tests, get pass/fail — a
> L8: ts-bench --agent claude --model <model>
> L15: ### v1 — Exercism (default)

## 星数曲线

```mermaid
xychart-beta
    title "laiso/ts-bench 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 241 --> 244
    line [242, 243, 243]
```

2026-10-18 242 → 2026-10-30 243（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `6a4d764c2a7f` · [字段定义](../../DATASET.md)*
