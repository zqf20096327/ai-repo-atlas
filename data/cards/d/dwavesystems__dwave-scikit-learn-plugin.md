# dwavesystems/dwave-scikit-learn-plugin

⭐ 18 · Python · Apache-2.0 · 推送 2026-01-14 · [GitHub](https://github.com/dwavesystems/dwave-scikit-learn-plugin) · 组织维护

**scikit-learn 插件：用量子-经典混合求解器做特征选择**

D-Wave 出品的 scikit-learn 插件包，提供 SelectFromQuadraticModel 转换器，在任意 sklearn 流水线中调用 Leap 量子-经典混合求解器（CQM/NL）完成特征选择；开发者需注册 Leap 量子云服务（可免费开始）。支持设置 time_limit 应对大规模问题，可配合 sklearn 的网格搜索等超参数优化器使用（会向混合求解器提交多次问题）。以 pip 包形式安装。

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

- 提供 SelectFromQuadraticModel，可嵌入任意 sklearn 流水线
- 调用 Leap 量子云的 CQM/NL 混合求解器
- 支持 time_limit 调整与 sklearn 超参数优化器配合

## 适用场景

- 在现有 sklearn 流水线中用混合求解器做特征选择
- 对高维数据集挑选指定数量的特征
- 通过网格搜索调优特征数量

## 场景标签

 · 领域:数据科学/量子机器学习

## 证据(README 行号)

> L6: This package provides a scikit-learn transformer for
> L15: The package's main class, `SelectFromQuadraticModel`, can be used in any existing `sklearn` pipeline.

## 星数曲线

```mermaid
xychart-beta
    title "dwavesystems/dwave-scikit-learn-plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `0ce64007826c` · [字段定义](../../DATASET.md)*
