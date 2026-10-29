# ur-grue/toptop

⭐ 19 · Rust · GPL-3.0 · 推送 2026-09-21 · [GitHub](https://github.com/ur-grue/toptop) · [官网](https://github.com/ur-grue/toptop#readme) · 个人维护

**终端本地推理观测与系统监视器（htop/btop 级）**

Rust 编写的单二进制终端系统监视器，同时提供本地 LLM 推理观测视图：显示 compute 与 memory-bandwidth 利用率对比、按进程 VRAM、tokens/sec、KV-cache 压力、队列深度与 TTFT/TPOT 分位数，并在 VRAM 溢出、GPU 降频等阈值前发出告警。自动发现 vLLM、llama.cpp、Ollama、TGI、TensorRT-LLM、LM Studio 等推理服务并抓取其指标，支持 JSON/Prometheus 导出与 SSH 多主机 fleet 视图。面向本地推理与 LLMOps 的运维/诊断用户，约 1MB 二进制、零运行时依赖，通过一键脚本、Homebrew、.deb 或源码安装，含 --demo 无 GPU 演示模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 视图：compute vs memory-bandwidth 对比、VRAM 溢出预警、降频原因读取
- 自动发现 vLLM/llama.cpp/Ollama/TGI 等服务并抓取 tokens/sec、KV-cache、TTFT
- 内置 Prometheus exporter（--serve-metrics）与 Grafana 面板
- --remote SSH 多主机 fleet 聚合视图与 --diagnose 瓶颈诊断输出

## 适用场景

- 排查本地 LLM 推理为何慢（带宽受限/VRAM 溢出/降频）
- 用 Grafana/Prometheus 持续监控推理集群的 tokens/sec 与告警
- 作为 htop/btop 替代的日常终端系统监视器

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L73: > **auto‑discovers your inference servers** (vLLM · llama.cpp · Ollama · TGI · TensorRT‑LLM · LM Studio) to scrape 
> L113: |🔭 **Server auto‑discovery**|finds listening vLLM / llama.cpp / Ollama / TGI / TensorRT‑LLM / LM Studio and scrape
> L141: Press **`a`** (or launch with **`--ai`**) for a view built around the question

## 星数曲线

```mermaid
xychart-beta
    title "ur-grue/toptop 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-29 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `961e1ce3d36a` · [字段定义](../../DATASET.md)*
