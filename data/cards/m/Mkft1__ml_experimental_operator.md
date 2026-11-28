# Mkft1/ml_experimental_operator

⭐ 3 · Go · 推送 2026-10-17 · [GitHub](https://github.com/Mkft1/ml_experimental_operator) · 个人维护

**Kubernetes Operator：自动化 ML 超参数搜索实验**

用 Go 编写的 Kubernetes Operator，通过两个自定义资源（Experiment/Trial）管理超参数搜索实验：Experiment 定义参数空间与资源限制，每个 Trial 对应一个 Job。支持网格搜索与随机搜索两种策略，控制器从 Job stdout 的最后一行 JSON 读取指标。基于 kubebuilder 构建，含 CEL 校验、RBAC 与部署清单。README 明确列出多项限制：EarlyStopping 未实际生效、无 admission webhook、PVC 需预先存在、不支持 autoscaling 与 seed 多次运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Experiment/Trial 两个 CRD，Trial 与 Kubernetes Job 一一对应
- 内置 GridSearch（笛卡尔积）与 RandomSearch（Fisher–Yates）策略
- 按约定从 Job stdout 末行 JSON 读取训练指标
- CRD 含 kubebuilder 校验与 CEL 规则

## 适用场景

- 在 Kubernetes 集群中批量跑超参数搜索实验
- 为团队搭建声明式 ML 实验管理流程

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L3: Kubernetes Operator на Go для запуска экспериментов по подбору
> L24: * `internal/search` — стратегии `GridSearch` (декартово произведение) и `RandomSearch` (Fisher–Yates).
> L29: Предпосылки: Go >= 1.19, docker, kubectl, кластер Kubernetes >= 1.25

## 星数曲线

```mermaid
xychart-beta
    title "Mkft1/ml_experimental_operator 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-26 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `cfe4422bf88e` · [字段定义](../../DATASET.md)*
