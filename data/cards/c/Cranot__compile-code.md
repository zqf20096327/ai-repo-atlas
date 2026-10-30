# Cranot/compile-code

⭐ 29 · Python · Apache-2.0 · 推送 2026-09-07 · [GitHub](https://github.com/Cranot/compile-code) · 个人维护

**为编码 agent 预解析代码库事实的本地 CLI 编译器**

roam-code 引擎之上的薄 CLI：在编码 agent 首个 token 之前，用确定性正则与本地代码图（28 种语言索引）将提示词分类到 22 个意图过程，预执行探查并注入约 10 KB 的事实信封（调用方、git 历史、影响面、bug 位点源码），全程零模型调用；agent 编辑后对其改动的行运行范围化校验，返回 fix-or-suppress 清单。可接入 Claude Code（compile claude / compile wire claude）或独立运行。尚未发布到 PyPI，需从 git 安装 main 分支，要求 Python 3.10+ 与 git 仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 提示词分类到 22 个意图过程，预执行探查并注入约 10 KB 事实信封
- 零模型调用、本地运行，支持 28 种语言索引
- agent 编辑后对改动行运行范围化 fail-closed 校验
- 可接入 Claude Code 或以 compile run 独立使用

## 适用场景

- 让编码 agent 在导航/理解类任务中跳过 grep 与读文件步骤
- 改动前先拿到影响面与受影响测试列表
- 编辑完成后自动检查命名约定与无效 import 等问题

## 场景标签

 · 领域:开发者工具/代码智能

## 证据(README 行号)

> L5: Pre-resolves the mechanical work — who calls this, what changed recently, what breaks if I touch it, where the bug-s
> L14:  A thin CLI over the roam-code engine (installed automatically) · 22 canonical intent procedures in Roam 13.10 · 28
> L218: The compiler classifies your prompt into one of 22 canonical intent procedures

## 星数曲线

```mermaid
xychart-beta
    title "Cranot/compile-code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-30 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `59a583fddd61` · [字段定义](../../DATASET.md)*
