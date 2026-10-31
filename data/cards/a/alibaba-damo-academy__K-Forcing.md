# alibaba-damo-academy/K-Forcing

⭐ 19 · Python · Apache-2.0 · 推送 2026-08-16 · [GitHub](https://github.com/alibaba-damo-academy/K-Forcing) · [官网](https://arxiv.org/abs/2606.10820) · 组织维护 · 中文 README

**论文官方实现：一次前向联合解码 k 个 token 的语言建模范式**

K-Forcing 论文的官方代码库：将自回归语言模型蒸馏为 push-forward 语言模型（PFLM），以 k 个独立均匀噪声为输入，一次前向生成 k 个未来 token，输出长度固定、复用原 AR 主干。提供 OWT 与 LM1B 数据集上的 AR/PFLM(k=4)/MDLM 基线 checkpoint（托管于 HuggingFace，可自动下载），并通过单一脚本 batch_inference_with_prefix.py 支持三种模型的批量前缀推理。安装走 uv sync 并需自行下载 flash-attn CUDA wheel；训练配方尚未发布（TODO 中）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一次前向联合生成 k 个 token 的 PFLM 范式
- 提供 AR/PFLM/MDLM 三种模型的批量推理脚本
- checkpoint 托管于 HuggingFace，省略路径时自动下载
- PFLM 推理支持任意 K（至多 4）与可选频率惩罚

## 适用场景

- 复现论文中 PFLM/AR/MDLM 的对比推理实验
- 在批量服务场景测试固定长度多 token 解码
- 基于公开 checkpoint 研究蒸馏得到的 push-forward 模型

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L1: K-Forcing: Joint Next-K-Token Decoding via Push-Forward Language Modeling
> L18: K-Forcing distills an autoregressive (AR) language model into a **push-forward language model (PFLM)** that generat
> L54: `batch_inference_with_prefix.py` supports AR, PFLM, and MDLM inference with batched generation from text prefixes a

## 星数曲线

```mermaid
xychart-beta
    title "alibaba-damo-academy/K-Forcing 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `945bfd5ed1a4` · [字段定义](../../DATASET.md)*
