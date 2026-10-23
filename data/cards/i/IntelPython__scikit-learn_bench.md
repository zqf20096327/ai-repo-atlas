# IntelPython/scikit-learn_bench

⭐ 124 · Python · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/IntelPython/scikit-learn_bench) · 组织维护

**跨框架机器学习算法基准测试工具，面向 sklearn 类 API 库**

IntelPython 维护的基准测试工具，对实现 Scikit-learn 类 API 及其他工作负载的库和框架进行性能与质量指标评测。通过 CLI 控制基准套件，以 JSON 配置定义基准用例，运行 sklbench 模块输出 JSON 结果，并支持生成 Excel 人类可读报告，可合并多环境结果。描述中提及支持 scikit-learn、DAAL4PY、cuML、XGBoost 等框架，README 中列出 sklearn/sklearnex 与 RAPIDS 环境的 pip/conda 安装配置。

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

- CLI 全量控制基准套件，配置结构灵活
- 支持性能与质量两类指标（estimator/function 两种基准类型）
- 自动生成基准报告，可合并多环境结果文件
- 提供 Intel VTune Profiler 等分析工具接入

## 适用场景

- 对比不同 ML 框架在同一算法上的性能表现
- 在不同环境间汇总基准测试结果生成报告
- 对 sklearn 类估计器做质量与性能回归评测

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: **Scikit-learn_bench** is a benchmark tool for libraries and frameworks implementing Scikit-learn-like APIs and othe
> L83:  - **Scikit-learn estimator** - Measures performance and quality metrics of the sklearn-like estimator.

## 星数曲线

```mermaid
xychart-beta
    title "IntelPython/scikit-learn_bench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 123 --> 125
    line [124, 124]
```

2026-10-18 124 → 2026-10-23 124（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `b681658246b5` · [字段定义](../../DATASET.md)*
