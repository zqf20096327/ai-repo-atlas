# GoogleCloudPlatform/ml-testing-accelerators

⭐ 64 · Jsonnet · Apache-2.0 · 推送 2026-07-22 · [GitHub](https://github.com/GoogleCloudPlatform/ml-testing-accelerators) · 组织维护

**在 GCP TPU/GPU 上运行深度学习模型测试的工具集**

GoogleCloudPlatform 下的测试框架，提供在 Google Cloud 硬件加速器（TPU/GPU）上运行 TensorFlow 与 PyTorch 模型测试的工具和示例。工作方式为：测试在 GKE 中按计划自动运行，结果由 Metrics Handler 收集并写入 BigQuery；部署涉及 Kubernetes 集群、Docker 测试镜像、Cloud Functions 上的指标处理器、事件发布器，并提供 JSonnet 模板库生成测试配置。README 声明本仓库正在弃用，要求迁移到新仓库；且声明非 Google 官方支持产品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 测试在 GKE 中按计划自动运行
- Metrics Handler 收集结果并写入 BigQuery
- JSonnet 模板库生成测试配置文件
- 支持 TPU 与 GPU 硬件加速器上的 TensorFlow/PyTorch 测试

## 适用场景

- 在云端 TPU/GPU 上按计划自动运行模型测试
- 将模型测试结果汇总到 BigQuery 并可选配置仪表盘查看

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: A set of tools and examples to run machine learning tests on ML hardware
> L12: In this mode, your tests and/or models run on an automated schedule in GKE.

## 星数曲线

```mermaid
xychart-beta
    title "GoogleCloudPlatform/ml-testing-accelerators 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 63 --> 65
    line [64, 64]
```

2026-10-18 64 → 2026-10-25 64（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `bffe4210db68` · [字段定义](../../DATASET.md)*
