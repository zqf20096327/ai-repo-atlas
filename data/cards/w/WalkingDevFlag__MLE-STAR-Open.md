# WalkingDevFlag/MLE-STAR-Open

⭐ 34 · Python · 推送 2026-06-16 · [GitHub](https://github.com/WalkingDevFlag/MLE-STAR-Open) · 个人维护

**多 agent 机器学习工程管线：自动生成、调试并提交 Kaggle 表格赛方案**

MLE-STAR 的非官方、去 Google 依赖重实现：多阶段 agent 管线覆盖初始化、精炼、集成与提交，面向表格数据任务自动生成与调试 ML 方案，输出 Kaggle 格式的预测文件。LLM 后端通过 OpenAI 兼容 API 使用 OpenRouter（免费档约 50 次/天），Ollama 本地适配器暂缓实现；搜索用 DuckDuckGo（无需 API key）。含基础数据泄漏检查与低 token 消耗的最小运行器。从源码运行，需 Python 3.12+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多 agent 阶段：初始化 → 精炼 → 集成 → 提交
- OpenRouter LLM 后端（OpenAI 兼容 API）
- DuckDuckGo 搜索，无需 API key
- 自动基础数据泄漏/数据使用检查与 Kaggle 提交格式化辅助

## 适用场景

- 自动生成并迭代表格数据任务的 Kaggle 竞赛方案
- 在本地小规模实验 agent 驱动的 ML 工程流程
- 低 token 消耗下用最小运行器跑通单个任务

## 场景标签

`多智能体` `数据分析` · 领域:Agent 开发

## 证据(README 行号)

> L9: - Multi-agent stages: initialization → refinement → ensembling → submission
> L3: A Google-free, local-friendly reimplementation of the MLE-STAR multi‑agent ML engineering pipeline.

## 星数曲线

```mermaid
xychart-beta
    title "WalkingDevFlag/MLE-STAR-Open 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-30 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `01b9bf9e98e3` · [字段定义](../../DATASET.md)*
