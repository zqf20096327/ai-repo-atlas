# DarioFT/ComfyUI-Qwen3-TTS

⭐ 316 · Python · 推送 2026-02-09 · [GitHub](https://github.com/DarioFT/ComfyUI-Qwen3-TTS) · [官网](https://github.com/QwenLM/Qwen3-TTS) · 个人维护

**ComfyUI 的 Qwen3-TTS 语音合成节点套件，支持音色克隆与微调**

面向 ComfyUI 用户的 Qwen3-TTS 自定义节点套件：支持 1.7B 与 0.6B 模型，提供 9 种预设音色合成、自然语言音色设计、短参考音频声音克隆三种生成方式；附带用自有数据集（.wav+.txt）微调专属音色模型的完整流程（数据制作、分词编码、训练、说话人相似度评估）。模型按需下载至 ComfyUI 模型目录，支持 HuggingFace/ModelScope 双源；支持 11 种语言的跨语言合成、FlashAttention 2 自动回退 SDPA。安装需手动 git clone 并 pip 安装依赖，上游包固定 transformers==4.57.3 可能降级现有版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 种预设音色、自然语言音色设计、参考音频克隆三种合成模式
- 自带微调流程：数据集制作、分词缓存、断点续训、8-bit AdamW 与梯度检查点等显存优化
- 微调结果评估：说话人相似度、mel 谱距离、语速比
- 11 种语言跨语言合成；模型按需下载且兼容 HuggingFace/ModelScope 缓存迁移

## 适用场景

- 在 ComfyUI 工作流中直接生成多语言语音
- 用一段参考音频克隆特定音色并批量合成
- 用自有数据集训练专属音色模型并对比评估

## 场景标签

`语音合成` `微调` · 领域:内容生成

## 证据(README 行号)

> L2: A ComfyUI custom node suite for Qwen3-TTS, supporting 1.7B and 0.6B models, Custom Voice, Voice Design, Voice Clonin
> L79: - **speaker**: Choose one of the 9 presets (e.g., Vivian, Ryan).
> L85: - **instruct**: Describe the voice you want, e.g., *"A deep, resonant male voice, narrator style, calm and professi

## 星数曲线

```mermaid
xychart-beta
    title "DarioFT/ComfyUI-Qwen3-TTS 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25", "2026-10-28"]
    y-axis "stars" 310 --> 317
    line [311, 313, 315, 316]
```

2026-10-18 311 → 2026-10-28 316（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `83699b415e7f` · [字段定义](../../DATASET.md)*
