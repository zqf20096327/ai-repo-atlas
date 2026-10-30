# hequan2017/docker-gpu-manage

⭐ 16 · Go · Apache-2.0 · 推送 2026-09-28 · [GitHub](https://github.com/hequan2017/docker-gpu-manage) · 个人维护 · 中文 README

**企业级 Docker GPU 算力资源管理平台：纳管节点、创建与回收 GPU 容器**

基于 Gin-Vue-Admin 前后端分离架构的平台，把 GPU 服务器通过 Docker API（支持 TLS）注册为算力节点，按产品规格（GPU/显存/CPU/内存/磁盘）一键创建容器实例，覆盖创建、连接、监控、回收全生命周期；配套 SSH 跳板机、Web 终端、端口转发与资源监控。同时内置 Kubernetes 多集群管理、PCDN 节点纳管、服务器/戴尔资产管理，以及 AI Agent（智谱 GLM）、模型微调任务管理、MCP 服务等扩展模块。支持本地开发、Docker Compose 与 Kubernetes 三种部署方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Docker API 远程纳管多 GPU 节点，TLS 安全连接，智能主机匹配
- HAMi 显存切分：自动注入 LD_PRELOAD 与 CUDA 限制环境变量
- Kubernetes 多集群管理（kubeconfig AES-256-GCM 加密）与三级 RBAC
- AI Agent（智谱 GLM）与 LLaMA 等模型微调任务管理

## 适用场景

- AI/ML 团队统一管理分散的 GPU 服务器并按规格创建训练推理容器
- 科研机构或高校搭建算力池与教学实验环境
- 运维团队纳管 Kubernetes 多集群与服务器资产

## 场景标签

 · 领域:基础设施/GPU 算力管理

## 证据(README 行号)

> L5: 企业级 Docker GPU 算力资源管理平台：把分散的 GPU 服务器纳管为算力节点，按规格一键创建 GPU 容器实例，覆盖创建、连接、监控、回收的全生命周期。
> L17: 本平台基于 Gin-Vue-Admin 脚手架构建，采用前后端分离架构，把 GPU 服务器注册为算力节点（通过 Docker API 远程连接，支持 TLS），将镜像库、产品规格、算力节点组合创建容器实例，并提供 SSH 跳板机、

## 星数曲线

```mermaid
xychart-beta
    title "hequan2017/docker-gpu-manage 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ffa19ef6dd1d` · [字段定义](../../DATASET.md)*
