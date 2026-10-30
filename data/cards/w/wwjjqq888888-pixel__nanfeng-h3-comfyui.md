# wwjjqq888888-pixel/nanfeng-h3-comfyui

⭐ 30 · Python · 推送 2026-09-01 · [GitHub](https://github.com/wwjjqq888888-pixel/nanfeng-h3-comfyui) · 个人维护 · 中文 README

**MiniMax H3 的 ComfyUI 一体化节点：多参考、分镜与音频驱动**

非官方的 ComfyUI 自定义节点（NanFengH3MultiReferenceGeneratorV10），为 MiniMax H3 视频生成把模型、LoRA、图片/视频/音频参考、分段提示词、Sigma 与一采/二采参数收进单块节点界面。功能包括智能分镜（视觉/文本模型独立配置）、音频驱动的分段裁切与凭据隔离、NativeAudioLock 音频锁定、Sigma 预设持久化与可移植的节点目录相对路径。不含模型权重，需用户自行搭建 ComfyUI + MiniMax H3 环境并配置 API。节点 UI 中文优先，暂无完整语言切换。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一节点组织图片/视频/音频参考与分段提示词
- 智能分镜：视觉与文本模型独立配置，结果追加不覆盖
- 音频驱动分段与 NativeAudioLock 精确源音频区间
- 共享 ModelPatcher、动态 LoRA 链与独立一采 Sigma 的连续一采/二采

## 适用场景

- 在 ComfyUI 中用多参考素材生成 MiniMax H3 视频
- 按音频驱动自动切分分镜并逐段生成
- 复用 Sigma 预设与恒定触发词管理长分段生成

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L3: > **一个节点，串起多参考素材、智能分镜、音频驱动与连续二采。** 这是我为 MiniMax H3 制作的非官方 ComfyUI 一体化工作台：把原本分散的模型、LoRA、参考图/视频/音频、提示词分段、Sigma 与二采参数收进
> L37: - 节点 ID：`NanFengH3MultiReferenceGeneratorV10`
> L147: No model weights, generated media, live credentials, vision-analysis cache, bytecode, or test cache are included. 

## 星数曲线

```mermaid
xychart-beta
    title "wwjjqq888888-pixel/nanfeng-h3-comfyui 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-30 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `013299582048` · [字段定义](../../DATASET.md)*
