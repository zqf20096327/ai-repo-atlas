# albond/DenseSpark-Qwen3.8-27B

⭐ 16 · Python · MIT · 推送 2026-09-01 · [GitHub](https://github.com/albond/DenseSpark-Qwen3.8-27B) · 个人维护

**在单台 DGX Spark 上高速运行 Qwen3.8-27B 的一键推理服务包**

面向 DGX Spark（或兼容 GB10 机器）用户的 Qwen3.8-27B 本地推理部署方案：一条 install.sh 命令完成安装，启动 OpenAI 兼容 API 服务（端口 8000），支持自动工具调用。关键机制为 INT4 AutoRound 量化、投机解码（按并发档位选草稿深度）与针对 GB10 SM121 架构重编译的 vLLM 算子；官方发布质量门（mean-NLL delta 阈值 0.005）与基准复现协议。限制：需要约 60 GB 磁盘，默认仅监听 loopback 且无鉴权，首 token 延迟高于 stock 配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- install.sh 一键安装并启动 OpenAI 兼容 API 服务（端口 8000）
- INT4 AutoRound 量化 + 投机解码 + GB10 SM121 定制编译算子
- 按预期并发自动调优投机解码草稿深度（1/2/3+ 档位）
- 量化与算子改动以 mean-NLL delta 质量门验证，未达标路径不发布

## 适用场景

- 在自家 DGX Spark 上快速跑起 Qwen3.8-27B 的推理服务
- 用现有 OpenAI 客户端/聊天 UI 接入局域网内的本地模型
- 为团队或应用提供单机 16 并发内的本地 LLM 服务

## 场景标签

`推理引擎` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L85: That is the whole thing. It serves an OpenAI-compatible API on port 8000, so
> L69: Tool calling works out of the box: the server is started with vLLM's automatic

## 星数曲线

```mermaid
xychart-beta
    title "albond/DenseSpark-Qwen3.8-27B 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `dcfdd27476c5` · [字段定义](../../DATASET.md)*
