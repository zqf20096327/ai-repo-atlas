# hec-ovi/vllm-awq4-qwen

⭐ 53 · Python · Unlicense · 推送 2026-05-10 · [GitHub](https://github.com/hec-ovi/vllm-awq4-qwen) · 组织维护

**在 AMD Strix Halo iGPU 上以 AWQ-INT4+DFlash 部署 Qwen 3.6-27B 的 vLLM 配置**

面向 AMD Strix Halo（gfx1151、128GB 统一内存）的 vLLM 推理部署仓库：将 Qwen 3.6-27B 以 AWQ-INT4 量化并启用 DFlash 投机解码，通过 Docker Compose 提供 OpenAI 兼容的 /v1/chat/completions、/v1/responses、/v1/completions 端点，支持视觉输入、工具调用与 256K 上下文。仓库内置针对 gfx1151 的自定义 HIP prefill 内核并逐项固定全部工具链版本。限制：每次启动冷启约 9 分钟；HIP graphs 在该 GPU 上会冻结需关闭；长上下文解码速率下降；工具调用仅两条推荐路径可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Unlicense |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AWQ-INT4 量化 + DFlash 投机解码（N=1/4/8），单流峰值 24.8 t/s
- 自定义 HIP prefill 内核，0-32K 上下文下 prefill 保持 105-134 t/s
- OpenAI 兼容端点，支持视觉输入、工具调用与 256K 上下文
- 全工具链版本逐项固定，Docker Compose 一键构建运行

## 适用场景

- 在 AMD Strix Halo 集成显卡本机上运行 27B 多模态模型服务
- 搭建本地 OpenAI 兼容推理端点供 Agent/RAG 应用调用
- 长上下文（最高 256K）文档处理与带思考链的问答

## 场景标签

`推理引擎` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L3:  Qwen 3.6-27B (AWQ-INT4) + DFlash speculative decoding on AMD Strix Halo (gfx1151).
> L20:  vLLM
> L58: > docker compose build --pull --no-cache

## 星数曲线

```mermaid
xychart-beta
    title "hec-ovi/vllm-awq4-qwen 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-29 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `69ac2369afb8` · [字段定义](../../DATASET.md)*
