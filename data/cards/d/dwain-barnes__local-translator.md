# dwain-barnes/local-translator

⭐ 37 · HTML · 推送 2026-07-21 · [GitHub](https://github.com/dwain-barnes/local-translator) · 个人维护

**本地离线翻译应用：Ollama+translateGemma 翻译 55 种语言**

单 HTML 文件的浏览器翻译应用：通过本地 Ollama 运行 Google translateGemma 模型（4B/12B/27B），支持 55 种语言，可翻译文本及 PDF、Word、图片文件，扫描版 PDF 走视觉模型逐页处理（限前 20 页）。所有处理在本地完成，无需联网与外部服务器；使用前需安装 Ollama 并拉取模型，设置 OLLAMA_ORIGINS 解决 CORS 或用本地 web 服务器打开。文档解析依赖 pdf.js 与 mammoth.js。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单 HTML 文件即可运行，通过 Ollama REST API 调用 translateGemma（4B/12B/27B）
- 支持 PDF/Word/图片文本提取与翻译，扫描 PDF 自动转视觉逐页处理
- 55 种语言，全程本地运行，无遥测与云服务

## 适用场景

- 翻译涉密或隐私敏感文档而不经过云服务
- 无网络环境下离线翻译文档与图片文字
- 对照不同模型规格（4B/12B/27B）选择速度与质量的平衡

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L9: A private, local AI-powered translation application that runs entirely on your computer. Translate text, documents, 
> L70: 1. **Local AI Processing** - Uses Google's translateGemma model via Ollama
> L81: - **APIs Used**: Ollama REST API

## 星数曲线

```mermaid
xychart-beta
    title "dwain-barnes/local-translator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-30 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `81dbfa398792` · [字段定义](../../DATASET.md)*
