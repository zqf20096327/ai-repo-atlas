# stdlogits/neuron-lens

⭐ 24 · Python · MIT · 推送 2026-10-31 · [GitHub](https://github.com/stdlogits/neuron-lens) · [官网](neuron-lens.com) · 组织维护

**Qwen3-8B 等模型的 MLP 神经元与注意力头含义编目数据集**

面向机制可解释性研究的公开目录：用 R-lens 与 S-lens 两种基于 Jacobian/RelP 的透镜，从权重直接读出 Qwen3-8B（884,736 个神经元极性条目、1,152 头）与 Gemma 4 12B（1,474,560 条目、768 头）每个单元的读方向与写入含义，并结合 15M token 真实文本上的激活统计、精确 token 驱动测试与 Claude Haiku 生成的文字标签；Gemma 4 还含图像/声音响应数据。附带 16 项 findings，标注各深度上哪些读法可信。目录由 stdlogits/rs-lens 透镜生成，限制：中层单元从两侧都难读，原始读法共享 hub token。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖两个模型共约 236 万个神经元极性条目与 1,920 个注意力头
- 每条目含权重透镜读、激活统计、精确 token 驱动、可读性测试与文字标签
- Gemma 4 神经元额外含 49,694 张图像与 46,932 段声音的响应数据
- 按层深给出哪些读法可信的分层结论表

## 适用场景

- 查某个 Qwen3-8B 神经元或注意力头的含义与驱动 token
- 机制可解释性研究中选取层深与分析方法的参考
- 基于公开目录数据做神经元/头层面的统计分析

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L13: - **Catalog:** `stdlogits/neuron-lens`: every
> L95: Every neuron has a `+` and a `−` pole, so the catalog has 884,736 neuron entries and 1,152 heads for
> L138: Neurons and heads get the same five tables, one row per pole or per head: `reads` (weight-only lens


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `10655c50c8a2` · [字段定义](../../DATASET.md)*
