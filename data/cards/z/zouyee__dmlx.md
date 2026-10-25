# zouyee/dmlx

⭐ 61 · Zig · MIT · 推送 2026-09-07 · [GitHub](https://github.com/zouyee/dmlx) · 个人维护

**Apple Silicon 本地 LLM 推理引擎：48GB Mac 运行 284B MoE 模型**

用 Zig 编写、基于 MLX（mlx-c）的 Apple Silicon 本地推理引擎，通过 C/Metal 原生路径、MoE 专家 SSD 流式加载与有界热缓存（SMELT）在 48GB 内存的 Mac 上运行 DeepSeek V4 Flash 4-bit 等前沿 MoE 模型；README 报告 M4 Pro 48GB 上 1.236 tok/s 短跑中位吞吐。支持 9 种架构、6 种 KV 缓存策略、OpenAI/Anthropic 兼容 HTTP 服务、投机解码、QLoRA 微调与视觉模型。需 macOS Apple Silicon、Zig 0.16.0 与 mlx-c，从源码 make 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MoE 专家流式加载 + 有界 SMELT 热缓存：284B 模型在 48GB 内存内运行
- 9 种模型架构、6 种运行时可切换 KV 缓存策略（最长 128K+ 上下文）
- OpenAI + Anthropic API 兼容 HTTP 服务（SSE 流式）
- 投机解码（PLD+EAGLE）、JSON Schema/Regex 引导解码、QLoRA 微调、LLaVA 视觉

## 适用场景

- 在无云无 GPU 集群的前提下于 MacBook 本地运行前沿 MoE 模型
- Mac mini 作为团队自建推理服务器（OpenAI API 兼容接入）
- 满足 HIPAA/GDPR 场景的离线数据不出机推理
- 研究者修改 MoE 路由、切换 KV 策略、测试量化格式

## 场景标签

`推理引擎` `微调` · 领域:训练与推理

## 证据(README 行号)

> L7: dmlx runs frontier Mixture-of-Experts models on Apple Silicon through a native C/Metal inference path with packed ex
> L117: - OpenAI + Anthropic API compatible HTTP server (SSE streaming)
> L129: **Requirements**: macOS Apple Silicon (M1-M4) + Zig 0.16.0 + mlx-c

## 星数曲线

```mermaid
xychart-beta
    title "zouyee/dmlx 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-25 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `fc811714423e` · [字段定义](../../DATASET.md)*
