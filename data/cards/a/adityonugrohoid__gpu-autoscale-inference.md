# adityonugrohoid/gpu-autoscale-inference

⭐ 32 · Shell · MIT · 推送 2026-10-07 · [GitHub](https://github.com/adityonugrohoid/gpu-autoscale-inference) · 个人维护

**给平台工程师：Kubernetes 上缩容到零的 GPU LLM 推理平台**

在 GKE 上运行 LLM 推理的 Kubernetes 平台：FastAPI 网关将请求写入 Redis 队列并立即返回 job_id，KEDA 按队列深度把 worker 与 vLLM Deployment 从 0 扩到 N，待调度的 vLLM Pod 的 GPU 资源请求触发 Cluster Autoscaler 拉起 GPU 节点，空闲时两层均缩回 0 以消除闲置成本。vLLM 以 continuous batching 提供推理。冷启动为已知代价：T4 Spot 上从约 11 分钟经 PVC 存权重与 GKE Secondary Boot Disk 预缓存镜像降至约 5.6 分钟。含 DCGM/vLLM 等 4 类 exporter 喂 12 面板 Grafana 看板与完整周期验证脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双层缩容到零：KEDA 按 Redis 队列深度扩 Pod，Cluster Autoscaler 按待调度 Pod 扩 GPU 节点
- Redis 队列缓冲冷启动期间的请求突发，无丢弃流量
- 冷启动优化：模型权重放 PVC + GKE Secondary Boot Disk 预缓存容器镜像，约 11 分钟降至约 5.6 分钟
- 四类 Prometheus exporter 与 12 面板 Grafana 看板，附全周期事件日志采集脚本

## 适用场景

- 在 Kubernetes 上低成本运行间歇性 LLM 推理负载，空闲时 GPU 费用归零
- 搭建带完整扩缩容链路与 GPU 可观测性的推理平台参考实现
- 验证和分析 scale-to-zero 场景下的冷启动瓶颈

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L7: **Scale-to-zero GPU inference platform: LLM serving on Kubernetes with KEDA pod autoscaling and Cluster Autoscaler n
> L15: An LLM inference platform whose core design decision is two independent autoscaling layers: KEDA scales pods on Red

## 星数曲线

```mermaid
xychart-beta
    title "adityonugrohoid/gpu-autoscale-inference 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 30 --> 33
    line [31, 32]
```

2026-10-18 31 → 2026-10-29 32（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `c5b40e264c43` · [字段定义](../../DATASET.md)*
