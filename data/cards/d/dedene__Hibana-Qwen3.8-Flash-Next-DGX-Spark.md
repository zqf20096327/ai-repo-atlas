# dedene/Hibana-Qwen3.8-Flash-Next-DGX-Spark

⭐ 3 · Python · MIT · 推送 2026-11-16 · [GitHub](https://github.com/dedene/Hibana-Qwen3.8-Flash-Next-DGX-Spark) · 个人维护

**在单台 DGX Spark 上用 Docker Compose 部署 Qwen3.8-Flash-Next 推理服务的方案**

一套部署配方（recipe）：在 DGX Spark（GB10）上以 Docker Compose 启动 Hibana 推理引擎，加载 125B MoE 的 NVFP4 检查点及 3-bit 副本，在 8888 端口提供 OpenAI 与 Anthropic 兼容 API，仅支持文本输出。提供 exact/fast/throughput 三种配置档，带工具调用 anyOf 问题的补丁、自检脚本、前缀缓存 SSD 层与内存保护等环境变量配置，并附速度测量与 AgentDojo/BFCL 等 agent 基准结果。面向持有 DGX Spark 并希望本地自托管该模型的用户。

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

- 一条命令完成镜像构建、检查点下载与服务启动（约 186 GB 下载）
- 提供 OpenAI/Anthropic 兼容 API，支持 thinking 开关、流式与工具调用
- exact/fast/throughput 三档 profile 与 MTP/DFlash2 投机解码可选
- 附 Inspect/AgentDojo/BFCL agent 基准与速度对比数据

## 适用场景

- 在 DGX Spark 上本地自托管 Qwen3.8-Flash-Next 并对外提供 API
- 以 agent 后端形式接入本地大模型并评估其任务完成表现
- 按吞吐或精确度需求切换量化 profile

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: Serves Qwen3.8-Flash-Next with
> L12: **Hardware:** DGX Spark (GB10, sm_121, aarch64), driver 580, CUDA 13, Docker with the NVIDIA Container Toolkit,
> L20: docker compose up -d --wait   # first run: ~15 min image build, 186 GB download, ~3 min kernel builds


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `7ff3fece2bc3` · [字段定义](../../DATASET.md)*
