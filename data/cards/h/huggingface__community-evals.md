# huggingface/community-evals

⭐ 14 · Python · Apache-2.0 · 推送 2026-03-23 · [GitHub](https://github.com/huggingface/community-evals) · 组织维护

**社区工具：向 HF 模型仓库提交结构化评测结果 PR**

Hugging Face 社区评测工具仓库：从模型卡 README 表格或 Artificial Analysis API 读取开源模型在 HLE、GPQA、MMLU-Pro、GSM8K 等基准上的分数，转为 .eval_results/ YAML 格式，通过 Pull Request 写入模型仓库，使结果出现在模型页与基准数据集排行榜。支持单模型添加与热门模型批量处理（含 dry run 预览），并附带 Claude Code skill 供 agent 自动化操作。需 HF_TOKEN 写权限，papers 来源标注未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从模型卡/Artificial Analysis 提取分数生成 .eval_results/ YAML
- 通过 PR 向模型仓库提交社区评测结果并登上排行榜
- 支持热门模型批量处理与 dry run 预览
- 内置 Claude Code skill 支持 agent 自动化工作流

## 适用场景

- 为开源模型补充 HLE/GPQA 等基准的结构化评测结果
- 批量处理热门模型并向其仓库提交评测 PR
- 让 AI agent 自动完成评测提取与 PR 提交流程

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: A repository for community-driven evaluation results for open source models on HuggingFace Hub.
> L5: This project adds structured evaluation results to model repositories using the new `.eval_results/` format, enablin
> L13: ## Supported Benchmarks

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/community-evals 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `f0a4e505a6e1` · [字段定义](../../DATASET.md)*
