# 199-biotechnologies/gemma-4-abliterated

⭐ 22 · Python · NOASSERTION · 推送 2026-04-03 · [GitHub](https://github.com/199-biotechnologies/gemma-4-abliterated) · [官网](https://paperfoot.com) · 组织维护

**Gemma 4 31B 的去拒答权重编辑模型（MLX 4-bit）**

对 Google Gemma 4 31B-IT 做的 abliteration（去拒答）版本及其完整管线：通过收集有害/无害提示的激活，计算 60 个 transformer 层各自的拒答方向，对 embed_tokens、o_proj、down_proj 三个权重矩阵做正交化去除拒答投影，再量化为 MLX 4-bit 供 Apple Silicon 本地推理。基座权重来自 google/gemma-4-31b-it，模型发布于 HuggingFace。附 100 提示评测套件（50 能力 + 50 拒答）与可断点续跑的管线脚本。运行推理需 20GB+ 统一内存，完整管线需 64GB 内存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 逐层（60 层）计算拒答方向并做权重正交化
- 输出 MLX 4-bit 量化权重，本地 Apple Silicon 运行
- 100 提示评测套件（能力 50 + 拒答 50）
- 管线支持断点续跑（checkpointing）

## 适用场景

- 在 Apple Silicon 上本地运行去除了拒答行为的 Gemma 4 31B
- 复现或修改 abliteration 管线处理其他模型
- 用评测套件检验模型能力与拒答变化

## 场景标签

`模型评测` `模型量化` · 领域:评测与运维

## 证据(README 行号)

> L3: ### The first quality-preserving abliteration of Google's Gemma 4 31B. Full guardrail removal. Zero intelligence los
> L46: model, processor = load("199-biotechnologies/gemma-4-31b-abliterated-mlx-4bit")

## 星数曲线

```mermaid
xychart-beta
    title "199-biotechnologies/gemma-4-abliterated 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-29 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `70672a227b6f` · [字段定义](../../DATASET.md)*
