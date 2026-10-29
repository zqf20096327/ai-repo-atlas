# leockl/sklearn-diagnose

⭐ 61 · Python · MIT · 推送 2026-01-30 · [GitHub](https://github.com/leockl/sklearn-diagnose) · 个人维护

**给 ML 从业者：用 LLM 诊断 scikit-learn 模型失效原因**

面向使用 scikit-learn 的数据科学与 MLOps 从业者的 Python 诊断库：先由信号提取器从模型与数据计算确定性统计量，再通过 LangChain 驱动的三个 LLM agent 生成失效模式假设（带置信度与证据）、修复建议与人类可读总结，可检测过拟合、欠拟合、标签噪声、类不平衡、数据泄漏等。附带 FastAPI Web 聊天机器人（内置 React 前端，无需 Node.js）。只读设计，不修改模型与数据。需配置 LLM API key（OpenAI/Anthropic/OpenRouter）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性信号提取 + LLM 假设/建议/总结三阶段生成
- 检测过拟合、欠拟合、标签噪声、特征冗余、类不平衡、数据泄漏等失效模式
- 只读保证：不调用 fit、不修改估计器参数与数据
- 内置 Web 聊天机器人（FastAPI + 打包 React 前端，无需 Node.js）

## 适用场景

- 训练后模型表现不佳时定位过拟合或数据泄漏等原因
- 通过对话式界面询问诊断结果与修复代码示例
- 在 MLOps 流程中对已拟合的 sklearn 模型做失效诊断

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L15: 1. **Signal Extractors**: Compute deterministic statistics from your model and data
> L16: 2. **LLM Hypothesis Generation**: Detect failure modes with confidence scores and severity
> L261: sklearn-diagnose uses **LangChain** under the hood for LLM integration. Each diagnosis involves three AI agents:

## 星数曲线

```mermaid
xychart-beta
    title "leockl/sklearn-diagnose 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-29 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e952ddd65e88` · [字段定义](../../DATASET.md)*
