# Tencent-Hunyuan/Hy-Embodied-RxBrain-1.0

⭐ 132 · Python · NOASSERTION · 推送 2026-07-28 · [GitHub](https://github.com/Tencent-Hunyuan/Hy-Embodied-RxBrain-1.0) · 组织维护

**具身认知多模态基础模型：统一理解、世界状态预测与子目标规划**

腾讯 Robotics X、福田实验室与混元团队发布的约 6.2B 参数具身认知基础模型，单一模型提供三项能力：图像与多帧视频的问答及思维链推理；预测动作产生的近未来帧（世界模型式想象）；将任务分解为子步骤，同时输出下一步动作的语言描述与目标图像。提供模型权重（HuggingFace）、推理入口脚本（T2I、多帧生成、VQA、交错规划）与 VQA/多帧生成/交错生成的微调代码，模型基于 UnifiedMoT 三流架构（文本/视觉/生成）并使用 FLUX VAE。运行要求 Python 3.10+ 与 CUDA GPU（flash-attn），另需自行获取 FLUX VAE 的 ae.safetensors。Apache 2.0 许可，附 arXiv 技术报告与项目主页，具身认知基准 RxBrain-Bench 尚在 TODO 中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 6.2B 模型统一具身理解推理、世界状态预测与联合子目标规划
- 交错规划同时输出每步的下一步动作（语言）与目标图像（视觉）
- 提供推理脚本与 VQA/多帧生成/交错生成的微调代码
- 模型权重托管于 HuggingFace，微调后 checkpoint 可直接用推理脚本运行

## 适用场景

- 机器人任务规划：输入观测图像与任务描述，得到分步动作与目标图像
- 在真实或仿真场景下做图像/视频具身问答与推理
- 预测动作执行后的近未来世界状态帧
- 在自有具身数据上微调 VQA 与生成能力

## 场景标签

`多模态` `微调` · 领域:感知与多模态

## 证据(README 行号)

> L17: **RxBrain** (`Hy-Embodied-RxBrain-1.0`) is a **unified multimodal foundation model for embodied cognition** —
> L20: - 🤖 **Embodied Understanding & Reasoning** — question answering and chain-of-thought over images and multi-frame vi
> L21: - 🔮 **World State Prediction** — imagine the near-future frames an action produces in the physical world.
> L22: - 🧩 **Joint Subgoal Planning** — decompose a task into steps, emitting for each step *both* the next action (langua

## 星数曲线

```mermaid
xychart-beta
    title "Tencent-Hunyuan/Hy-Embodied-RxBrain-1.0 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 131 --> 133
    line [132, 132]
```

2026-10-18 132 → 2026-10-27 132（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `735d7f59b45d` · [字段定义](../../DATASET.md)*
