# overcrash66/OpenTranslator

⭐ 18 · Python · NOASSERTION · 推送 2026-03-26 · [GitHub](https://github.com/overcrash66/OpenTranslator) · 个人维护

**带语音克隆的语音转语音/语音转文本翻译桌面工具**

支持 17 种语言互译的语音翻译器：将音频转写为文本并可合成为语音，附带语音克隆功能。运行模式分三种：在线模式（调用 Google 翻译 API，无需 API key）、全本地模式（使用本地 LLM）、混合模式。文件菜单提供 MP3 转换、从视频提取音频、YouTube 下载、替换视频音轨、录音等辅助功能。以 Python 脚本仓库形式提供，需 Python 3.10+、FFmpeg（手动安装），本地模式另需安装 mecab，可选 CUDA 118 GPU 加速的 torch 版本；含 GUI 与 Gradio Web UI 两种入口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 17 种语言的语音转语音与语音转文本翻译
- 在线（Google 翻译，无需 API key）/本地 LLM/混合三种运行模式
- 语音克隆与录音、视频提音、YouTube 下载等音频工具菜单
- 提供 GUI 与基于 Gradio 的 Web UI（本地 LLM 模式）

## 适用场景

- 把外语音频或视频文件翻译成目标语言语音/文本
- 在无 API key 条件下用 Google 翻译做在线语音翻译
- 用本地 LLM 离线翻译音频文件

## 场景标签

`语音识别` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L1: # Open Translator: Speech To Speech and Speech to text Translator with voice cloning and other cool features
> L3: ## Or Fully Locally (using local LLM's)

## 星数曲线

```mermaid
xychart-beta
    title "overcrash66/OpenTranslator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `656522116e6d` · [字段定义](../../DATASET.md)*
