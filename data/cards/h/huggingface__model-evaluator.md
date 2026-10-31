# huggingface/model-evaluator

⭐ 14 · Python · Apache-2.0 · 推送 2026-09-24 · [GitHub](https://github.com/huggingface/model-evaluator) · [官网](https://huggingface.co/spaces/autoevaluate/model-evaluator) · 组织维护

**向 AutoTrain 提交 Hub 模型评测任务的 Streamlit 应用**

Hugging Face 官方的模型评测前端：基于 Streamlit 的 Space，用户通过 UI 选择模型与数据集提交评测任务，后端由 AutoTrain 执行，支持二分类、多分类、实体抽取、抽取式问答、翻译、摘要、图像分类、零样本文本评测等 10 种任务。评测触发由 GitHub Actions cron 每 15 分钟运行 run_evaluation_jobs.py 完成。项目已声明归档（archived）。本地运行需 pip 安装依赖并配置 HF_TOKEN 与 AUTOTRAIN_BACKEND_API 环境变量。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 UI 向 AutoTrain 后端提交模型评测任务
- 支持 10 种评测任务（含图像分类与零样本评测）
- GitHub Actions cron 每 15 分钟自动触发就绪的评测
- 可切换连接本地 AutoTrain 实例

## 适用场景

- 在 Hugging Face Hub 上为 Transformers 模型发起评测
- 配合本地 AutoTrain 实例运行模型评测
- 通过 UI 提交任务后由定时脚本自动完成评测触发

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L11: > Submit evaluation jobs to AutoTrain from the Hugging Face Hub
> L56: 1. Submitting an evaluation job via the UI. This creates an AutoTrain project with `N` models for evaluation. At th

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/model-evaluator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `2208894fb71a` · [字段定义](../../DATASET.md)*
