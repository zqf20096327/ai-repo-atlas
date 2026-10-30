# kyegomez/SimplifiedTransformers

⭐ 16 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/kyegomez/SimplifiedTransformers) · [官网](https://discord.gg/GYbXvDGevY) · 个人维护

**简化 Transformer 模块结构的 PyTorch 实现库**

基于信号传播理论与实证观察对标准 Transformer block 做结构简化：移除跳跃连接、投影参数、顺序子块和归一化层。作者报告简化后的模型在保持同等训练速度与性能的同时，训练吞吐量提升 15%、参数量减少 15%。以 pip 包形式提供的 PyTorch 实现库，供研究者在实验中使用，MIT 许可。README 仅含简介、安装与一段用法示例，无训练脚本或详细文档。

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

- 移除跳跃连接、投影参数、顺序子块与归一化层
- 报告同等性能下训练吞吐快 15%、参数少 15%
- PyTorch 实现并以 pip 包分发

## 适用场景

- 研究者复现简化 Transformer 块的结构修改
- 在自有模型中替换标准 Transformer 块以减少参数量
- 神经架构消融实验的对照实现

## 场景标签

 · 领域:深度学习/模型实现

## 证据(README 行号)

> L4: The author presents an implementation for Simplifying Transformer Blocks. The standard transformer blocks are comple
> L16: from simplified_transformers.main import SimplifiedTransformers

## 星数曲线

```mermaid
xychart-beta
    title "kyegomez/SimplifiedTransformers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `06352a5755d6` · [字段定义](../../DATASET.md)*
