# geshang777/GaMMA

⭐ 57 · Apache-2.0 · 推送 2026-05-04 · [GitHub](https://github.com/geshang777/GaMMA) · 组织维护

**音乐理解多模态大模型：统一处理全局语义与时序推理**

论文 GaMMA 的官方实现，一个面向音乐理解的大型多模态模型，在统一参数空间内同时处理全局音乐理解（风格、情绪等非时序语义）与时序音乐推理。架构采用编码器-解码器范式，结合语言建模、双音频专家与门控融合机制；训练流程分预训练、监督微调与强化学习三阶段。提供 PyTorch 与 vLLM 两种推理路径，含 CLI 与 Web Demo。实现基于 Python 3.12 与 CUDA 12.4，推理需 NVIDIA A100 80GB 显存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一参数空间内联合全局音乐理解与时序推理
- 双音频专家 + 门控融合的编码器-解码器架构
- 预训练/监督微调/强化学习三阶段渐进训练
- 提供 PyTorch 与 vLLM 两种推理路径（CLI 与 Web Demo）

## 适用场景

- 对完整歌曲做风格、情绪与人声特征的问答理解
- 需要时序定位的音乐结构推理任务
- 复现论文或基于 checkpoint 做音乐理解研究

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L5: Introducing GaMMA, a large multimodal model designed to jointly handle both global music understanding and temporal 
> L11: - `[2026-5-1]`:🔥 GaMMA is released! Check out our project page and paper.

## 星数曲线

```mermaid
xychart-beta
    title "geshang777/GaMMA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 56 --> 58
    line [57, 57]
```

2026-10-18 57 → 2026-10-31 57（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c3c9286b307e` · [字段定义](../../DATASET.md)*
