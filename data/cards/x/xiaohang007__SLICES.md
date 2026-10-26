# xiaohang007/SLICES

⭐ 145 · Python · LGPL-2.1 · 推送 2026-03-03 · [GitHub](https://github.com/xiaohang007/SLICES) · [官网](https://www.nature.com/articles/s41467-023-42870-7) · 个人维护 · 中文 README

**晶体结构可逆字符串表示工具：编码/重构晶体并生成新材料**

SLICES 提供晶体结构的可逆、不变字符串表示：可将晶体编码为 SLICES 字符串、由字符串重构原晶体结构（Text2Crystal），并基于 MatterGPT / SLICES-PLUS 生成具有目标性质的固态材料。提供 Hugging Face 在线转换器与 MatterGPT 在线 Demo，本地支持 Ubuntu/WSL 安装与 Docker 镜像，图形界面需 slices>=2.0.8。相关成果发表于 Nature Communications（2023），示例基于 pymatgen 结构对象。50 系显卡需将 PyTorch 调整为 cu128 版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | LGPL-2.1 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 晶体结构与 SLICES 字符串的双向转换（编码/重构）
- 基于 MatterGPT / SLICES-PLUS 的固态材料逆向设计
- 提供 Hugging Face 在线转换器与在线 Demo
- 支持本地 Conda 安装、Docker 镜像与图形界面

## 适用场景

- 将 CIF 晶体结构编码为字符串用于机器学习
- 用生成模型逆向设计具有目标性质的新材料
- 在 Materials Project 全库中做新颖性检查

## 场景标签

 · 领域:材料科学/晶体学

## 证据(README 行号)

> L3: The **Simplified Line-Input Crystal-Encoding System (SLICES)** is the first invertible and invariant crystal represe
> L19: 1. **Encode crystal structures into SLICES strings**
> L21: 3. **Inverse design of solid-state materials with desired properties using MatterGPT**

## 星数曲线

```mermaid
xychart-beta
    title "xiaohang007/SLICES 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 144 --> 146
    line [145, 145]
```

2026-10-18 145 → 2026-10-26 145（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `3c42b2cdabf0` · [字段定义](../../DATASET.md)*
