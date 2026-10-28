# hanxiao/Qwen3.6-35B-A3B-MTP-L4

⭐ 19 · Shell · 推送 2026-08-24 · [GitHub](https://github.com/hanxiao/Qwen3.6-35B-A3B-MTP-L4) · 个人维护

**在单张 L4 24GB 上部署 Qwen3.6-35B-A3B + MTP 投机解码的方案**

面向单张 NVIDIA L4 24 GB（GCP g2-standard-8）的 llama.cpp 部署配置仓库：使用 Unsloth Q4_K_XL GGUF 量化版 Qwen3.6-35B-A3B-MoE 模型，通过官方 llama.cpp Docker 镜像运行 MTP 投机解码服务。核心机制为两项无损优化：全 GPU 常驻（-ngl 99 --n-cpu-moe 0，约 +28%）与关闭 GDDR6 ECC（约 +10%），实测解码吞吐约 91–99 tok/s。提供一键 spot 实例开通脚本、预构建镜像、Web UI 与 Prometheus 指标；README 说明单 L4 无法让所有负载超过 100 tok/s。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 官方 llama.cpp Docker 镜像运行 Q4_K_XL 量化 MoE 模型 + MTP 投机解码
- 两项无损优化：全 GPU 专家常驻与关闭 ECC，合计约 +45% 吞吐
- provision-spot.sh 一键开通 GCP spot 实例并启动服务（含 Web UI 与 Prometheus）
- 可复现基准脚本 bench.sh，公开 MTP n-max 与参数扫描数据

## 适用场景

- 在单张 L4 上以受限显存运行 35B MoE 模型推理服务
- 通过 OpenAI 兼容接口（/v1/chat/completions）本地调用该模型
- 复现或参考 llama.cpp MTP 投机解码的调参与吞吐基准

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: Deploy Qwen3.6-35B-A3B (Unsloth **Q4_K_XL** GGUF) with MTP (Multi-Token Prediction) speculative decoding on a **sing
> L52: No source build needed — the official `ghcr.io/ggml-org/llama.cpp:server-cuda` image runs MTP out of the box with `

## 星数曲线

```mermaid
xychart-beta
    title "hanxiao/Qwen3.6-35B-A3B-MTP-L4 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `f0b61b37b990` · [字段定义](../../DATASET.md)*
