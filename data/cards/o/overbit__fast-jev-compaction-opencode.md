# overbit/fast-jev-compaction-opencode

⭐ 14 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/overbit/fast-jev-compaction-opencode) · [官网](https://overbit.github.io/fast-jev-compaction-opencode/) · 个人维护

**OpenCode 插件：用 JEV 决策模型剪除陈旧工具历史做上下文压缩**

面向 OpenCode V2 的上下文压缩插件，从 tamaratran/fast-jev-compaction 移植。不请生成模型改写对话为摘要，而是由 JEV 分类器对已完成的工具调用与输出做去留判定：保留的文本原样复制进 checkpoint，最新消息默认置顶；分类失败或压缩比不足时回退到 OpenCode 原生压缩。后端支持托管 TypeSafe JEV 与本地 System One（LM Studio 0.4.26+ / Ollama 0.35+），保留旧版 LM Studio chat 适配器。适合长会话、工具调用密集的编码任务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 按 keepThreshold 对工具调用/输出做分类式剪除而非 LLM 摘要改写
- 支持托管 TypeSafe JEV 与本地 System One（LM Studio/Ollama）后端
- 分类失败或压缩比不足时回退 OpenCode 原生压缩
- 写入诊断日志记录后端、候选数、压缩比与覆盖/回退原因

## 适用场景

- 长编码会话中削减工具输出堆积的上下文
- 在本地用 LM Studio/Ollama 跑 0.8B 决策模型做无摘要压缩
- 希望保留精确路径/命令等细节、不依赖 LLM 改写的压缩方案

## 场景标签

 · 领域:开发工具/LLM Agent 基础设施

## 证据(README 行号)

> L7: **JEV-guided context compaction for OpenCode V2.**
> L94: opencode plugin add github:overbit/fast-jev-compaction-opencode
> L351: Plugin.define({

## 星数曲线

```mermaid
xychart-beta
    title "overbit/fast-jev-compaction-opencode 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `1dde82ea2e8e` · [字段定义](../../DATASET.md)*
