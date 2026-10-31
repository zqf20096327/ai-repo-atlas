# heartleo/subtrans

⭐ 19 · Go · MIT · 推送 2026-05-11 · [GitHub](https://github.com/heartleo/subtrans) · 个人维护 · 中文 README

**用 OpenAI 兼容 API 翻译字幕文件的 Go 工具**

读取 SRT/VTT/ASS/LRC/SBV 五种字幕格式，通过 OpenAI 兼容 API 完成翻译，支持按句子边界智能分批、缺失/合并自动重试、自定义指令与提示词、原文与译文双语输出。以命令行工具、Go 库和 HTTP API（含 SSE 流式输出）三种形式提供，可用 Homebrew、curl 脚本、go install 安装或从源码编译。适用于需要批量本地化字幕文件的开发者和视频创作者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 SRT/VTT/ASS/LRC/SBV 五种字幕格式的读取与翻译
- 按句子边界智能分批与翻译缺失/合并自动重试
- 可作为命令行工具、Go 库、HTTP API（SSE 流式）使用
- 支持自定义翻译指令与提示词、双语输出

## 适用场景

- 把外语字幕批量翻译成中文等目标语言
- 在程序中通过 Go 库或 HTTP API 集成字幕翻译
- 生成原文与译文对照的双语字幕文件

## 场景标签

 · 领域:视频/字幕翻译工具

## 证据(README 行号)

> L3: ***使用 OpenAI API 翻译字幕文件（SRT / VTT / ASS / LRC / SBV）***
> L17: - 支持 OpenAI 兼容 API
> L22: - 支持作为 **命令行工具**、**Go 库** 使用

## 星数曲线

```mermaid
xychart-beta
    title "heartleo/subtrans 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `2cfd3e41b463` · [字段定义](../../DATASET.md)*
