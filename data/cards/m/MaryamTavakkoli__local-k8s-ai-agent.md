# MaryamTavakkoli/local-k8s-ai-agent

⭐ 21 · HTML · 推送 2026-05-27 · [GitHub](https://github.com/MaryamTavakkoli/local-k8s-ai-agent) · 个人维护

**自托管 K8s 只读 AI 诊断 Agent：本地 LLM 读实时集群状态**

部署在 Kubernetes 上的自托管 AI agent，面向 DevOps 与平台工程师：通过只读 ServiceAccount 读取实时 pods、events 与 logs，结合本地 Mistral 7B（经 Ollama 运行）对集群实际状态做推理诊断，RAG 模式下回答附带所读集群上下文。提供浏览器 Chat UI 与 FastAPI REST 端点（/ask、/diagnose、/docs）。部署链路为 GitHub Actions 多架构构建 + ArgoCD Image Updater + ArgoCD 同步的 GitOps 流程；安装步骤较长，需 minikube、Helm、ArgoCD 等全套本地环境，CPU 上响应需 1-2 分钟。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 只读 RBAC ServiceAccount，仅 get/list 权限，agent 只能观察不能修改集群
- 本地 Mistral 7B 经 Ollama 运行，无 API key，数据不出集群
- Diagnose 模式读取实时 pods/events/logs 并附上所读上下文供核验
- GitHub Actions + ArgoCD Image Updater 全 GitOps 自动化部署

## 适用场景

- 诊断自己集群命名空间里 pod 重启、错误事件等实际状态
- 通过对话 UI 或 REST API 询问 Kubernetes 运维问题
- 学习 AI agent 在 K8s 上的概念与 GitOps 部署模式

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L5: The agent doesn't just answer generic Kubernetes questions - it **reads your live pods, events, and logs** and reaso
> L9: - **Local LLM** - Mistral 7B via Ollama, on your hardware, no API keys, no data leaves your cluster
> L28:  - `Diagnose Cluster` - the agent reads live pods, events, and logs from your namespace and reasons about the actua

## 星数曲线

```mermaid
xychart-beta
    title "MaryamTavakkoli/local-k8s-ai-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `fb106a7221c7` · [字段定义](../../DATASET.md)*
