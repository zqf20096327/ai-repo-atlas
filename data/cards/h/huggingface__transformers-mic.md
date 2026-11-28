# huggingface/transformers-mic

⭐ 10 · Python · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/huggingface/transformers-mic) · 组织维护

**为框架 CI 提供可执行模型集成契约（MIC）标准与工具**

定义并实现 Model Integration Contract（MIC）标准：在每个 Hub 模型旁附带一份可执行检查，由使用该模型的框架 CI 运行。每个 MIC 包含三部分：由真实 checkpoint 配置收缩生成的 CPU 可运行 fixture、记录用户典型用法的可执行 Markdown 使用路径、以及经人工审核的基线输出。仓库提供 tmic CLI、fixture 构建器与运行器，契约发布于 huggingface-mic 并由数据集固定版本。fixture 在 PR 上秒级运行作为回归信号，真实 checkpoint 在合并后夜间运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- MIC 三件套：fixture、usage path、人工审核的 baselines
- tmic CLI 支持本地收缩 checkpoint 并起草契约，--mode agent 提供 JSON 协议
- fixture 在框架 PR 的 CPU 上秒级运行，作为快速回归信号
- 提出 Hub 上的 proposed link 让 agent 发现模型的 MIC

## 适用场景

- 框架维护者在 PR CI 中运行模型集成契约以捕获回归
- 为 Hub 上的模型生成可本地验证的收缩 fixture 与基线
- 通过 agent 模式用 JSON 协议自动化契约起草流程

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: A **Model Integration Contract (MIC)** is a proposed standard: next to a Hub
> L32: This repository holds the `tmic` CLI, the fixture builder and the runner. MICs are
> L36: In Transformers, the contracts job runs on PRs and reports failures without


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `00df2a8fdd7a` · [字段定义](../../DATASET.md)*
