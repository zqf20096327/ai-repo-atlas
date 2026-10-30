# hi-paris/XPER

⭐ 21 · Python · NOASSERTION · 推送 2026-06-02 · [GitHub](https://github.com/hi-paris/XPER) · [官网](https://hi-paris.github.io/XPER/) · 组织维护

**度量各输入特征对模型预测性能贡献的 Python 解释性库**

基于 Shapley 值的方法论与 Python 库，用于将任一计量经济学或机器学习模型的预测性能（如 AUC、R²）分解到各输入特征上；与聚焦模型预测值的 SHAP 不同，XPER 聚焦性能指标本身，且 SHAP 为其特例。提供 bar/beeswarm/force 可视化，超过 10 个特征变量时建议启用 kernel=True 以保证计算效率。在 Linux/macOS/Windows 测试通过，经 pip 安装，附 Colab 示例（贷款分类、波士顿房价回归）。由 HEC Paris 研究者团队开发，配有 SSRN/arXiv 论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Shapley 值将模型性能（AUC/R²）分解到各输入特征
- 标准 SHAP 方法为 XPER 的特例
- bar/beeswarm/force 三种可视化图表
- kernel=True 选项用于超过 10 个特征时的高效计算

## 适用场景

- 分析信用评分模型中哪些特征驱动 AUC 表现
- 解释回归模型中各变量对 R² 的贡献
- 模型开发中比较特征重要性以辅助特征筛选

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L7: **XPER (eXplainable PERformance)** is a methodology designed to measure the specific contribution of the input featu
> L126: Hué, Sullivan, Hurlin, Christophe, Pérignon, Christophe and Saurin, Sébastien. "Measuring the Driving Forces of Pr

## 星数曲线

```mermaid
xychart-beta
    title "hi-paris/XPER 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `1434bad05882` · [字段定义](../../DATASET.md)*
