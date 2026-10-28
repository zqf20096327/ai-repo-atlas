# rstudio/vetiver-python

⭐ 71 · Python · MIT · 推送 2026-07-01 · [GitHub](https://github.com/rstudio/vetiver-python) · [官网](https://rstudio.github.io/vetiver-python/stable/) · 组织维护

**训练模型的版本化、部署与监控工具库（MLOps）**

面向数据科学开发者的 Python MLOps 库：以 VetiverModel 对象封装训练好的模型，记录并检查输入数据原型，通过 pins 板（本地文件夹、Connect、S3 等）做版本化与共享，并用基于 FastAPI 扩展的 VetiverAPI 部署为 API 端点，支持从远端端点预测与监控。通过泛型机制可扩展支持 scikit-learn、torch、statsmodels、xgboost、spacy 等多种模型，另有对应的 R 版本。项目自标为 experimental 阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- VetiverModel 封装模型的存储、版本化与部署
- 基于 FastAPI 扩展的 VetiverAPI 部署端点，可检查输入数据原型
- 通过 pins 板（本地/Connect/S3）版本化共享模型
- 泛型可扩展支持 scikit-learn/torch/statsmodels/xgboost/spacy 等模型

## 适用场景

- 把训练好的模型版本化并共享给团队
- 将模型快速部署为可检查输入原型的 API 服务
- 监控远端 API 端点的模型预测

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L8: The goal of vetiver is to provide fluent tooling to version, share, deploy, and monitor a trained model. Functions h
> L59: You can **deploy** your pinned `VetiverModel()` using `VetiverAPI()`, an extension of FastAPI.

## 星数曲线

```mermaid
xychart-beta
    title "rstudio/vetiver-python 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 70 --> 72
    line [71, 71]
```

2026-10-18 71 → 2026-10-27 71（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `80e1b69ef512` · [字段定义](../../DATASET.md)*
