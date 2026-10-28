# srk0102/AnimTOON

⭐ 22 · Python · MIT · 推送 2026-04-11 · [GitHub](https://github.com/srk0102/AnimTOON) · [官网](https://huggingface.co/srk0102200/AnimTOON-3B) · 个人维护

**将 SVG 动画化为 Lottie 的 3B 文本格式模型与工具链**

AnimTOON 是一种面向 LLM 的纯文本动画格式及配套 3B 模型（Qwen2.5-3B-Instruct + LoRA）：模型只输出动画关键帧（166-597 tokens），形状来自输入 SVG，转换器确定性生成合法 .lottie 文件，README 称 token 用量较原始 Lottie JSON 减少 98.8%。v3 支持多部件 SVG 动画与 14 层角色走路/待机循环，推理约需 5GB VRAM。自述为早期研究版本，模型训练约完成 60%，不支持形状生成（必须提供 SVG）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 模型仅生成动画关键帧，SVG 提供形状，转换器保证 100% 格式合法
- v3 支持 14 层协调角色 walk/idle 循环与多部件 SVG 动画（47 部件演示）
- 推理约 5GB VRAM，训练在单张 RTX 5060 Ti 16GB 完成（LoRA/Unsloth）
- 提供 AnimTOON <-> Lottie JSON <-> .lottie 双向转换器与训练数据管线

## 适用场景

- 把图标/Logo 的 SVG 动画化为 Lottie 文件用于前端播放
- 生成简单角色 walk/idle 循环动画
- 基于 MMLottie 数据训练自己的动画生成模型

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L88:     |  SVG   | --> | Prompt  | --> | AnimTOON  | --> |.lottie |
> L124: - SVG -> animated .lottie pipeline (python-lottie + model + converter)
> L156: python test_svg_pipeline.py inputs/apple.svg

## 星数曲线

```mermaid
xychart-beta
    title "srk0102/AnimTOON 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `274238fd416c` · [字段定义](../../DATASET.md)*
