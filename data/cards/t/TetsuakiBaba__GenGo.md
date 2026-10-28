# TetsuakiBaba/GenGo

⭐ 20 · Swift · 推送 2026-08-26 · [GitHub](https://github.com/TetsuakiBaba/GenGo) · [官网](https://tetsuakibaba.github.io/GenGo/) · 个人维护

**macOS 菜单栏本地 LLM 文本处理工具：划词翻译/改写/生成**

Swift/SwiftUI 原生 macOS 菜单栏应用：监听全局快捷键，捕获选中文本并交由 LLM 处理后原位替换，支持翻译、校对、改写与纯文本生成（最多 5 个预设提示词，默认日英互译）。LLM 提供方包括 LM Studio、Ollama、Apple Intelligence 与 OpenAI 兼容 API，可全部走本地模型。需授予 macOS 辅助功能权限以读取和回写选中文本；设置本地存储。提供 GitHub Releases 下载 dmg/zip，也可用 Swift Package Manager 从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 全局快捷键划词捕获并原位替换文本
- 支持 LM Studio、Ollama、Apple Intelligence、OpenAI 兼容 API 四类提供方
- 最多 5 个可自定义快捷键的预设提示词，默认日英互译
- 设置仅本地存储（Application Support/settings.json）

## 适用场景

- 在任意 macOS 应用中划词即时日英互译
- 用自定义提示词对选中文本做改写或校对
- 通过本地 LLM 完成文本处理，数据不出本机

## 场景标签

`AI 写作` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: **GenGo** is a native macOS app for processing selected text with Large Language Models. It lives in the menu bar, w
> L31: - **LM Studio**: choose from models loaded in LM Studio
> L32: - **Ollama**: choose local or cloud models from the Ollama catalog
> L33: - **Apple Intelligence**: available on supported macOS versions

## 星数曲线

```mermaid
xychart-beta
    title "TetsuakiBaba/GenGo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `26bdb99355c6` · [字段定义](../../DATASET.md)*
