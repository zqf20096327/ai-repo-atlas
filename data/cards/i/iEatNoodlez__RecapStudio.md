# iEatNoodlez/RecapStudio

⭐ 3 · Python · MIT · 推送 2026-11-15 · [GitHub](https://github.com/iEatNoodlez/RecapStudio) · 个人维护

**在本机把漫画/条漫自动转成带旁白解说的回顾视频**

面向个人创作者的桌面应用（Windows/Linux，含服务器版）：导入章节图片/.cbz 后一键运行流水线——OpenCV 切分面板、RapidOCR/PP-OCRv5 读台词、识别角色归属、由脚本写作器逐章生成旁白，再经 Kokoro 或微软 Edge/ElevenLabs 配音，最终渲染含字幕、YouTube 标题与缩略图的视频。本地模型（Ollama）与 Kokoro 免费离线，在线服务需自备 API key（用 Claude 每章约 1–40 美分）。NVIDIA GPU 可加速 OCR 与语音。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 端到端流水线：切面板→OCR→角色归属→旁白→配音→渲染字幕视频
- 脚本写作器支持 Ollama 本地模型及 Claude、Gemini、OpenRouter、DeepSeek、Groq、Mistral 等在线后端
- Kokoro 本地配音，或微软 Edge 语音、ElevenLabs、自录音频
- 提供 Lite 与 Full Suite 两种版本及 Docker/NAS 服务器部署形态

## 适用场景

- 把自己追的漫画章节做成带旁白的回顾视频
- 在 NAS 或迷你 PC 上以浏览器远程跑回顾项目
- 为 YouTube/TikTok 生成带标题建议与缩略图的投稿素材

## 场景标签

`语音合成` `OCR` `AI 写作` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L22: Add the chapters, press **Make the recap**, and Recap Studio cuts the pages into panels, reads the text, works out 
> L89: |Script|Writes the narration a chapter at a time, from the pictures and the text.|A local model (Ollama), Claude Co


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `a8dd0db8d1e3` · [字段定义](../../DATASET.md)*
