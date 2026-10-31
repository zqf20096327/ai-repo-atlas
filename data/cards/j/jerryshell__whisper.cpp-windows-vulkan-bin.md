# jerryshell/whisper.cpp-windows-vulkan-bin

⭐ 25 · 推送 2026-06-28 · [GitHub](https://github.com/jerryshell/whisper.cpp-windows-vulkan-bin) · 个人维护

**whisper.cpp 的 Windows Vulkan GPU 预编译二进制发布**

提供 whisper.cpp 在 Windows 上带 Vulkan GPU 支持的预编译二进制，用户从 Releases 页面下载 zip 即可运行，无需自行编译。README 给出两个使用示例：将文件复制到 Subtitle Edit v4.x 目录以集成字幕编辑器，以及用 yt-dlp 下载、ffmpeg 提取重采样音频后，用 whisper-cli 加载 ggml 量化模型生成 SRT 字幕；另支持 --vad 语音活动检测（配合 whisper-vad 模型）。更多用法指向上游 ggml-org/whisper.cpp。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Windows 平台 Vulkan GPU 支持的预编译二进制
- Subtitle Edit v4.x 集成示例
- YouTube 视频下载→音频提取→whisper-cli 转写生成 SRT 的完整命令示例
- 支持 --vad 语音活动检测转写

## 适用场景

- 在 AMD 等 Vulkan GPU 上免编译运行 whisper.cpp 语音转文字
- 给 Subtitle Edit 字幕编辑器添加本地 whisper 转写后端
- 为 YouTube 视频离线生成 SRT 字幕

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L1: # whisper.cpp Windows binary w/ Vulkan GPU support
> L38: ./whisper-cli \

## 星数曲线

```mermaid
xychart-beta
    title "jerryshell/whisper.cpp-windows-vulkan-bin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-31 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `f4ecf49d39d3` · [字段定义](../../DATASET.md)*
