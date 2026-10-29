# QwenLM/Confident-Decoding

⭐ 34 · Python · 推送 2026-06-30 · [GitHub](https://github.com/QwenLM/Confident-Decoding) · 组织维护

**推理时逐 token 选取低熵中间层 logits 的解码方法（vLLM 分支）**

面向自回归语言模型的 logits 层选择方法：不固定使用最后一个 transformer 层，而是在近末端候选层中计算逐 token 预测熵，默认 trough 策略从末层向前扫描选取最靠近末层的熵谷，用该层 logits 解码。以 vLLM v0.19.1 分支形式提供：先 pip 安装 vLLM，再将修改源文件覆盖到已安装的 vllm 包目录，confident-vllm 目录不是独立可安装包。支持 Llama、Qwen、Gemma、DeepSeek-V2/GLM 等模型族，附基准评测框架与可引用论文。需 Python 3.10+、CUDA 12.1+、PyTorch 2.x。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- trough 等多种层选择策略（熵谷扫描、固定偏移等）
- 通过覆盖源文件方式集成到 vLLM v0.19.1，提供 serve 参数开关
- 支持 Llama/Qwen/Gemma/DeepSeek-V2/GLM/GPT-OSS 多模型族
- 附评测 harness，覆盖 gpqa/hle/lcb/longbench 等 6 项基准

## 适用场景

- 在自托管 vLLM 服务上启用置信层解码
- 对比不同层选择策略对基准成绩的影响
- 复现论文 Deeper is Not Always Better 的实验

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: An inference-time logits-layer selection method for autoregressive language models. Instead of always using the logi
> L5: This repository provides a fork of vLLM (v0.19.1) with Confident Decoding integrated, plus a benchmark evaluation ha

## 星数曲线

```mermaid
xychart-beta
    title "QwenLM/Confident-Decoding 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-29 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `04a118ae40e9` · [字段定义](../../DATASET.md)*
