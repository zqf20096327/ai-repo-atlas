# TrusteeML/trustee

⭐ 35 · Python · GPL-3.0 · 推送 2026-08-24 · [GitHub](https://github.com/TrusteeML/trustee) · 组织维护

**从黑盒 ML 模型中提取决策树解释的框架**

Python 包 trustee，用于从黑盒机器学习模型中提取决策树形式的解释，帮助审查（scrutinize）模型行为。支持 scikit-learn、Keras、TensorFlow、PyTorch、AutoGluon 等库训练的模型，提供 TrustReport 输出报告，examples/ 目录含使用示例。官方 Use Cases 覆盖入侵检测、网络流量异常检测、IoT 设备识别、自适应码率预测等场景，要求 Python >=3.11。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从黑盒模型提取决策树解释并生成 TrustReport
- 支持 scikit-learn/Keras/TensorFlow/PyTorch/AutoGluon 五类库
- 提供入侵检测、网络异常检测、IoT 识别等 8 个 Use Case

## 适用场景

- 解释和审查已训练黑盒模型的决策逻辑
- 对网络入侵检测或流量分类模型做可解释性分析
- 生成模型解释报告用于模型审查

## 场景标签

 · 领域:AI 可解释性/机器学习工具

## 证据(README 行号)

> L5: This package implements the `trustee` framework to extract decision tree explanation from black-box ML models.
> L42: For other examples and use cases of how Trustee can used to scrutinize ML models, listed in the table below, please

## 星数曲线

```mermaid
xychart-beta
    title "TrusteeML/trustee 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-25 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a3b038cafe2b` · [字段定义](../../DATASET.md)*
