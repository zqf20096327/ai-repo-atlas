# Siddhant-K-code/LLMTraceFX

⭐ 14 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/Siddhant-K-code/LLMTraceFX) · [官网](https://siddhantkhare.com/writing?q=Inference+lab) · 个人维护

**面向本地模型与 OpenAI 兼容 API 的 LLM 推理测量与验证工具包**

evidence-first 的推理测量工具包：将 MLX/MLX-LM 本地运行、OpenAI 兼容流式 API、llama.cpp 导入与 Apple Instruments 采集的时序、内存与 trace 数据写入统一的 ExperimentRecord 规范，数值均带单位与来源（原生测量/墙钟/provider 上报/推导/估计），不可得的观测保持缺失。用确定性工作负载核验模型输出，含 KV-cache 真值审计演示、可恢复的哈希校验运行，以及预注册的 vLLM 编译交叉对比协议（含 Modal L4 变体，目前被离线算术门拒绝执行）。面向做推理评测与性能研究的研究者/开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一 ExperimentRecord 证据模式，数值带单位与 provenance，缺失观测不补零
- 离线 KV-cache 真值审计演示（make kv-cache-demo）生成可独立校验的哈希绑定证据包
- 确定性工作负载目录 + 哈希校验的可恢复运行，失败/部分行保持可见
- 预注册的 vLLM eager/compiled 交叉对比协议，付费运行需签名授权回执

## 适用场景

- 对 Apple silicon 上本地模型运行做时序与内存测量
- 核验 LLM 输出是否匹配固定工作负载，保留失败证据
- 按预注册协议对比 vLLM 编译模式的性能差异

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L21: LLMTraceFX is an evidence-first inference toolkit for local models and
> L142: Inference collectors and the llama.cpp importer produce `ExperimentRecord`
> L186: `llmtracefx-vllm-crossover plan` renders the preregistered Qwen3-8B vLLM

## 星数曲线

```mermaid
xychart-beta
    title "Siddhant-K-code/LLMTraceFX 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `8c1c819a971e` · [字段定义](../../DATASET.md)*
