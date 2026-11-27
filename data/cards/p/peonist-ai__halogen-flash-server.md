# peonist-ai/halogen-flash-server

⭐ 1,473 · Shell · NOASSERTION · 推送 2026-11-26 · [GitHub](https://github.com/peonist-ai/halogen-flash-server) · [官网](https://peonist.ai/halogen/) · 组织维护

**在 AMD Strix Halo 上以 OpenAI/Anthropic API 本地运行 Qwen3.8 的推理服务器**

针对 AMD Strix Halo 单一 GPU 与 Qwen3.8 模型族逐内核编写的本地推理服务器，不使用通用运行时；以容器镜像分发，在同一端口暴露 OpenAI 兼容与 Anthropic Messages API，面向编码 agent 的长会话场景。支持 Qwen3.8-27B 与 Flash-Next 共用镜像、直接读取 llama.cpp GGUF 文件、NPU 小模型，并提供投机解码的字节级贪心一致性保证。仅能在该 GPU 上运行；镜像须在 BIOS 中设置 UMA carve-out。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一端口提供 OpenAI 兼容 API 与 Anthropic Messages API
- 直接读取 llama.cpp GGUF 文件，无需转换步骤
- 支持 Qwen3.8-27B、图像输入与 LoRA 适配器，以及 NPU 小模型
- 投机解码在每个发布版本验证，输出与串行贪心解码字节一致

## 适用场景

- 在 Strix Halo 机器上本地部署编码 agent 的推理后端
- 用 OpenAI 或 Anthropic 客户端接入本地长上下文模型
- 直接加载已有的 GGUF 权重文件运行

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L9: Every kernel is written for this one GPU and this one model family. No
> L89: |Clients|Codex (Responses API) · Claude Code (Messages API) · agent harnesses · sessions: keep, fork, join|
> L102: podman run --rm -p 8731:8731 \

## 星数曲线

```mermaid
xychart-beta
    title "peonist-ai/halogen-flash-server 星数(近 27 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 1046 --> 1511
    line [1084, 1099, 1111, 1123, 1131, 1137, 1144, 1161, 1175, 1084, 1262, 1286, 1306, 1316, 1328, 1346, 1355, 1364, 1382, 1390, 1398, 1407, 1412, 1417, 1424, 1461, 1473]
```

2026-10-25 1,084 → 2026-11-27 1,473（+389）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `061655c6fd5a` · [字段定义](../../DATASET.md)*
