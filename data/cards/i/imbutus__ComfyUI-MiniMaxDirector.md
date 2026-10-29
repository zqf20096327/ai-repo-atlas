# imbutus/ComfyUI-MiniMaxDirector

⭐ 68 · JavaScript · MIT · 推送 2026-09-16 · [GitHub](https://github.com/imbutus/ComfyUI-MiniMaxDirector) · 个人维护 · 中文 README

**ComfyUI 时间轴导演插件：为 MiniMax H3 视频模型编排镜头并编译结构化提示词**

面向 ComfyUI 用户的 MiniMax H3 视频模型自定义节点包：在时间轴上排布镜头、运镜与音频提示，编译为 H3 文本编码器读取的结构化提示词，并输出 conditioning、合法帧数的 latent 与 lint 报告。覆盖官方提示词指南的完整运镜词汇、旁白、跨切对话、屏幕文字与故事板引用；提供 WHO & WHAT 卡片管理角色/道具/场景资产。附带完整工作流（含采样器、双 VAE 解码、视频输出、Turbo 加速与可选 Upscale 阶段）。核心为纯 Python 编译器，无 ComfyUI 之外依赖，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 时间轴镜头/运镜/音频提示编译为 H3 结构化提示词，每次编辑暂停即编译并 lint
- 帧点阵约束（length % 17 == 5 @24fps）在编辑时自动吸附
- WHO & WHAT 卡片统一管理人脸、声音、参考资产，支持换脸与动作/音色迁移
- 随附完整工作流：加载器、双 VAE 解码、Turbo 四步采样与可选 latent 放大

## 适用场景

- 在 ComfyUI 中按时间轴编排多镜头视频并生成带音频的成片
- 用参考图/视频驱动 MiniMax H3 的图生视频与参考生视频
- 草稿用 Turbo 四步 LoRA 快速迭代，正式渲染再关掉

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L3: A timeline director for the MiniMax H3
> L105: |`MiniMax Director`|Timeline editor; outputs `positive`, `latent`, the compiled `prompt`, and a lint `report`.|

## 星数曲线

```mermaid
xychart-beta
    title "imbutus/ComfyUI-MiniMaxDirector 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26", "2026-10-29"]
    y-axis "stars" 65 --> 69
    line [66, 67, 68, 68]
```

2026-10-18 66 → 2026-10-29 68（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `e0d99b70b2ac` · [字段定义](../../DATASET.md)*
