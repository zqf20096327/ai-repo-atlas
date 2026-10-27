# bidual/awesome-dgx-spark

⭐ 91 · Shell · CC0-1.0 · 推送 2026-10-22 · [GitHub](https://github.com/bidual/awesome-dgx-spark) · 个人维护

**NVIDIA DGX Spark（GB10）社区工具与指南策展清单**

面向 NVIDIA DGX Spark（GB10 Grace Blackwell 个人 AI 超算）的 awesome 清单，收录社区项目链接，覆盖设备配置、模型推理服务（vLLM/SGLang/llama.cpp/Ollama 等引擎的项目）、微调、基准测试与日常运维；并注明平台要素：aarch64、CUDA 13.x、sm_121、128 GB 统一内存、200 Gb/s ConnectX-7 组网。条目按 Official、Setup & Configuration、Inference & Serving 等章节组织，每条附一句话描述。本仓库为链接索引，不提供可运行软件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | CC0-1.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按配置、推理服务、微调等主题组织的社区项目链接索引
- 标注 GB10 平台要素：aarch64 / CUDA 13.x / sm_121 / 128 GB 统一内存
- 收录双机 200 Gb/s 组网与多节点集群相关项目

## 适用场景

- 拿到 DGX Spark 后查找配置与系统安装指南
- 寻找在 GB10 上运行 vLLM、Ollama 等推理引擎的社区项目
- 了解 DGX Spark 生态中微调与基准测试工具的分布

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L1: # Awesome DGX Spark Awesome
> L3: > A curated list of awesome tools, guides, playbooks, and resources for the NVIDIA DGX Spark, the GB10 Grace Blackwe
> L5: DGX Spark is a desktop machine built on the GB10 Grace Blackwell Superchip (SM 12.1 / sm_121), with 128 GB of unifie

## 星数曲线

```mermaid
xychart-beta
    title "bidual/awesome-dgx-spark 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24", "2026-10-27"]
    y-axis "stars" 85 --> 92
    line [86, 88, 90, 91]
```

2026-10-18 86 → 2026-10-27 91（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `dd6e1b903a38` · [字段定义](../../DATASET.md)*
