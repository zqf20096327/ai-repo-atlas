# Andro-Meta/ComfyUI-Krea-Moodboards

⭐ 20 · Python · MIT · 推送 2026-08-07 · [GitHub](https://github.com/Andro-Meta/ComfyUI-Krea-Moodboards) · 个人维护

**给 ComfyUI 用户的 Krea 风格情绪板提示词搜索与应用节点包**

非官方的 ComfyUI 自定义节点包，内置 3549 个 Krea 公开情绪板风格提示词（含 60 个 Andro.Meta 策展条目），提供可视化缩略图浏览、关键词搜索、随机抽取、2-4 板混合（Mashup）与用户提示词合成（Apply）等节点，输出纯 STRING 文本供 Krea 2 工作流或 Qwen3-VL 文本编码器使用。节点不加载模型、不修改采样器，仅操作提示词层；另附可直接加载的 Krea 2 Turbo 示例工作流。通过 ComfyUI-Manager / Comfy Registry 或克隆到 custom_nodes 目录安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 3549 个 Krea 情绪板风格提示词目录（0.2.1 覆盖完整公开目录）
- 搜索为依赖无关的同义词感知加权搜索，支持标题/关键词/风格轴等多字段
- 风格描述重写为类型化 schema，仅描述渲染方式不注入主体，附 style-only 防护栏
- Mashup 节点可混合 2-4 个情绪板并去重风格轴与负面引导

## 适用场景

- 在 Krea 2 文生图工作流中按风格关键词查找并套用情绪板提示词
- 视觉浏览 Krea 情绪板缩略图后直接接入提示词管线
- 随机或混合多个风格探索图像视觉风格组合

## 场景标签

`提示工程` `图像生成` · 领域:Agent 开发

## 证据(README 行号)

> L3: Prompt-only Krea moodboard nodes for ComfyUI. This pack ships 3549 enriched Krea moodboard prompt styles and helps y
> L72: These nodes do not load Krea 2, patch the model, emit conditioning tensors, download images, or replace the sampler

## 星数曲线

```mermaid
xychart-beta
    title "Andro-Meta/ComfyUI-Krea-Moodboards 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `3f9f26986081` · [字段定义](../../DATASET.md)*
