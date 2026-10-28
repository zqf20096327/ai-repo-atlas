# ElectronGirl/ComfyUI-Anima-Ref-Adapter

⭐ 33 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/ElectronGirl/ComfyUI-Anima-Ref-Adapter) · 个人维护

**ComfyUI 节点包：单参考图保持角色一致性的 Anima 图像生成**

面向 ComfyUI 用户的 Anima 参考图适配器：给定一张参考图与仅描述场景的提示词，生成保持角色特征（发型、瞳色、服装）与部分画风、但姿势/背景/构图跟随提示词的图像。机制为参考图编码为第二潜在帧、偏移 RoPE 坐标避免像素对齐复制，并由 rank-32 LoRA（45.9M 参数）学习读取该帧，配合独立文本/参考引导与 APG。属试验版本：仅 300 训练角色、2,000 步，仅用 Anima 生成图像训练；身份迁移优于风格，细节易丢失。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 参考图作为偏移 RoPE 的第二潜在帧，避免姿势复制
- rank-32 LoRA（45.9M 参数）读取参考帧
- 提供 Loader / Ref Latent / Ref Guider 三个自定义节点与示例工作流
- 试验版本：300 训练角色、2,000 步

## 适用场景

- 用单张参考图让 Anima 生成同角色不同场景的图像
- 为原创角色（无角色名/画师标签）保持一致性生成
- 在 ComfyUI 中做角色与风格迁移实验

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L13: Give Anima a single reference image and a prompt that only
> L66: - A **rank-32 LoRA** (45.9M parameters) learns to read that frame. It was trained on pairs of the same


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `376b3fc12acf` · [字段定义](../../DATASET.md)*
