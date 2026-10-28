# lucidrains/ultra-mem

⭐ 28 · Python · MIT · 推送 2025-11-04 · [GitHub](https://github.com/lucidrains/ultra-mem) · 个人维护

**UltraMem 稀疏记忆层的 PyTorch 实现，供深度学习研究者使用**

lucidrains 对 ByteDance AI Lab 论文 Ultra-Sparse Memory Network（UltraMem，改进 Product Key Memory 设计）的 PyTorch 实现，以 pip 包形式提供 UltraMem 模块，可导入并与 torch 配合使用；附带字符级语言模型训练脚本（uv run train.py）。面向深度学习研究者在语言模型中集成超稀疏记忆层。README 未给出硬件要求或预训练权重说明。

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

- 实现 UltraMem（改进的 Product Key Memory 设计）
- pip 安装的 Python 包，提供可导入的 UltraMem 模块
- 附带字符级 LM 训练脚本

## 适用场景

- 在语言模型中实验稀疏记忆层替代 FFN
- 复现或扩展 Ultra-Sparse Memory Network 论文方法
- 研究持续学习中的稀疏记忆微调

## 场景标签

 · 领域:深度学习/记忆网络

## 证据(README 行号)

> L5: Implementation of UltraMem, improved Product Key Memory design, from Bytedance AI labs
> L17: from ultra_mem import UltraMem

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/ultra-mem 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `bcc84c7df55b` · [字段定义](../../DATASET.md)*
