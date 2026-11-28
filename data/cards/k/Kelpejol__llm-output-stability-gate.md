# Kelpejol/llm-output-stability-gate

⭐ 10 · Python · MIT · 推送 2026-01-21 · [GitHub](https://github.com/Kelpejol/llm-output-stability-gate) · 个人维护

**检测 AI 生成代码不稳定性的 CLI 可靠性门槛工具**

基于 UQLM（语言模型不确定性量化）的 CLI 工具：对同一 prompt 生成 5 次回答，通过多采样一致性计算置信度分数（0.0-1.0），输出不一致点、共识元素、分歧分析与建议（使用/复查/拒绝），并给出单条、批量与多模型对比三种分析模式。附带 30 条 prompt、5 类别的基准测试脚本与 pytest 测试。定位为 AI 生成代码合入前的检查工具，面向需要审查 AI 代码（如 Copilot 建议）的开发者与团队。限制：不证明正确性、不能替代测试、单次分析需 5-10 秒、仅针对代码生成 prompt。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多次采样一致性测量，输出置信度分数与分歧分析
- 支持单条、批量文件与多模型对比三种分析模式
- 附带 30 prompt×5 类别的基准脚本（run_benchmark.py）
- 基于 UQLM 库与语义一致性研究实现

## 适用场景

- 合入 Copilot 生成的代码前先测置信度
- 安全相关代码（认证/加密）生成后的复查门槛
- 团队用统一标准检查 AI 代码产出
- 批量分析 prompt 列表定位模型不稳定的任务类型

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L8: A CLI tool that detects when AI-generated code is unreliable by measuring output consistency using UQLM (Uncertainty
> L20: UQLM-Guard asks the same question multiple times and **flags code where the AI is uncertain**.
> L104: │ 1. Generate Multiple Responses (5x)        │

## 星数曲线

```mermaid
xychart-beta
    title "Kelpejol/llm-output-stability-gate 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-11-28"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-26 10 → 2026-11-28 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `c7ca259d9c49` · [字段定义](../../DATASET.md)*
