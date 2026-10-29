# mni-ml/transformer

⭐ 27 · JavaScript · 推送 2026-05-05 · [GitHub](https://github.com/mni-ml/transformer) · 组织维护

**Node.js 实现的 12M 参数 Transformer LLM：训练与文本生成**

用 @mni-ml/framework 在 Node.js 中实现的最小 Transformer 语言模型（约 1200 万参数），基于 BPE 字节级分词。包含 Python 数据准备脚本，可从 TinyStories 或 YouTube-Commons 字幕构建数据集；训练与采样在 JavaScript 中运行，提供 CPU 与 GPU（可选 CUDA/WebGPU 原生包，GPU 采样需 native.flashAttention）两条路径。默认检查点与分词器已提交到 out/ 目录。

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

- Node.js 训练与采样的 12M 参数 LLM
- TinyStories / YouTube-Commons 数据集构建脚本（含 BPE 训练）
- CPU 与 GPU 双路径（GPU 需可选 CUDA/WebGPU 原生包与 flashAttention）
- 通过环境变量配置超参数（层数/头数/嵌入维度/批次等）

## 适用场景

- 学习 Transformer 训练流程的完整实现
- 在 Node.js 环境中训练小型语言模型
- 基于 TinyStories 数据做文本生成实验

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L3: A 12M paramater LLM in **Node.js**, trained with `@mni-ml/framework` on **BPE-tokenized** text. You can build the da
> L10: |`src/train.js`|**CPU** training (default npm native build; matmul attention fallback)|

## 星数曲线

```mermaid
xychart-beta
    title "mni-ml/transformer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-29 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `a1d5f4d592a1` · [字段定义](../../DATASET.md)*
