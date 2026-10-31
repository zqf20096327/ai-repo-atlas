# VictorVVedtion/ouro-loop

⭐ 20 · Python · MIT · 推送 2026-03-16 · [GitHub](https://github.com/VictorVVedtion/ouro-loop) · [官网](https://victorvvedtion.github.io/ouro-loop/) · 个人维护

**给 AI 编码代理加约束边界的自治循环框架**

面向使用 Claude Code、Cursor、Aider、Codex 等 AI 编码代理的开发者的开源框架。开发者用 BOUND 系统定义绝对约束（DANGER ZONES、IRON LAWS），代理在边界内自主循环执行 Build → Verify → Self-Fix；验证失败时代理查阅修复手册自行回退重试。约束通过 Claude Code Hooks 在运行时强制执行（exit 2 硬阻断），而非依赖代理自觉。核心为三个文件（program.md 方法论、framework.py 运行时、prepare.py 初始化），零依赖、纯 Python 3.10+，README 标注状态为 Experimental。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- BOUND 约束系统经 Claude Code Hooks 在运行时强制执行（exit 2 硬阻断）
- 六阶段循环 BOUND→MAP→PLAN→BUILD→VERIFY→LOOP，失败时自主修复并报告
- 5 个验证门 + 三层反思日志（WHAT/WHY/PATTERN），结果写入 TSV 可审计
- 零依赖，纯 Python 3.10+，提供 ouro CLI

## 适用场景

- 让 AI 代理在受保护文件（支付、鉴权、共识）之外通宵自主开发
- 长周期重构或自主研究任务中防止代理越界或陷入修复循环
- 对 AI 代理的自治开发过程留下可审计的记录

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L16: **Ouro Loop** is an open-source framework that gives AI coding agents (Claude Code, Cursor, Aider, Codex) a structu
> L22: |**What you get**|`program.md` (method) + `framework.py` (runtime) + `sentinel.py` (24/7 review) + 5 hooks (enforce
> L50: - **`program.md`** — the methodology instructions. Defines the six-stage loop (BOUND, MAP, PLAN, BUILD, VERIFY, LOO

## 星数曲线

```mermaid
xychart-beta
    title "VictorVVedtion/ouro-loop 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-31 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `657b858a181c` · [字段定义](../../DATASET.md)*
