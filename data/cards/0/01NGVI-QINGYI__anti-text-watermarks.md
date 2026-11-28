# 01NGVI-QINGYI/anti-text-watermarks

⭐ 3 · Python · NOASSERTION · 推送 2026-11-10 · [GitHub](https://github.com/01NGVI-QINGYI/anti-text-watermarks) · 个人维护 · 中文 README

**针对统计式 LLM 水印与隐形 Unicode 标记的本地去除工具**

本地运行、零强制依赖的 Python 文本处理引擎，用于消除两类水印：统计式 token 采样水印（textGrain、SynthID-Text、Red-Green/Gumbel）与隐写式字符标记（零宽字符、同形字等）。将去水印建模为滑动上下文窗口上的约束优化问题：代码块、LaTeX、HTML、URL 作为原子 AST token 锁定不动，通过熵校准选择枢轴词替换以使检测 Z 分数降至阈值以下。数学原理整合自五个开源/学术工作并重新实现，内置 TextGrainSimulator 测试场与 Web Studio 控制台，另提供 Python SDK，支持三语文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AST 结构守卫：代码块、公式、HTML、URL 锁定不改写
- 贪心最大覆盖集调度器，仅编辑约 25.8% token 即破坏 4-gram 哈希
- 内置 TextGrainSimulator 实弹统计水印测试场与消融基准
- 零强制依赖 Python 代码库，可离线运行

## 适用场景

- 去除 AI 生成文本中的统计水印信号
- 清理文本中隐写的零宽字符与同形字标记
- 对去水印方案进行 Z 分数基准对比评测

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L8:  A local-first, zero-dependency toolkit against statistical LLM watermarks (OpenAI textGrain, Google SynthID-Text, R
> L56: `anti-text-watermarks` (`atw`) is an **auditable, offline-capable, zero-dependency** adversarial text processing en
> L61: - **Objective (Context-Hash Cascade Collapse)**: Select the minimum set of high-conditional-entropy pivot words and

## 星数曲线

```mermaid
xychart-beta
    title "01NGVI-QINGYI/anti-text-watermarks 星数(近 2 点)"
    x-axis ["2026-11-27", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-27 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `4c589b3ee3d8` · [字段定义](../../DATASET.md)*
