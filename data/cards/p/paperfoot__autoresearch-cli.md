# paperfoot/autoresearch-cli

⭐ 33 · Rust · MIT · 推送 2026-04-17 · [GitHub](https://github.com/paperfoot/autoresearch-cli) · 个人维护

**让任意 AI 编程代理通宵跑自主实验循环的 Rust CLI**

单个约 1.1 MB 的 Rust 二进制，把自主实验循环模式工具化：用户在 autoresearch.toml 中定义一个可修改文件、一个待优化指标和一个评估命令，由 AI 编程代理执行实验循环，CLI 负责脚手架、14 项预检、JSONL 原子记录、实验历史与 diff、fork 并行分支、跨模型 review 提示生成与 markdown 报告。开箱支持 Claude Code、Codex、Cursor、Windsurf 等 8 类代理。支持 cargo install、Homebrew 与安装脚本三种安装方式，无 Python/Node/Docker 依赖。

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

- 与 8 类主流 AI 编程代理开箱配合（安装技能/斜杠命令/自动发现）
- doctor 预检、record 原子 JSONL 记录、log/best/diff/status 实验追踪
- fork 多方向并行实验与 merge-best 分支择优
- 所有命令支持 --json 结构化输出，代理端命令返回带 suggestion 的 JSON 信封

## 适用场景

- 让 Claude Code 等代理通宵迭代 ML 训练脚本并自动保留优胜实验
- 对有可量化指标的项目（引擎 Elo、API 延迟等）跑自主优化循环
- 实时用 watch 面板监控通宵实验进度并生成报告

## 场景标签

`编码 Agent` `MLOps` · 领域:编码与开发

## 证据(README 行号)

> L14: A single Rust binary that turns any AI coding agent into an autonomous research machine. Define one file to modify,
> L24: But every project reimplements this from scratch -- copying `program.md`, figuring out the eval, hand-writing JSONL
> L64: The CLI handles everything except the loop itself:

## 星数曲线

```mermaid
xychart-beta
    title "paperfoot/autoresearch-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-28 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `aa200680c072` · [字段定义](../../DATASET.md)*
