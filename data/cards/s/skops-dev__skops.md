# skops-dev/skops

⭐ 530 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/skops-dev/skops) · [官网](https://skops.readthedocs.io/en/stable/) · 组织维护

**帮助共享与部署 scikit-learn 模型的 Python 库**

面向使用 scikit-learn 的开发者与 MLOps 场景：提供 skops.io 模块以不依赖 pickle 的方式持久化 sklearn 估计器，并声明具备安全性；提供 skops.card 模块生成模型卡片，说明模型用途与使用方式。以 Python 库形式发布，通过 pip 安装，附有文档、用户指南与完整示例，在 Linux/macOS/Windows 上运行测试。

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

- skops.io：不使用 pickle 的 sklearn 估计器持久化
- skops.card：生成解释模型用途与用法的模型卡片
- 提供文档、用户指南与完整示例

## 适用场景

- 以非 pickle 格式安全保存与分发 sklearn 模型
- 为训练好的模型生成模型卡片随模型发布
- 将 sklearn 模型投入生产流程时管理工件

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L31: ``skops`` is a Python library helping you share your `scikit-learn
> L33: At the moment, it includes `skops.io` to securely persist sklearn estimators and
> L34: more, without using ``pickle``. It also includes `skops.card` to create a model

## 星数曲线

```mermaid
xychart-beta
    title "skops-dev/skops 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 528 --> 530
    line [529, 529]
```

2026-10-18 529 → 2026-10-24 529（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `ac1839fd115b` · [字段定义](../../DATASET.md)*
