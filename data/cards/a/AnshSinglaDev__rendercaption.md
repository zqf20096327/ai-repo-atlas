# AnshSinglaDev/rendercaption

⭐ 16 · TypeScript · MIT · 推送 2026-07-16 · [GitHub](https://github.com/AnshSinglaDev/rendercaption) · [官网](https://github.com/AnshSinglaDev/rendercaption/releases/latest) · 个人维护

**离线语音转文字与字幕生成的桌面应用，支持25+语言**

基于 Tauri/Rust/React 的桌面应用，在本地对音频/视频文件生成字幕与转录文本，全程离线无需云端与 API key。通过内置 Model Manager 按需下载量化 GGUF 模型（IndicConformer、Parakeet 系列），也可放入自定义 .gguf 文件。采用 Vulkan GPU 与 AVX2 CPU 双引擎自动选择，音频按 30 秒分块并发处理，可导出 TXT/SRT。提供 Windows 安装包，源码构建需 Node.js、Rust 与 Tauri CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地离线转录，支持 25+ 语言含印地语、旁遮普语等南亚语言
- GGUF 模型按需下载，支持自定义本地 .gguf 模型
- Vulkan GPU / AVX2 CPU 双引擎自动选择，跨 NVIDIA/AMD/Intel
- 导出 TXT/SRT 字幕，带词级置信度热力图

## 适用场景

- 给视频制作 SRT 字幕文件且不上传音频到云端
- 处理印地语/旁遮普语等南亚语言的转录
- 低配机器上用 CPU 模式后台转录长音频

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L10:  RenderCaption is a one-click install desktop app that generates subtitles, captions, and transcriptions from any a
> L22: 1. Download the latest installer from the **Releases Page**.

## 星数曲线

```mermaid
xychart-beta
    title "AnshSinglaDev/rendercaption 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `1cc4c20a944e` · [字段定义](../../DATASET.md)*
