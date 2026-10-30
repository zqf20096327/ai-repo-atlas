# bentoml/yatai-image-builder

⭐ 17 · Go · 推送 2026-10-23 · [GitHub](https://github.com/bentoml/yatai-image-builder) · 组织维护

**在 k8s 中为 Bento 构建 OCI 镜像的 Yatai 组件**

BentoML Yatai 生态的 Kubernetes 组件：作为 BentoRequest CRD 的 operator，监听并 reconcile 该 CR，为 Bento 构建容器镜像，构建完成后生成 Bento CR，供 yatai-deployment 组件在 k8s 中部署。遵循 Kubernetes Operator 模式，通过 make 工具链完成镜像构建、controller 部署与 CRD 安装/卸载。需要 Kubernetes 集群运行，面向使用 BentoML/Yatai 部署 ML 服务的平台开发或运维人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BentoRequest CRD 的 operator，reconcile 后为 Bento 构建镜像
- 构建完成生成 Bento CR，供 yatai-deployment 部署
- 遵循 Kubernetes Operator 模式，提供 make 部署/卸载工具链

## 适用场景

- 在 Yatai 平台中自动为 Bento 构建容器镜像
- 配合 yatai-deployment 实现 Bento 的 k8s 部署流水线
- 在 KIND 本地集群上测试镜像构建 controller

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L3: yatai-image-builder is a yatai component dedicated to building container images for Bento
> L7: yatai-image-builder runs in k8s, it is the operator of `BentoRequest` CRD, it is responsible for reconcile `BentoReq

## 星数曲线

```mermaid
xychart-beta
    title "bentoml/yatai-image-builder 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [18, 17, 17]
```

2026-10-18 18 → 2026-10-30 17（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `a17310da2ffc` · [字段定义](../../DATASET.md)*
