# Multicorewareinc/M-Stack

⭐ 22 · Python · Apache-2.0 · 推送 2026-09-22 · [GitHub](https://github.com/Multicorewareinc/M-Stack) · 组织维护

**在自有服务器上声明式搭建 K8s AI 推理平台的 Python SDK**

面向持有裸金属/虚拟机的开发者与团队，以声明式 spec（pydantic 模型）+ 后端执行的统一模式，把从 RKE2 集群、GPU 调度、Longhorn 存储、MinIO、vLLM/llama.cpp 模型服务到网关、限流、计费、Portal 等 18 项能力组合成完整 AI 推理平台。后端通过 shell 调用 ssh/helm/kubectl 而非客户端库；不负责置备裸金属与网络，要求节点间 L3/UDP 可达与免密 SSH，并需在首个控制面节点上运行。当前为 0.x 预发布版，发布于 TestPyPI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 18 项能力各为独立包，声明式 spec 组合、Stack 强制依赖顺序
- 推理后端可选 vLLM 或 llama.cpp，提供 OpenAI 兼容端点与网关
- SQLite 单文件状态记录（~/.multistack/state.db）跟踪部署与故障
- kubeconfig 显式传递，不读取环境中的 $KUBECONFIG

## 适用场景

- 在自有 GPU 服务器上从裸机搭建完整 LLM 服务栈
- 为团队搭建带认证、限流与用量计费的 OpenAI 兼容推理平台
- 以基础设施即代码方式管理 RKE2 + 存储 + 模型服务全链路

## 场景标签

`推理引擎` `MLOps` · 领域:训练与推理

## 证据(README 行号)

> L3: A declarative Python SDK for provisioning AI infrastructure. Every
> L149: |Inference|`examples/inference/serve.py`|Serves a model behind an OpenAI-compatible endpoint (vLLM or llama.cpp), 

## 星数曲线

```mermaid
xychart-beta
    title "Multicorewareinc/M-Stack 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-30 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `1d68af1c9a8d` · [字段定义](../../DATASET.md)*
