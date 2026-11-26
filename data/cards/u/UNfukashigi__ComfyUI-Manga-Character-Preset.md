# UNfukashigi/ComfyUI-Manga-Character-Preset

⭐ 5 · JavaScript · Apache-2.0 · 推送 2026-11-20 · [GitHub](https://github.com/UNfukashigi/ComfyUI-Manga-Character-Preset) · 个人维护

**ComfyUI 角色预设节点：一键切换提示词与三个 LoRA**

面向漫画等重复生成同一角色的场景，提供 ComfyUI 自定义节点：每个角色预设包含正/负提示词与最多三个 LoRA（各自独立的模型/CLIP 强度与 ON/OFF 开关），通过下拉框切换角色，编辑自动写回预设。预设存储在工作流 JSON 内，不跨工作流共享；另提供 12 个带悬停提示的一键提示词快捷按钮。安装为手动放置目录到 custom_nodes，无额外 Python 依赖，模型权重与 LoRA 不随仓库分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每个角色预设含正/负提示词与最多 3 个 LoRA，支持独立强度与 ON/OFF 切换
- 预设随工作流 JSON 保存，编辑自动更新
- 12 个一键提示词快捷按钮，悬停可预览文本
- 无额外 Python 依赖

## 适用场景

- 漫画项目中反复生成同一角色时一键切换提示词与 LoRA 组合
- 临时开关某个 LoRA 做效果对比而不改动配置
- 把角色预设随工作流 JSON 一起保存与复用

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: A custom node for switching between character prompts and up to three LoRAs with a single selection. Designed for ma
> L10: - Up to three LoRAs per character, with independent model and CLIP strengths and ON/OFF toggles.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `e0d764bdd37f` · [字段定义](../../DATASET.md)*
