# niklasfrick/spark-dashboard

⭐ 139 · TypeScript · MIT · 推送 2026-10-17 · [GitHub](https://github.com/niklasfrick/spark-dashboard) · 个人维护

**Linux+NVIDIA 主机的硬件与 LLM 推理实时监控仪表盘**

Rust 后端通过 NVML、sysinfo、procfs 采集 GPU/CPU/内存/磁盘/网络指标，并经 Prometheus 指标读取 vLLM、SGLang、llama.cpp 引擎统计（Ollama 仅显示状态与已加载模型），经 WebSocket 推送到 React 前端。面板可自由拖拽布局、按引擎/GPU 绑定，支持多引擎并排监控与墙面展示轮播。面向运行 NVIDIA GPU Linux 主机的开发与运维人员；需 NVIDIA 驱动，Ollama 无指标面板，两种安装路径均从源码编译。

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

- 1 秒级采集 GPU 利用率/温度/功耗及热节流等事件检测
- vLLM/SGLang/llama.cpp 引擎指标：TPS、TTFT、KV cache、SLO Goodput 等
- 通过进程扫描与 Docker API 自动发现引擎，含容器内引擎
- 面板可编辑布局、命名页面各带 URL，保存于服务端

## 适用场景

- 监控推理服务器的 GPU 与 vLLM/SGLang 引擎运行状态
- 多引擎并排观察 tokens/s 与延迟指标
- 为机房墙面显示屏配置轮播监控页面

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: Real-time hardware and LLM inference monitoring for Linux systems with NVIDIA
> L6: A Rust backend collects GPU, CPU, memory, disk, and network metrics alongside
> L83: **LLM Engine Monitoring** (vLLM, SGLang and llama.cpp via Prometheus metrics)

## 星数曲线

```mermaid
xychart-beta
    title "niklasfrick/spark-dashboard 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-25"]
    y-axis "stars" 135 --> 140
    line [136, 138, 139]
```

2026-10-18 136 → 2026-10-25 139（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `7b875fce9f35` · [字段定义](../../DATASET.md)*
