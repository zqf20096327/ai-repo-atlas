# vavo/TagPilot

⭐ 40 · HTML · MIT · 推送 2026-07-24 · [GitHub](https://github.com/vavo/TagPilot) · 个人维护

**浏览器端 LoRA 训练数据集打标与裁剪管理工具**

单文件 HTML 浏览器应用，面向 Stable Diffusion/Flux LoRA 训练者，完成图像上传（含 ZIP 与已有 .txt 配对）、触发词前置、批量 AI 打标与描述生成、自由裁剪与预设比例、本地哈希去重、标签全局清理，并导出图像+.txt 的 ZIP 供 kohya_ss 等训练器使用。AI 打标支持多种云端模型（Gemini/Claude/Grok/OpenAI）与 vLLM OpenAI 兼容端点、DeepDanbooru、WD1.4；API key 存于浏览器本地存储，图像仅在打标时发送至所选提供方。安装仅需克隆仓库并在浏览器打开 HTML 文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多种 AI 打标后端：Gemini、Claude、Grok、OpenAI、vLLM 兼容端点、DeepDanbooru、WD1.4
- 触发词自动作为每张图首标签，批量模式支持忽略/追加/覆盖
- 预设 LoRA 裁剪比例（1:1、16:9 等）与可配置输出宽度
- 本地哈希去重与浏览器本地存储 API key，无需服务器

## 适用场景

- 为 LoRA 训练准备带触发词和标签的图像数据集
- 批量给图像生成标签和描述文本并导出 ZIP
- 对已打标数据集做裁剪、去重与标签全局清理

## 场景标签

`微调` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L17: - **AI Tagging Turbo**: Powered by Gemini 3.1 Flash Lite, Claude Sonnet 4.5, Grok 4.3, OpenAI GPT-5.4 Mini, vLLM Op
> L27: - **Export Glory**: One click → pristine ZIP with images + .txt files, ready for kohya_ss or your trainer of choice
> L28: - **Privacy First**: Everything runs in your browser. API keys stay in your browser's local storage. Images are onl

## 星数曲线

```mermaid
xychart-beta
    title "vavo/TagPilot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-30 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `932050339014` · [字段定义](../../DATASET.md)*
