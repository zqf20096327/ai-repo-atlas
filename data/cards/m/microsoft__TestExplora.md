# microsoft/TestExplora

⭐ 16 · Python · MIT · 推送 2026-03-26 · [GitHub](https://github.com/microsoft/TestExplora) · 组织维护

**仓库级测试生成基准：评测 LLM 主动发现软件缺陷能力**

论文 TestExplora 的官方实现：一个 repository 级 benchmark，评测 LLM 通过生成测试用例主动发现潜在软件缺陷的能力。数据集来自真实 GitHub PR，含 2,389 个测试生成任务（覆盖 482 个仓库），要求模型写出能在缺陷版与修复版间触发 Fail-to-Pass 转换的测试。支持 API 模型（GPT/Claude/Gemini）与 agent 模型（SWE-agent、Trae-agent），通过 inference harness 驱动生成测试补丁，并用 Docker 在本地执行评测；另提供从自有仓库构建同类基准的流水线脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 2,389 个测试生成任务，来自 482 个仓库的 1,552 个真实 PR
- 任务要求触发 buggy/修复版之间的 Fail-to-Pass 转换
- 支持 API 模型与 agent 模型（SWE-agent/Trae-agent）评测
- 提供 AST 分析与依赖图构建的基准数据集生成流水线

## 适用场景

- 评测代码 LLM 在仓库级场景下主动发现缺陷的能力
- 复现论文中的 baseline 评测结果
- 从自己的 GitHub 仓库构建类似的测试生成基准

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: This repository is the official implementation of the paper "TestExplora: Benchmarking LLMs for Proactive Bug Discov
> L9: TestExplora is a systematic, repository-level benchmark designed to evaluate the capability of Large Language Models

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/TestExplora 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `76be8e969477` · [字段定义](../../DATASET.md)*
