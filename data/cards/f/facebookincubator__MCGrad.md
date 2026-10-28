# facebookincubator/MCGrad

⭐ 52 · Jupyter Notebook · MIT · 推送 2026-10-16 · [GitHub](https://github.com/facebookincubator/MCGrad) · [官网](https://mcgrad.dev) · 组织维护

**面向 ML 从业者的多校准库：修正模型在各子群体上的概率校准偏差**

Python 多校准（multicalibration）工具库：在全局校准之外，自动识别并修正模型预测在特征定义的各子群体（如国家、内容类型及其组合）上的系统性过自信/欠自信，无需手工指定受保护群体。采用似然改进的更新与基于验证集的早停，README 称已在 Meta 数百个生产模型上部署。提供 pip/conda 安装、NumPy/Pandas 风格接口与 Colab 交互式笔记本，要求 Python 3.10+，附 KDD 2026 论文。

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

- 按特征定义的任意子群体修正概率校准偏差
- 无需手动指定受保护群体即可发现隐藏校准缺口
- 似然改进更新与验证集早停机制
- 含 LLM 输出置信度校准的示例笔记本

## 适用场景

- 上线前修正分类/预测模型在细分人群上的置信度偏差
- 对 LLM 输出的置信度分数做多校准
- 替代仅做全局校准的后处理流程

## 场景标签

 · 领域:机器学习工具/模型校准

## 证据(README 行号)

> L18: **MCGrad** is a scalable and easy-to-use tool for **multicalibration**. It ensures your ML model predictions are we
> L39: MCGrad has been deployed at **Meta** on hundreds of production models. See the research paper for detailed experime

## 星数曲线

```mermaid
xychart-beta
    title "facebookincubator/MCGrad 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-28 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `cfc4fc127afe` · [字段定义](../../DATASET.md)*
