# uzunenes/triton-server-hpa

⭐ 16 · Python · MIT · 推送 2026-09-11 · [GitHub](https://github.com/uzunenes/triton-server-hpa) · 个人维护

**按 GPU 利用率在 Kubernetes 上自动扩缩 Triton 推理服务的部署方案**

一套端到端可复现的部署配置与指南：将 YOLOv7-tiny 导出 ONNX 并构建 TensorRT engine，由 Triton Inference Server 在 minikube/Kubernetes 上服务；通过 GPU 时间切片让多个 Triton Pod 共享单块物理 GPU，DCGM exporter 采集 GPU 利用率，经 Prometheus 与 Prometheus Adapter 暴露为自定义指标，HorizontalPodAutoscaler 据此增减副本。已在 RTX 4060 Ti + Ubuntu 22.04 环境验证（约 359 req/s 负载）。限制：需 NVIDIA GPU 与匹配驱动（575+），容器镜像约 40 GB 磁盘、约 16 GB 内存。

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

- 以 GPU 利用率（DCGM 指标）而非 CPU/内存驱动 HPA 扩缩
- 单物理 GPU 时间切片为 10 个可调度单元，多 Triton Pod 共享
- 完整指标链路：dcgm-exporter→Prometheus→prometheus-adapter→custom metrics API→HPA
- 在单卡机器（RTX 4060 Ti）上完成端到端验证并记录各组件版本

## 适用场景

- 在 Kubernetes 上部署随 GPU 负载自动扩缩的推理服务
- 在单 GPU 机器上演练多副本推理服务的弹性伸缩
- 参考 DCGM+Prometheus Adapter 接入 HPA 自定义指标的完整配置

## 场景标签

`推理引擎` `MLOps` · 领域:训练与推理

## 证据(README 行号)

> L9: Build an AI inference service that grows and shrinks with demand. A YOLOv7-tiny
> L15: Clients hit a Kubernetes service in front of a Triton deployment; DCGM exporter feeds GPU utilisation to Prometheus
> L366: `k8s/hpa-gpu.yaml` targets **30 % GPU utilisation** and

## 星数曲线

```mermaid
xychart-beta
    title "uzunenes/triton-server-hpa 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `140655c81c17` · [字段定义](../../DATASET.md)*
