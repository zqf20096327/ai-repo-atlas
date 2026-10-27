# robss2020/microllm-lab

⭐ 53 · JavaScript · NOASSERTION · 推送 2026-10-02 · [GitHub](https://github.com/robss2020/microllm-lab) · 个人维护

**在浏览器 WebGPU 里运行 Q4 量化小语言模型的实验台**

纯前端 WebGPU 应用：把 8 个 26M–360M 的小型 Llama 式/GPT-2 式检查点转为 Q4（group-32）权重，在 Safari/Chrome/Edge 中解码生成文本，权重缓存于本 origin 的 IndexedDB。提供 Metal 与 fused-NVIDIA 两种 WebGPU 解码路径，Benchmarks/Compare 页用 Chart.js 对各模型的速度（tok/s）与客观题套件通过率做图表对比。附 Python 转换脚本可将其他 Hugging Face 检查点转为 Q4 格式。限制：仅贪心解码、上下文上限 2048 token、模型会产生幻觉。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 个 Q4 量化小模型（26M–360M）在浏览器内直接生成文本
- Compare/Benchmarks 图表对比各模型速度与准确率
- 提供 convert_hf_to_pgw / convert_gpt2_to_pgw 转换脚本接入其他 Llama 式检查点
- 权重存 IndexedDB，提示词不离开本机

## 适用场景

- 在没有 API key 和 Python 环境的浏览器里体验本地小模型
- 对比多个小模型在我这台设备上的速度与准确率
- 为端侧功能选型前感受质量/速度权衡
- 把自己的 Llama 式 Hugging Face 检查点转成 Q4 在浏览器试跑

## 场景标签

`模型量化` `推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: **Run a 135M-class language model in the tab you already have open.**
> L22: Q4 (group-32) conversions of redistributable checkpoints, plus Metal and fused-NVIDIA WebGPU decoders (Llama-style 
> L69: The **Benchmarks** tab plots per-test wall time and pass/fail after a suite. **Compare** keeps the latest suite per

## 星数曲线

```mermaid
xychart-beta
    title "robss2020/microllm-lab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-27 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `7e2dd3af52be` · [字段定义](../../DATASET.md)*
