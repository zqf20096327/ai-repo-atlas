# unbreaking-lab/blunderbuss

⭐ 5 · Rust · NOASSERTION · 推送 2026-11-26 · [GitHub](https://github.com/unbreaking-lab/blunderbuss) · [官网](https://unbreakinglab.org/project/blunderbuss) · 个人维护

**面向开发者的安全约束型 LLM 编码任务执行器**

Rust 编写的 LLM 编码 harness：用户在 blunderbuss.local.md 中以 markdown+yaml 前置描述任务与配置，工具经 shlex 解析为前缀白名单授权，任务开始时创建临时 git commit 保证变更可回退，结束前须通过 check 命令才判定成功，不提供多轮对话与 LLM 生成总结。基于 genai crate 支持多供应商模型接入，以 cargo 安装、命令 blb 调用。定位为规避现有 harness 交互缺陷的替代方案。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 允许清单式工具授权，仅可访问当前工作目录内未被 git ignore 的文件
- git 临时 commit 检查点，所有变更（含 shell 命令产生的）可回退
- 任务须通过 check 命令才判定成功，失败自动开启新一轮
- 基于 genai crate，支持 40+ 供应商前缀接入

## 适用场景

- 给 AI 派发编码任务后无需盯守终端，回来决定保留或回退
- 限制 AI 只能调用指定 shell 命令以缩小破坏面
- 需要随时切换 LLM 供应商的本地编码自动化

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L9: `blunderbuss` is a coding harness that acknowledges LLMs are dangerous, not just because they often take unexpected 
> L22: - **Vendor agnostic:** `blunderbuss` is built on the `genai` crate, and so allows you to use any provider/model you
> L56: - **`model`:** Specifies the model to use for this task, with a provider specified before the `::`. Full reference 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `ddc7bd169572` · [字段定义](../../DATASET.md)*
