# sruja-ai/sruja

⭐ 24 · Rust · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/sruja-ai/sruja) · [官网](https://sruja.ai/) · 组织维护

**带确定性验证门的 CLI 自主编程 agent**

Sruja 是 CLI 优先的自主编程 agent，运行 comprehend → plan → execute → critique → replan 闭环，由预算、迭代次数与文件守卫约束边界；同时可作为被动 harness 经 MCP 嵌入 Cursor、Copilot、Claude、Windsurf 等编辑器，由宿主 LLM 驱动。核心机制是独立于执行模型之外的确定性验证层（drift、lint、verify-task、intent check），即写代码的模型不评判自己的产出。安装提供 shell 脚本、cargo 与源码构建三种途径；README 列出动态导入、反射/DI 等已知限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自主 agent loop 与编辑器内 MCP harness 两种运行方式
- drift/lint/verify-task/intent check 独立确定性验证层
- 编辑前提供文件级结构简报（依赖、影响半径、相关决策）
- 支持结构化上下文摄取与决策记录（ingest、decision add）

## 适用场景

- 让 agent 自主完成重构等编码任务并在提交前通过确定性验证
- 在 Cursor/Copilot 等编辑器中为自己的 LLM 附加接地上下文与编辑后验证门
- 团队在 CI 中运行 drift 与 reviewed intent 边界检查

## 场景标签

 · 领域:开发者工具/AI 编程

## 证据(README 行号)

> L5: **Sruja is a CLI-first autonomous coding agent where the actor never grades itself.** It scans your repo, grounds ev
> L16: The deterministic layer (`drift`, `lint`, `verify-task`, `intent check`) is the **independent grader** — the model 
> L111: |**Autonomous mode**|Host-managed agent loop|`sruja agent loop` — owns the full observe → act → verify → critique 

## 星数曲线

```mermaid
xychart-beta
    title "sruja-ai/sruja 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `6c067833cab7` · [字段定义](../../DATASET.md)*
