# rxavier/poniard

⭐ 143 · Python · MIT · 推送 2026-08-03 · [GitHub](https://github.com/rxavier/poniard) · [官网](https://rxavier.github.io/poniard/) · 个人维护

**scikit-learn 多模型诊断与基准对比的配套库**

Poniard 是围绕 scikit-learn 的多模型诊断库：同一折上交叉验证多个模型并附 Dummy 基线，提供配对折检验、Pareto 前沿与时间预算内选模；ErrorAnalyzer 输出结构化错误报告定位失败样本；自动推断数值/类别/日期类型并生成预处理，支持网格/随机/减半调参与多样性感知的集成；最终导出无 poniard 依赖的纯 sklearn Pipeline。定位为非 AutoML、非端到端。支持 Python 3.10–3.13，跨 Linux/macOS/Windows。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同折交叉验证多模型并自动附 Dummy 基线
- 配对折检验与 Pareto 前沿、时间预算内选模
- ErrorAnalyzer 结构化错误分析报告
- 导出无 poniard 引用的纯 sklearn Pipeline

## 适用场景

- 我在多个 sklearn 模型间做同口径的交叉验证对比
- 我想知道模型 A 是否真的优于 B 还是折间噪声
- 我要分析模型在哪些样本和特征切片上失败
- 我想在时间预算内选出够好且够快的模型并导出部署

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L8: Poniard is a scikit-learn companion for **multi-model diagnostics**. Fit a handful
> L16: Then export a plain `sklearn` pipeline you own and leave. Not AutoML. Not

## 星数曲线

```mermaid
xychart-beta
    title "rxavier/poniard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 142 --> 144
    line [143, 143]
```

2026-10-18 143 → 2026-10-30 143（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `17c92f877680` · [字段定义](../../DATASET.md)*
