# scimorph/secureml

⭐ 37 · Python · MIT · 推送 2026-04-11 · [GitHub](https://github.com/scimorph/secureml) · [官网](https://secureml.readthedocs.io) · 组织维护

**面向开发者的隐私保护 AI Python 工具库：匿名化、差分隐私与合规检查**

SecureML 是一个开源 Python 库，与 TensorFlow 和 PyTorch 集成，为开发者提供隐私保护机器学习工具：数据匿名化（K-匿名、假名化、数据脱敏）、差分隐私训练（经 Opacus 与 TF Privacy）、基于 Flower 的联邦学习与安全聚合、合成数据生成（统计建模、GAN、Copula 及 SDV 集成）。内置 GDPR、CCPA、HIPAA、LGPD 预设用于合规检查，并提供审计日志、函数级审计装饰器与 HTML/PDF 合规报告。需要 Python 3.11-3.12，通过 pip 安装。

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

- K-匿名、假名化、数据脱敏与自动敏感数据检测等匿名化工具
- 差分隐私训练集成 PyTorch（Opacus）与 TensorFlow（TF Privacy）
- GDPR/CCPA/HIPAA/LGPD 四种法规预设与合规检查器
- 审计日志、HTML/PDF 自动化合规报告与可视化仪表盘

## 适用场景

- 对含个人敏感信息的数据集做匿名化后再用于训练
- 用差分隐私或联邦学习方式训练模型以满足合规要求
- 生成保持统计特性的合成数据替代真实数据
- 检查数据集与模型配置是否存在隐私合规风险并生成报告

## 场景标签

 · 领域:隐私保护机器学习/合规工具

## 证据(README 行号)

> L11: SecureML is an open-source Python library that integrates with popular machine learning frameworks like TensorFlow 
> L22:  - Differential privacy integration with PyTorch (via Opacus) and TensorFlow (via TF Privacy)

## 星数曲线

```mermaid
xychart-beta
    title "scimorph/secureml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-28 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1fbae25a6f2d` · [字段定义](../../DATASET.md)*
