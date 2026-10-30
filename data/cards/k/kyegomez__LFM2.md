# kyegomez/LFM2

⭐ 33 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/kyegomez/LFM2) · [官网](https://discord.gg/jM3Z6M9uMq) · 个人维护

**Liquid AI LFM2 架构的 PyTorch 最小实现，供研究教育用**

第三方用 PyTorch 复现 Liquid AI 博客文章描述的 LFM2 架构，官方未开源实现，声明仅供研究与教育用途。实现混合架构：16 个块（10 个 LIV 卷积块 + 6 个 GQA 块），包含双重门控短程卷积、分组查询注意力、SwiGLU、RMSNorm 与 RoPE。支持 350M/700M/1.2B 三种参数规模，通过 pip 安装，example.py 提供前向传播、注意力掩码、缓存等用法示例。声明非官方、与 Liquid AI 无关，实现可能与原模型存在差异。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 16 块混合架构：10 个 LIV 卷积块 + 6 个 GQA 块
- 支持 350M / 700M / 1.2B 三种模型规模
- 双重门控短程卷积 + GQA + RoPE + SwiGLU + RMSNorm

## 适用场景

- 研究 LFM2 架构的内部机制与代码实现
- 教学场景中学习混合卷积-注意力架构
- 在本地运行前向传播实验并按需扩展

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L6: This is a minimal, open-source implementation of the Liquid Foundation Model 2 (LFM2) architecture described in Liqu
> L10: - Hybrid architecture combining short-range convolutions with grouped query attention

## 星数曲线

```mermaid
xychart-beta
    title "kyegomez/LFM2 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-30"]
    y-axis "stars" 31 --> 34
    line [32, 33, 33]
```

2026-10-18 32 → 2026-10-30 33（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b733e7e537cf` · [字段定义](../../DATASET.md)*
