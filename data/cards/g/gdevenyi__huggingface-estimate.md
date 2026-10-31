# gdevenyi/huggingface-estimate

⭐ 30 · JavaScript · 推送 2026-07-20 · [GitHub](https://github.com/gdevenyi/huggingface-estimate) · [官网](https://gabriel.devenyi.ca/huggingface-estimate/) · 个人维护

**为 HuggingFace GGUF 模型估算显存/内存用量的网页计算器**

面向在本地运行 GGUF 量化模型的开发者的 Web 工具与 Node CLI：输入 HuggingFace 仓库路径，通过 HTTP Range 请求解析 GGUF 元数据（无需下载模型），计算模型权重、KV cache、激活与多模态投影器的 VRAM/RAM 占用；支持 89 种架构、106 种量化类型与 19 种 KV cache 量化类型，Dense/MoE 分层放置逻辑对齐 llama.cpp 语义（--cpu-moe/--n-cpu-moe）。提供 GPU/CPU 预设，按 FLOPs 与带宽估算 decode/prefill/TTFT 吞吐上限（README 注明为理论上限，实测约为 40-70%）。浏览器版需经 HTTP 服务运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无需下载即可解析 HuggingFace GGUF 元数据并计算显存/内存占用
- 覆盖 89 种架构、106 种量化类型（含 ik_llama.cpp/turboquant/rotorquant/tq3 分支）
- Dense/MoE 分层放置与 --cpu-moe 语义对齐 llama.cpp 实现
- 基于硬件预设估算 decode/prefill/TTFT 吞吐理论上限并标注瓶颈类型

## 适用场景

- 下载模型前判断某个 GGUF 量化版本能否装进我的显卡
- 估算特定上下文长度与 KV cache 量化下的内存需求
- 比较不同 GPU/CPU 组合下的推理吞吐上限

## 场景标签

 · 领域:LLM 基础设施/推理资源规划

## 证据(README 行号)

> L5:  Estimate VRAM and RAM requirements for any GGUF model from HuggingFace — no download required.
> L32: Performance flags: `--gpu <name>` (e.g. `"RTX 4090"`, matches `gpu-data.json`), `--cpu <name>` (e.g. `"Ryzen 9 7950

## 星数曲线

```mermaid
xychart-beta
    title "gdevenyi/huggingface-estimate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-31 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `193158d82ac1` · [字段定义](../../DATASET.md)*
