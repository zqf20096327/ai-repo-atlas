# CASE-Lab-UMD/LLM-Drop

⭐ 193 · Python · Apache-2.0 · 推送 2026-10-02 · [GitHub](https://github.com/CASE-Lab-UMD/LLM-Drop) · [官网](https://openreview.net/forum?id=1I7PCbOPfe) · 组织维护

**Transformer 层删除压缩框架：统一删层提速省显存**

TMLR 2026 论文的官方实现，面向 LLM 研究者与模型压缩使用者。提供 Block Drop、Attention Drop、MLP Drop、Joint Drop 四类层删除策略的统一框架与对比基准，通过 config.json 中的 drop 列表配置要删除的层，产出的模型经 auto_map 可由 Hugging Face AutoModelForCausalLM 直接加载，并可叠加 AWQ/GPTQ 4-bit 量化。论文报告最高 2.1× 推理加速与超 40% KV cache 节省，保留 95-98% 基准能力。提供 Hugging Face 上的预删除 checkpoint 与基准评测脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一四类层删除策略（Block/Attention/MLP/Joint）的框架与对比
- 产出模型经 auto_map 可由 AutoModelForCausalLM 直接加载
- 可叠加 AWQ/GPTQ 4-bit 后训练量化
- Hugging Face 提供 6 个预删除 checkpoint（Mistral/Llama-2/Llama-3/Gemma-2）

## 适用场景

- 压缩 LLM 以降低推理延迟与 KV cache 占用
- 研究不同层级（注意力/MLP/整块）冗余度并复现论文基准
- 为端侧部署生成更小的量化模型

## 场景标签

`模型量化` · 领域:训练与推理

## 证据(README 行号)

> L31: > This is the official repository for the paper **Uncovering the Redundancy in Transformers via a Unified Study of 
> L43: - ⚡ **Significant Speedup & Memory Savings**: Achieves up to **2.1× inference speedup** and over **40% KV cache mem
> L61: |Strategy|Dropped Components|Target Redundancy|Memory / KV Cache Saving|Latency Speedup|Recommended Use Case|

## 星数曲线

```mermaid
xychart-beta
    title "CASE-Lab-UMD/LLM-Drop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 192 --> 194
    line [193, 193]
```

2026-10-18 193 → 2026-10-28 193（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `75a1f9542029` · [字段定义](../../DATASET.md)*
