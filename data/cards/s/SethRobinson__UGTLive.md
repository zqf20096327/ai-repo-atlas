# SethRobinson/UGTLive

⭐ 117 · C# · NOASSERTION · 推送 2026-09-03 · [GitHub](https://github.com/SethRobinson/UGTLive) · 个人维护

**Windows 实时屏幕翻译工具：OCR 加 LLM 翻译游戏漫画**

面向玩家、漫画读者与语言学习者的 Windows GUI 工具，通过矩形选区捕获屏幕，用 GPU 加速 OCR（EasyOCR/MangaOCR/PaddleOCR/docTR/Windows OCR/Google Cloud Vision）识别文本，再经 LLM 翻译为 26 种语言之一并覆盖显示，支持手柄热键、颜色检测替换原文、语音朗读与 PDF/CBZ 批量转换。翻译可走云端 API（OpenAI/Gemini/OpenRouter/Anthropic 等），也可用本机 llama.cpp 或 Ollama 完全本地运行。限制：要求 Windows 与 8GB+ 显存的 NVIDIA RTX 20/30/40/50 系显卡，AMD 暂不支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实时屏幕捕获 + GPU OCR + LLM 翻译，支持 26 种语言
- 翻译与语音可经本地 llama.cpp / Ollama / Qwen-TTS 完全离线运行
- 竖排日文漫画识别、朗读与 PDF/CBZ 批量转换
- GPU Service Console 一键安装各后端服务

## 适用场景

- 游玩日文游戏时实时翻译屏幕文本
- 阅读竖排日文漫画并跟读学日语
- 把漫画 PDF/CBZ 批量转成翻译版本
- 用 OpenAI 实时接口给语音对话加字幕并翻译

## 场景标签

`OCR` · 领域:感知与多模态

## 证据(README 行号)

> L21: An easy-to-use GUI-based Windows tool that performs "live" translations of anything on the screen using modern mach
> L31: * Out of the box you can do local GPU accelerated OCR (Easy OCR, Manga OCR, Paddle OCR, docTR, Windows OCR, Google 
> L32: * Optional features (translation, speech) enabled locally with llama.cpp, Ollama and Qwen-TTS support. Or go higher

## 星数曲线

```mermaid
xychart-beta
    title "SethRobinson/UGTLive 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23"]
    y-axis "stars" 116 --> 119
    line [118, 117, 117]
```

2026-10-18 118 → 2026-10-23 117（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `ab31e5c84e19` · [字段定义](../../DATASET.md)*
