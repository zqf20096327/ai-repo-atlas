# sengseng123/aix-drama-factory

⭐ 13 · Python · AGPL-3.0 · 推送 2026-09-15 · [GitHub](https://github.com/sengseng123/aix-drama-factory) · 个人维护 · 中文 README

**本地 AI 短剧生产 Web 工作台，串联剧本到成片全流程**

基于 Python/Flask 后端与 Web 前端的本地优先短剧生产工作台：覆盖故事、大纲、剧本、角色/场景资产、MiniMax H3 提示词、ComfyUI 图片与视频生成、断点恢复和成片整理的分阶段流程。支持 managed 托管与 external 外部服务两种运行模式，设置页可扫描选择本地 GGUF 大语言模型与 ComfyUI 视频模型，内置 Qwen Image 2512 生图适配器。自动故事/剧本功能需 OpenAI 兼容 LLM，运行依赖用户自备的 ComfyUI、H3 模型与 FFmpeg，仓库不含运行环境与模型权重。当前为 v2.0.0-dev.12 开发预览版，以 AGPL-3.0-only 授权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 故事→剧本→资产→H3 提示词→图片/视频→成片的分阶段流水线
- 断点恢复、失败片段单独重试与服务重启后状态恢复
- managed/external 双运行模式，外部模式不动用户已有 ComfyUI/Qwen
- 设置页扫描选择本地 GGUF LLM 与 ComfyUI 视频 UNET 模型

## 适用场景

- 在本地把剧本流程化生成 AI 短剧成片
- 复用已有 ComfyUI 环境组织视频生成队列
- 生成失败后从断点继续而不重做成功片段

## 场景标签

`视频生成` `图像生成` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: AIX 短剧工厂是面向本地 AI 视频生产的 Web 工作台，把故事/剧本、角色与场景资产、MiniMax H3 提示词、ComfyUI 生成、断点恢复和成片整理放在同一套流程中。
> L31: - 通用 V2 分阶段生产：故事、大纲、剧本、资产、H3 提示词、图片/视频和成片整理。

## 星数曲线

```mermaid
xychart-beta
    title "sengseng123/aix-drama-factory 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24", "2026-10-28", "2026-10-31"]
    y-axis "stars" 9 --> 14
    line [10, 11, 12, 13, 13]
```

2026-10-18 10 → 2026-10-31 13（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `b569643c5fab` · [字段定义](../../DATASET.md)*
