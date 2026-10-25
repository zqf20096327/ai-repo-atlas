# Gyyyn/OpenWebTTS

⭐ 74 · JavaScript · MIT · 推送 2025-11-14 · [GitHub](https://github.com/Gyyyn/OpenWebTTS) · [官网](https://openwebtts.guyra.com.br/) · 个人维护

**本地自托管的 TTS 网页应用：用本地模型朗读 PDF/EPUB**

面向终端用户的自托管文本转语音 Web 应用：读取 PDF、EPUB 等文档及 URL，用本地 TTS 引擎生成语音朗读，无需订阅与联网跟踪。支持 Piper、Kokoro、Coqui（XTTS2）、Chatterbox（开发中）多种引擎，内置模型下载器；提供 10 秒 wav 语音克隆、无文本 PDF 的自动 OCR、自动跳过页眉页脚等文档处理功能。运行方式为克隆仓库、Python venv 装依赖并用 npm 构建，详见 BUILD.md。Coqui 部分仅支持 XTTS2。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 Piper/Kokoro/Coqui/Chatterbox 多引擎并内置模型下载器
- 10 秒 wav 文件即可语音克隆
- 无文本 PDF 自动 OCR 并跳过页眉页脚
- 离线优先、可自托管

## 适用场景

- 本地朗读 PDF/EPUB 等文档且不上传数据
- 用阅读障碍辅助工具收听文档内容
- 用自己的声音克隆配音朗读

## 场景标签

`语音合成` `OCR` · 领域:内容生成

## 证据(README 行号)

> L1: # OpenWebTTS: Local Text-to-Speech Web UI
> L7: OpenWebTTS is the open-source, privacy-first alternative to Speechify and ElevenLabs. Run it locally, use any TTS en
> L27: See `BUILD.md` for detailed instructions. If you know what you're doing: clone the repo, install Python dependencie

## 星数曲线

```mermaid
xychart-beta
    title "Gyyyn/OpenWebTTS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 73 --> 75
    line [74, 74]
```

2026-10-18 74 → 2026-10-25 74（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `522dd17c431c` · [字段定义](../../DATASET.md)*
