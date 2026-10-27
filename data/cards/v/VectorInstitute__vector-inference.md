# VectorInstitute/vector-inference

⭐ 110 · Python · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/VectorInstitute/vector-inference) · [官网](https://vectorinstitute.github.io/vector-inference/) · 组织维护

**在 Slurm 集群上部署 LLM 推理服务的工具**

由 Vector Institute 维护的推理部署工具：以 Slurm 作业形式启动基于 vLLM 或 SGLang 的 OpenAI 兼容推理服务器，暴露 URL 端点供请求。提供 CLI（launch/batch-launch/status/metrics/shutdown 等命令）与 Python API 两种接口，动态生成 Slurm 脚本并保存启动配置用于复现。原生适配 Vector 集群环境，其他 Slurm 集群需修改 environment.yaml 与 models.yaml 配置或使用提供的 Dockerfile 构建镜像。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 Slurm 作业部署 vLLM/SGLang 推理服务器，OpenAI 兼容端点
- CLI 与 Python API 双接口，支持批量启动、状态查询、指标流式输出
- 动态生成 Slurm 脚本并留存启动配置 JSON 用于复现
- 提供 vllm/sglang Dockerfile，镜像发布至 Google Artifact Registry

## 适用场景

- 在 Slurm 管理的 HPC 集群上部署 LLM/VLM 推理服务
- 批量管理多个模型推理服务器并监控状态与指标
- 通过 SSH 隧道从本地设备访问集群上的推理端点

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L12: This repository provides an easy-to-use solution to run inference servers on Slurm-managed computing clusters using
> L44: The `launch` command allows users to deploy a model as a slurm job. If the job successfully launches, a URL endpoin

## 星数曲线

```mermaid
xychart-beta
    title "VectorInstitute/vector-inference 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 109 --> 111
    line [110, 110]
```

2026-10-18 110 → 2026-10-27 110（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `7c8cd670f961` · [字段定义](../../DATASET.md)*
