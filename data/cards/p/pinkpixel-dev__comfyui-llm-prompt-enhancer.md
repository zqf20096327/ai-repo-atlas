# pinkpixel-dev/comfyui-llm-prompt-enhancer

⭐ 24 · Python · MIT · 推送 2026-08-16 · [GitHub](https://github.com/pinkpixel-dev/comfyui-llm-prompt-enhancer) · [官网](https://pinkpixel.dev) · 组织维护

**用 LLM 在 CLIP 编码前改写提示词的 ComfyUI 自定义节点**

ComfyUI 自定义节点：接收 CLIP 输入与用户简短提示词，调用 LLM 按选定风格改写后输出 conditioning 与增强文本，可直接接入现有工作流。支持 OpenAI、Anthropic、Google、OpenRouter 与本地 Ollama 五种提供方，每种可单独选模型；输出格式分 descriptive 与 tags（SDXL/Danbooru 风格标签），提供 9 类 47 种风格。API 调用失败时回退原始提示词。安装方式为克隆仓库到 custom_nodes 并 pip 安装各提供方 SDK（可选）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五种提供方含 OpenRouter 与本地 Ollama（无需 API key）
- 47 种风格、9 个类别，输出 descriptive 或 tags 两种格式
- API 失败时回退原始提示词，不中断运行
- 各提供方可独立选模型，缺失 SDK 包不影响其他提供方

## 适用场景

- 在 ComfyUI 工作流中把简短提示词扩写为带风格细节的完整提示词
- 用本地 Ollama 模型离线增强提示词，不发送到外部 API
- 为 SDXL/Flux 生成 Danbooru 风格标签格式的提示词

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: A ComfyUI node that rewrites your prompt with an LLM before it reaches the CLIP encoder. You type something short, p
> L9: - **Five providers**: OpenAI, Anthropic, Google, OpenRouter, and Ollama for local models

## 星数曲线

```mermaid
xychart-beta
    title "pinkpixel-dev/comfyui-llm-prompt-enhancer 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-31 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `3a6c09a78060` · [字段定义](../../DATASET.md)*
