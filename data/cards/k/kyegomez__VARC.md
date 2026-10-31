# kyegomez/VARC

⭐ 14 · Python · Apache-2.0 · 推送 2025-11-19 · [GitHub](https://github.com/kyegomez/VARC) · [官网](https://discord.gg/EamjgSaEQf) · 个人维护

**VARC 论文的开源 PyTorch 实现：用 ViT 解决 ARC 任务**

对论文《ARC Is a Vision Problem》模型架构的单文件开源实现：将 ARC 任务转化为图像到图像翻译问题，用固定尺寸 Canvas 放置网格，配合标准 Vision Transformer（分组查询注意力 + RMSNorm）、2D 可分离位置编码、任务条件化 token 与几何/颜色数据增强，并通过测试时训练实现对未见任务的泛化。README 报告在 ARC-1 上从零训练达到 60.4% 准确率。面向使用 PyTorch 的 AI 研究者与开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Canvas 表示将 ARC 任务作为自然图像处理
- 带分组查询注意力 + RMSNorm 的 ViT 实现
- 测试时训练泛化到未见任务，ARC-1 准确率 60.4%
- 提供 VisionARCModel/ARCLoss 的 Python API 与 example.py

## 适用场景

- 复现或扩展 VARC 论文的视觉方法
- 研究 ViT 在 ARC 推理任务上的能力
- 基于测试时训练做泛化实验

## 场景标签

 · 领域:机器学习/视觉推理

## 证据(README 行号)

> L5: This is a clean, open-source, single-file implementation of the model architecture from the "ARC Is a Vision Problem
> L19: |**Standard vision architecture**|Demonstrates that a vanilla Vision Transformer can effectively solve ARC tasks wh

## 星数曲线

```mermaid
xychart-beta
    title "kyegomez/VARC 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `4f40e94461ae` · [字段定义](../../DATASET.md)*
