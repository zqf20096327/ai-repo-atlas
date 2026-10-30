# Tencent-Hunyuan/C3-Benchmark

⭐ 38 · Python · NOASSERTION · 推送 2026-03-01 · [GitHub](https://github.com/Tencent-Hunyuan/C3-Benchmark) · 组织维护 · 中文 README

**评测 LLM Agent 多轮工具调用鲁棒性的基准数据集与评测框架**

开源基准 C^3-Bench，面向基于 LLM 的工具调用 Agent：设计三项挑战（复杂工具关系导航、关键隐藏信息处理、动态决策路径管理），测试数据经五轮人工校验，支持中英双语；评测框架分离推理与结果分析，采用标准 ToolCalls 协议，支持 API 模型与 HuggingFace 开源模型（可用 vllm 部署），输出多维度 CSV 分析结果。README 声明本仓库已迁移至 WildToolBench 仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三项挑战设计：工具关系导航、隐藏信息、动态决策路径
- 测试数据经五轮人工校验，中英双语
- 标准 ToolCalls 协议，支持 API 模型与 vllm/HuggingFace 开源模型
- 六维度结果分析，输出 CSV 供 bad case 分析

## 适用场景

- 评测自研或开源 Agent 模型的多轮工具调用能力
- 分析模型在工具依赖与长上下文上的错误类型
- 复现论文中的 49 个主流 Agent 实验结论

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L21: To bridge this gap, we present an open-source and high-quality benchmark C^3-Bench.
> L22: This benchmark integrates attack concepts and applies univariate analysis to pinpoint key elements affecting agent 
> L31: - Test data location: c3_bench/data/C3-Bench.jsonl or 🤗 Dataset

## 星数曲线

```mermaid
xychart-beta
    title "Tencent-Hunyuan/C3-Benchmark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-30 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `14b1696d5a21` · [字段定义](../../DATASET.md)*
