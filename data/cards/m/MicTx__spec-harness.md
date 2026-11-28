# MicTx/spec-harness

⭐ 317 · Python · NOASSERTION · 推送 2026-11-27 · [GitHub](https://github.com/MicTx/spec-harness) · 个人维护 · 中文 README

**给 AI 编程智能体提供任务包工作流：范围冻结、证据门禁与 Git 交付**

一个面向 AI 编程智能体的两相任务包工作流工具：先冻结目标与验收标准，再按证据执行、恢复和交付。通过 /spec 系列命令创建任务包、lint 规划、按恢复循环验证修复、在用户授权后完成 Git 交付。提供安装器自动探测宿主（Claude Code、Codex、Gemini 等），配置对应 hook；更新命令支持 GitHub 与国内镜像双源。需要 Python 3.9+、Git、Bash。许可为 PolyForm Noncommercial，商业使用需另行授权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- /spec 命令族覆盖规划、执行、修复、验证与 Git 交付全流程
- 安装器自动探测宿主，支持 claude/codex/gemini/cursor 等多种 INSTALL_HOSTS 配置
- spec-harness update 支持 GitHub 与国内镜像源，带校验与旧版备份
- 证据记录退出 Git 索引的 purge 机制，本地归档保留完整运行历史

## 适用场景

- 让 AI 智能体执行有验收标准的长期改动，避免范围漂移
- 在 Claude Code / Codex 等宿主中启用规范驱动的开发流程
- 多宿主环境下统一安装、更新和管理任务包工作流

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: 面向 AI 编程智能体的两相任务包工作流：先冻结目标和验收，再按证据执行、恢复和交付。
> L31: |DeepSeek Harness / Cursor|`dsh` / `cursor`|

## 星数曲线

```mermaid
xychart-beta
    title "MicTx/spec-harness 星数(近 16 点)"
    x-axis ["2026-10-26", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-27", "2026-11-28"]
    y-axis "stars" 0 --> 347
    line [10, 31, 10, 285, 297, 300, 302, 307, 310, 311, 312, 313, 314, 316, 317, 317]
```

2026-10-26 10 → 2026-11-28 317（+307）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `94aae40663ae` · [字段定义](../../DATASET.md)*
