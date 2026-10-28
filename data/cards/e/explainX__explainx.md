# explainX/explainx

⭐ 454 · Python · MIT · 推送 2026-07-13 · [GitHub](https://github.com/explainX/explainx) · 组织维护

**黑盒 ML 模型的解释与调试 Python 库，可经 MCP 供 LLM agent 调用**

explainX 3.0 是可解释性（XAI）引擎：对已训练的任意框架模型（scikit-learn/XGBoost/PyTorch/Keras 等）输出全局与局部特征重要性（SHAP/LIME）、反事实与 recourse、公平性检验与偏差缓解、保形预测、数据漂移检测、标签问题与泄漏诊断等，结果为结构化 JSON 对象并生成自然语言摘要。提供 Python API、CLI、Streamlit 仪表盘与 MCP 服务器，使 Claude 等 agent 可作为工具调用 22 个解释/诊断函数。注意 3.0 尚未发布到 PyPI，pip install explainx 仍装旧版 2.x，需从 GitHub 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 统一 API 覆盖 SHAP/LIME/Anchors/反事实/ALE/公平性/保形预测等 XAI 方法
- 结果为结构化 JSON + 自然语言摘要，经 MCP 供 Claude 等 agent 调用（22 个工具）
- 数据为中心诊断：误差切片、标签问题、目标泄漏、校准评估
- 提供 CLI、HTML 报告导出与 Streamlit 交互式仪表盘

## 适用场景

- 解释模型预测原因，向利益相关方或 agent 提供可读摘要
- 检测并缓解模型对敏感属性的群体性偏差
- 用反事实分析找到翻转某条决策的最小改动
- 让 LLM agent 在建模流程中调用解释与诊断工具闭环修复数据

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: **explainX 3.0** is a modern, **LLM-native** rewrite of the explainability
> L13: from plain Python *and* over the **Model Context Protocol (MCP)** so agents like
> L208: ## Use it from an LLM agent (MCP)

## 星数曲线

```mermaid
xychart-beta
    title "explainX/explainx 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-28"]
    y-axis "stars" 452 --> 455
    line [453, 454, 454]
```

2026-10-18 453 → 2026-10-28 454（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `ee4b11f3c0a9` · [字段定义](../../DATASET.md)*
