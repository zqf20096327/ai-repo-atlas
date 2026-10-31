# chaohong-ai/ai-auto-work

⭐ 134 · Shell · 推送 2026-07-26 · [GitHub](https://github.com/chaohong-ai/ai-auto-work) · 个人维护 · 中文 README

**Claude+Codex 双模型对抗协作的自动化全周期开发工作流**

运行于 Claude Code 内的 agentic coding 工作流命令集：Claude 作执行者、Codex 作对抗审查者，通过 Triple-Check 收敛循环自动完成需求调研→审查→规划→审查→开发→开发审查直至提交。提供三种模式：全自动 /auto-work、小改动快速路径 /fast-auto-work、带人工检查点的 /manual-work，另有计划生成、技术研究、bug 修复与安全 git 操作等子命令。任务按 S/M/L 分级并分解为原子提交（≤3 实现文件、估计 ≤100 行）；每阶段隔离进程、以持久化文件交接；编译与测试门禁未过则失败关闭。Codex 不可用时回退为独立 Claude 审查者；工作流本身语言无关，内置 constitution 针对 Go/TypeScript/Python/GDScript 配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Claude 执行 + Codex 对抗审查的双模型 Triple-Check 收敛循环
- S/M/L 复杂度分级与原子任务分解（≤3 实现文件 / 估计 ≤100 行）
- 每阶段隔离进程、文件化交接，避免上下文污染
- 系统性错误写入 .ai/ 共享知识库，后续运行自动加载

## 适用场景

- 让 AI 自主完成从中大型功能需求到代码提交的完整开发周期
- 小改动走快速路径，经编译与测试门禁快速验证
- 在关键里程碑保留人工审查节点的半自动开发

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L12: Automatically completes the full pipeline: **Requirement Research → Research Review → Planning → Plan Review → Deve
> L16: AI Auto-Work is an **agentic coding workflow system** that orchestrates large language models (LLMs) to complete re

## 星数曲线

```mermaid
xychart-beta
    title "chaohong-ai/ai-auto-work 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 132 --> 135
    line [133, 134, 134]
```

2026-10-18 133 → 2026-10-31 134（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `328e2e100ee8` · [字段定义](../../DATASET.md)*
