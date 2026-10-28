# Siwoo4985/Micro-Diffusion

⭐ 35 · Python · MIT · 推送 2026-04-13 · [GitHub](https://github.com/Siwoo4985/Micro-Diffusion) · 个人维护

**约150行纯Python的离散文本扩散教学实现**

受 Karpathy MicroGPT 启发的学习型仓库：用约150行代码演示离散文本扩散的核心循环——训练时按噪声等级将token替换为[MASK]，生成时从全掩码出发按置信度逐步揭示。提供三个脚本：两个 NumPy MLP 版本和一个 PyTorch 4层双向 Transformer 版本，去噪器架构可替换。数据为 names.txt 中 32,000 个小写人名，字符级词表28。无 checkpoint、评测与打包模块，定位为可读性优先的教学参考实现而非生产系统。

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

- 同一扩散循环下三种去噪器实现：2层/3层 MLP（NumPy）与 4层 Transformer（PyTorch）
- mask→denoise→unmask 的吸收态扩散过程，含 cosine 掩码调度与置信度揭示
- 全部脚本支持 --seed/--steps/--samples 等 CLI 参数
- GitHub Actions 冒烟测试覆盖 NumPy 与 PyTorch 路径

## 适用场景

- 通过可运行的小代码理解离散文本扩散的训练与生成循环
- 对比自回归与扩散两种文本生成路径的差异
- 替换去噪器架构做扩散循环实验

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L11: Karpathy's MicroGPT showed how GPT works in a few hundred lines. This project aims for the same style of explanatio
> L47: Train: given masked text at noise level `t`, predict the original.
> L48: Generate: start from all masks, then reveal the most confident predictions first.

## 星数曲线

```mermaid
xychart-beta
    title "Siwoo4985/Micro-Diffusion 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-28 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `eb05b9ae2e4b` · [字段定义](../../DATASET.md)*
