# Khanz9664/TrustLens

⭐ 16 · Python · MIT · 推送 2026-07-20 · [GitHub](https://github.com/Khanz9664/TrustLens) · [官网](https://pypi.org/project/trustlens) · 个人维护

**面向 ML 从业者的模型可靠性与公平性诊断评测库**

Python 库，用于在准确率之外审计机器学习模型：四个诊断引擎分别计算校准误差（ECE/Brier）、子组公平性差距（Equalized Odds）、潜空间可分性（Silhouette/CKA）与失败模式分布，合成 0–100 的 Trust Score 并输出 Ready/Blocked 部署判定。Prediction Resolver 自动检测并标准化 scikit-learn、XGBoost、LightGBM、CatBoost 等框架的模型输出，无需手写概率抽取代码。当前版本 v0.5，提供 quick_analyze 一行式内置数据集审计；回归信任分、深度学习后端与 CI/CD 集成在 v0.6/v1.0 规划中。通过 pip 安装。

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

- 四引擎诊断：校准、公平性、潜空间健康、失败分析
- 合成 0–100 Trust Score 与 Ready/Blocked 机器可读部署判定
- 原生支持 scikit-learn/XGBoost/LightGBM/CatBoost 的 Prediction Resolver
- quick_analyze 一行式内置数据集审计（如 breast_cancer）

## 适用场景

- 模型上线前检查过自信与子组公平性风险
- 在 CI/CD 流程中用部署判定拦截高风险模型
- 对 XGBoost/LightGBM 等已有模型做无样板代码的可靠性审计

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: ### Audit ML models beyond accuracy — calibration, fairness, latent health, and deployment verdicts.
> L85: TrustLens evaluates your model through four distinct diagnostic modules, combining the findings into a **Trust Scor

## 星数曲线

```mermaid
xychart-beta
    title "Khanz9664/TrustLens 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `34b9b2314e4b` · [字段定义](../../DATASET.md)*
