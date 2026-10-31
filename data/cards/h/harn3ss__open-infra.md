# harn3ss/open-infra

⭐ 14 · Go · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/harn3ss/open-infra) · 个人维护

**自托管 AWS 兼容云平台：用自有硬件运行 25+ AWS 风格服务**

部署在自有 Linux 硬件上的云平台，在 Kubernetes/GitOps（k3s + Argo CD + Crossplane）之上提供 AWS 形态的服务面：S3（MinIO）、RDS（CloudNativePG/Babelfish）、DynamoDB（FerretDB）、Lambda（Knative）、EC2 式 VM（KubeVirt）、Step Functions、IAM 等 25+ 映射，另含 Bedrock/SageMaker 对应的 GPU 推理与训练（Ollama、GPU batch Job，多项标注 experimental）。三种使用面：infra.yaml/GitOps、Web 控制台、Terraform provider；可选 AWS-SDK shim 以 SigV4 应答未修改的 AWS CLI/SDK。未覆盖的 AWS 服务返回 501。面向无法采用超大规模云的学校、医院、地方政府等。非 AI 基础设施本身，AI 推理是其中功能之一。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- AWS wire protocol shim：SigV4 认证、真实后端、兼容探针验证
- infra.yaml 声明意图，GitOps 自动协调，无需手写 Kubernetes
- 25+ AWS 服务概念映射（S3/RDS/DynamoDB/Lambda/Step Functions/IAM 等）
- GPU 推理与训练：Ollama 后端 kind:Model、SageMaker 系列（多项 experimental）

## 适用场景

- 在学校/医院/政府等自有硬件上运行 AWS 形态的私有云
- 让现有 AWS CLI/SDK/Terraform/CloudFormation 工具不改代码接入自有基础设施
- 在自有 GPU 节点上运行托管式模型推理（Ollama 后端）

## 场景标签

 · 领域:云计算/基础设施

## 证据(README 行号)

> L7: > A **self-hosted cloud that speaks AWS**, running entirely inside your own trust boundary.
> L93: |Bedrock|managed inference (`kind: Model`)|Ollama on GPU + NVIDIA device plugin|
> L48: **Who it's for.** Organisations that need cloud-style infrastructure but can't justify — or safely

## 星数曲线

```mermaid
xychart-beta
    title "harn3ss/open-infra 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `99bea7d46104` · [字段定义](../../DATASET.md)*
