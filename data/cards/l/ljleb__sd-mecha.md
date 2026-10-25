# ljleb/sd-mecha

⭐ 81 · Python · MIT · 推送 2026-08-17 · [GitHub](https://github.com/ljleb/sd-mecha) · 个人维护

**通用模型合并库：内存高效地合并扩散模型与 LLM 等权重**

sd-mecha 是一个 Python 模型合并库，可合并扩散模型、LLM、VLM、审美评分器等任意 state dict 模型。核心机制：以 .mecha 格式存储可读且可执行的合并配方（recipe），按键逐步合并并在可用时立即保存，从而无需将中间模型落盘，可在低配硬件上一次合并大量模型。内置 SD1.5/SDXL/SD3/FLUX 支持，可合并 LyCORIS 网络，支持 MBW 块级超参数，并提供可扩展接口添加自定义模型与合并方法。安装方式为 pip install sd-mecha。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- .mecha 格式存储可读且可执行的合并配方
- 按键合并并即时保存，无需中间模型落盘
- 内置 SD1.5/SDXL/SD3/FLUX 支持，可合并 LyCORIS 网络
- MBW 块级超参数与自定义模型/合并方法扩展接口

## 适用场景

- 我要把多个 Stable Diffusion 或 LLM 权重合并成一个模型
- 在低配硬件上执行大规模多模型合并
- 保存和复现完整可追溯的合并配方

## 场景标签

 · 领域:模型工程/模型合并

## 证据(README 行号)

> L13: sd-mecha is a general memory-efficient model merging library. It can merge *any* model:
> L22: - Memory efficient model merging: merge a very large number of models in a single execution

## 星数曲线

```mermaid
xychart-beta
    title "ljleb/sd-mecha 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 79 --> 82
    line [80, 81, 81]
```

2026-10-18 80 → 2026-10-25 81（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0980d2e95413` · [字段定义](../../DATASET.md)*
