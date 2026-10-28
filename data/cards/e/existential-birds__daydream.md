# existential-birds/daydream

⭐ 21 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/existential-birds/daydream) · [官网](https://existentialbirds.com) · 组织维护

**记录审查/修复/测试轨迹的 agentic 代码审查 CLI**

命令行工具，对代码变更执行审查，可自动修复发现的问题、运行测试并提交推送；每次运行记录 ATIF 轨迹，用于面向开放权重代码审查模型的研究。后端默认使用已认证的 Claude Code CLI，也可切换 Codex、Pi 或 Osprey；发布 PR 行内评论需 gh 认证。报告写入 .review-output.md，轨迹存于 .daydream/runs/。加 --capture-data 可在本地保留不可变运行记录，上传需选择私有 Hugging Face 数据集并安装 hub extra；训练管线为 SFT→RFT→在线 RL，生产训练尚未完成。另提供自托管 GitHub bot 安装命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 审查、修复、测试、提交推送一体化的 agentic 流程
- 默认深度多栈审查，--shallow 可切单次
- 以 ATIF 轨迹形式记录每次运行，用于微调开放权重模型
- 数据捕获为可选，上传要求显式选择的私有 Hugging Face 数据集

## 适用场景

- 在合并前对分支变更做自动化代码审查并发布 PR 评论
- 让我修复审查发现的问题并跑通测试后提交
- 积累审查轨迹数据用于训练自己的代码审查模型

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L13: Daydream reviews code changes, can fix findings and run tests, and records
> L19: Requires uv, Python 3.14+, and an authenticated

## 星数曲线

```mermaid
xychart-beta
    title "existential-birds/daydream 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `8d2e337f6534` · [字段定义](../../DATASET.md)*
