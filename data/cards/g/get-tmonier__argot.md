# get-tmonier/argot

⭐ 51 · Rust · MIT · 推送 2026-10-01 · [GitHub](https://github.com/get-tmonier/argot) · [官网](https://argot.tmonier.com) · 个人维护

**基于仓库历史学习的本地统计代码审查工具，检测偏离代码库惯例的变更**

以 Rust 单二进制形式分发的命令行工具：从仓库自身 Git 历史拟合统计基线（argot init/audit/check），对新变更检测 12 类规则，如陌生依赖导入、罕见 token 序列、重复函数、测试被删减、分层方向反转等。完全本地运行，语义检测所用的 15.6M 参数嵌入模型编译进二进制，无生成式模型参与判定。支持 12 种语言，提供 CLI、MCP 服务器、Claude Code 插件、pre-commit 钩子与 GitHub Action 等接入方式。限制：历史浅或生成的仓库可能产出无用基线；结果为审查提示而非正确性证明。

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

- 从仓库 Git 历史学习基线，检测 12 类偏离惯例的规则
- 100% 本地运行，嵌入模型编译进单个静态链接 Rust 二进制
- 支持 12 种语言，在 36 个真实仓库上做了基准测量
- 提供 CLI / MCP / Claude Code 插件 / pre-commit / GitHub Action 多种接入方式

## 适用场景

- 我想在 code review 中拦截引入仓库从未用过的依赖或重复实现的 PR
- 我想为 AI 生成的代码加一道基于本仓库惯例的守护栏
- 我想在 CI 中对变更集做同基线的一致性评分

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5:  AI writes the code. argot harnesses it with the one thing that can’t
> L7:  Statistics, not a second LLM. 100% local. It surfaces the divergence — you
> L119: argot is a probabilistic review guardrail, not a correctness oracle. Each

## 星数曲线

```mermaid
xychart-beta
    title "get-tmonier/argot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-27 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `45e079209b6c` · [字段定义](../../DATASET.md)*
