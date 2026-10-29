# pixelpainter/comfyui-AI-prompt-editor

⭐ 29 · JavaScript · GPL-3.0 · 推送 2026-09-01 · [GitHub](https://github.com/pixelpainter/comfyui-AI-prompt-editor) · [官网](https://registry.comfy.org/nodes/comfyui-ai-prompt-editor) · 个人维护

**ComfyUI 提示词编辑节点：本地 Ollama 驱动的 AI 提示词写作室**

单个 ComfyUI 自定义节点，将提示词文本框替换为完整写作环境：多标签编辑器（最多 10 个，含撤销/历史/查找替换/清洗）、AI 变换（Enhance 扩写、Variations 三种风格变体、Inverter 反向改写）、自然语言 Instruct edit 连锁改写并保持上下文线程、图/视频转提示词（需视觉模型）、8 种风格目标与 6 滑块调校、浏览 Civitai 与 Genur.art 提示词库，以及无线注入目标文本组件。AI 功能全部由本地 Ollama 模型驱动，无云端 API 与密钥；节点本身无输入输出端口，通过 wireless targets 注入。须经 ComfyUI Manager、comfy CLI 或 git 手动安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 变换：Enhance/Variations/Inverter/自然语言 Instruct edit（连锁改写与方向线程）
- 8 种风格目标与 6 个滑块调整 AI 美学词汇
- 无线目标：运行时将提示词注入工作流中任意文本组件，无需连线
- 全部 AI 功能由本地 Ollama 运行，无云端 API、无密钥

## 适用场景

- 在 ComfyUI 里把粗略想法扩写成适配 Flux/Qwen-Image 等编码器的扩散提示词
- 用自然语言连锁修改提示词并保持语义一致
- 浏览 Civitai/Genur.art 提示词库并一键使用或再变换

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L9: **A full prompt-writing studio inside a single ComfyUI node** — AI-powered editing, style targeting,
> L10: prompt browsing, and wireless prompt injection, all driven by your local Ollama models.
> L17: EPE replaces the humble prompt textbox with a complete writing environment. Write a rough idea, and your local LLM 

## 星数曲线

```mermaid
xychart-beta
    title "pixelpainter/comfyui-AI-prompt-editor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-29 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `1b1565108213` · [字段定义](../../DATASET.md)*
