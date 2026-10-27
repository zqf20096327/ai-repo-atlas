# zs1314/AHD

⭐ 39 · Python · 推送 2026-04-13 · [GitHub](https://github.com/zs1314/AHD) · 组织维护

**dLLM 免训练解码策略 AHD 的官方实现（ACL 2026 论文）**

扩散大语言模型（dLLM）的训练无关、即插即用动态解码策略 AHD 的官方代码库，配套论文投至 ACL 2026。提供在 LLaDA-8B-Instruct、LLaDA-1.5、MMaDA-8B-MixCoT、DIFFA 四种模型上的解码实现与评测脚本，覆盖 BBH、MMLU-Pro、HumanEval、MATH、MathVista 等文本与多模态基准；部分评测任务以 GPT（默认 gpt-4.1-mini）作 LLM-judge，需配置 OpenAI API key。每个模型分支使用独立的 conda 环境（Python 3.10-3.12）安装依赖。Todo 中列出重构代码库与多 batch-size 支持为未完成项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 训练无关、即插即用的 dLLM 解码策略
- 覆盖 LLaDA / LLaDA-1.5 / MMADA / DIFFA 四种模型的实现
- 提供 BBH、MMLU-Pro、HumanEval、MathVista 等多基准评测脚本
- AHD 专用超参（kl_threshold_AHD、history_length_AHD）可在脚本中配置

## 适用场景

- 在 LLaDA 等 dLLM 上运行 AHD 解码生成文本
- 复现论文在文本与多模态基准上的评测结果
- 对比 Baseline 与 AHD 的解码效果

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: This is the official implementation of **AHD (Anchor-based History-stable Decoding)**, a training-free, plug-and-pla
> L16: │   ├── generate_AHD_acc.py # AHD decoding implementation

## 星数曲线

```mermaid
xychart-beta
    title "zs1314/AHD 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-27 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `8ec38748c883` · [字段定义](../../DATASET.md)*
