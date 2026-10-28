# logic-star-ai/swt-bench

⭐ 92 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/logic-star-ai/swt-bench) · [官网](https://swtbench.com/) · 组织维护

**评测 LLM 仓库级测试生成能力的基准与 Docker 评测框架**

NeurIPS 2024 论文的基准与评测框架：给定代码库与 GitHub issue，让模型生成复现性测试——在原始代码上失败、在修复补丁后通过。提供基于 Docker 的可复现评测 harness，支持单元测试模式与复现脚本模式，输出成功率、覆盖增量等指标；提供数据集下载、结果提交排行榜与零样本数据构建脚本。基于 SWE-Bench 工具链构建，推荐 x86_64、120GB 存储、16GB 内存、8 核环境运行。给研究 LLM 代码/测试能力的科研人员使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 任务定义：生成在修复前失败、修复后通过的复现测试
- Docker 化可复现评测 harness，支持单元测试/复现脚本两种模式
- 提供 SWT-Bench / Lite / Verified 数据集与排行榜提交流程
- 复用 SWE-Bench 工具链，支持自建数据集与零样本推理

## 适用场景

- 评测代码 agent 或 LLM 在真实软件缺陷上的测试生成能力
- 复现论文中 SWE-Agent、OpenHands 等方法的结果
- 构建自定义 SWE-Bench 风格数据集并生成零样本基线

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L12: SWT-Bench is a benchmark for evaluating large language models on testing generation for real world software issues 
> L13: Given a *codebase* and an *issue*, a language model is tasked with generating a *reproducing test* that fails in th
> L165: This repo is based on the SWE-Bench evaluation harness and we want to thank all their contributors.

## 星数曲线

```mermaid
xychart-beta
    title "logic-star-ai/swt-bench 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 90 --> 93
    line [91, 92, 92]
```

2026-10-18 91 → 2026-10-28 92（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `1c81b272d3f9` · [字段定义](../../DATASET.md)*
