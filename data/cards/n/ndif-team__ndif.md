# ndif-team/ndif

⭐ 51 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/ndif-team/ndif) · 组织维护

**面向可解释性研究的远程模型推理服务端，运行 nnsight 干预实验**

NDIF（National Deep Inference Fabric）是 nnsight 客户端的服务器后端：接收用户提交的干预代码（hooks、捕获、编辑、生成），在共享 GPU 集群上对大模型执行，供本机硬件放不下模型的研究者远程运行实验。由 API（队列与结果流）、Ray actor（加载模型并执行 trace 块）、Redis/RustFS/Postgres 及遥测组件构成；提供单一 Docker 镜像、compose 开发栈与 PyPI 安装三条途径。默认无鉴权且未指定 tags 的请求被信任、代码在模型进程内执行；沙箱 actor 提供进程隔离但非安全边界，配置全部经 NDIF_* 环境变量。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在共享 GPU 集群上远程执行 nnsight 的干预/追踪代码
- 三种部署方式：单镜像 docker run、compose 开发栈（带 Grafana/Prometheus 遥测）、pip 安装 CLI
- 默认无鉴权部署，未指定 tags 的请求代码在模型进程内执行（有沙箱 actor 选项）
- 全部配置经 NDIF_* 环境变量，无配置文件

## 适用场景

- 研究者在本地放不下的大模型上做干预与内部机制实验
- 自建一套 nnsight 远程推理服务端供实验室共享 GPU 使用
- 通过 dashboard 查看 deploy/evict/status 与请求监控

## 场景标签

`推理引擎` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L7: **NDIF** is the server backend for **nnsight**. It runs
> L9: large models on a shared GPU cluster. Researchers point nnsight at an NDIF
> L125: |`api`|`localhost:8001`|Accepts nnsight requests, queues them, streams results back.|

## 星数曲线

```mermaid
xychart-beta
    title "ndif-team/ndif 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-24 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9ed0eb61a3dc` · [字段定义](../../DATASET.md)*
