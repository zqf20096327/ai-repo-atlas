# SUP3RMASS1VE/Suno-Song-Remaster

⭐ 127 · JavaScript · 推送 2026-07-10 · [GitHub](https://github.com/SUP3RMASS1VE/Suno-Song-Remaster) · 个人维护

**桌面音频母带处理应用：把 AI 生成音乐处理到流媒体响度标准**

基于 Electron + Vite 的桌面应用，面向 AI 生成音乐（如 Suno 产出）的母带处理：提供批处理队列、响度归一化（-20 至 -6 LUFS，ITU-R BS.1770-4）、4 倍过采样真峰值限制（dBTP）、五段 EQ、立体声宽度、Center Bass、迷你 DAW 音频编辑器（淡入淡出/裁剪/撤销）与实时试听，导出 WAV（44.1/48kHz、16/24 位）并嵌入元数据。音频处理为纯 JavaScript 实现（不依赖 FFmpeg）。Windows/macOS/Linux 提供安装包，macOS 构建未签名需手动放行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ITU-R BS.1770-4 LUFS 响度归一化与 4x 过采样真峰值限制
- 批处理队列与逐文件元数据编辑，一键批量导出 WAV
- 迷你 DAW 编辑器：波形选择、淡入淡出、裁剪、撤销/重做
- 纯 JavaScript 音频处理与 Web Audio API 实时试听，不依赖 FFmpeg

## 适用场景

- 我把 Suno 等 AI 生成的歌曲做母带处理并调整到流媒体响度标准
- 批量处理多首 AI 音乐并补齐标题/作者等元数据后导出 WAV
- 导出前实时试听 EQ 和响度效果并做剪辑微调

## 场景标签

 · 领域:音频工具/桌面应用

## 证据(README 行号)

> L3: A professional desktop app for mastering AI-generated music to streaming-ready quality.
> L81: - Pure JavaScript audio processing (no FFmpeg)

## 星数曲线

```mermaid
xychart-beta
    title "SUP3RMASS1VE/Suno-Song-Remaster 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 123 --> 126
    line [124, 125, 125]
```

2026-10-18 124 → 2026-10-24 125（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `29cbb2093a4e` · [字段定义](../../DATASET.md)*
