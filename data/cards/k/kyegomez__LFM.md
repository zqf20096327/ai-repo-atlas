# kyegomez/LFM

⭐ 231 · Python · MIT · 推送 2026-10-13 · [GitHub](https://github.com/kyegomez/LFM) · [官网](https://discord.com/servers/agora-999382051935506503) · 个人维护

**Liquid AI 液态基础模型（LFM）的开源 PyTorch 实现**

第三方对 Liquid AI 闭源 LFMs 的开源复现尝试，非官方仓库，以论文为参考。提供 pip 可安装的 lfm-torch 包，包含 LFModel 模型代码，并引入结合液态神经网络、Transformer 注意力与 MoE 的 Liquid Transformer 架构。作者声明该项目非常实验性且处于早期，训练脚本尚在开发中，仍需接入实际分词器。模型架构署名归 liquid.ai 原作者，采用 MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- LFMs 的 PyTorch 开源实现（非官方）
- Liquid Transformer：液态神经网络 + Transformer 注意力 + MoE
- pip 安装包 lfm-torch 提供 LFModel

## 适用场景

- 研究并复现液态基础模型架构
- 在 PyTorch 中实验液态神经网络与 MoE 组合
- 跟进 LFM 论文的代码化实现进展

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L5: This is an attempt to make an open source implementation of LFMs, this is obviously not the official repository beca
> L17: from lfm_torch.model import LFModel
> L23: A novel neural architecture combining Liquid Neural Networks, Transformer attention mechanisms, and Mixture of Expe

## 星数曲线

```mermaid
xychart-beta
    title "kyegomez/LFM 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23"]
    y-axis "stars" 229 --> 232
    line [230, 231, 231]
```

2026-10-18 230 → 2026-10-23 231（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a6e7443a7d1b` · [字段定义](../../DATASET.md)*
