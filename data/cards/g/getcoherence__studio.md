# getcoherence/studio

⭐ 76 · TypeScript · MIT · 推送 2026-07-22 · [GitHub](https://github.com/getcoherence/studio) · [官网](https://studio.getcoherence.io) · 组织维护

**带 AI 编辑功能的开源录屏工具：自动字幕、智能剪辑、配音**

免费开源的屏幕录制与编辑桌面应用，由 Coherence 团队开发，fork 自 Siddharth Vaddem 的 OpenScreen。录制时使用 macOS ScreenCaptureKit / Windows WGC 原生捕获；AI 功能包括基于 Whisper 的自动字幕、去除空段与加载画面的智能剪辑、AI 生成配音旁白，另提供光标自动缩放、光标特效、背景自定义、标注、一键成片及导出 MP4/GIF。README 同时推广付费 Pro 版（13 个 AI agent 生成动态图形视频）。通过 GitHub Releases 下载安装包，macOS 需手动 xattr 去隔离，Linux 提供 AppImage。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Whisper 的自动字幕生成
- 智能剪辑：自动去除空段与加载画面
- AI 自动配音旁白
- 原生屏幕捕获（ScreenCaptureKit / WGC）与导出 MP4/GIF

## 适用场景

- 录制并快速产出带字幕的演示或教程视频
- 自动清理录屏中的停顿与加载片段
- 为视频生成 AI 配音旁白

## 场景标签

`视频生成` `语音识别` · 领域:内容生成

## 证据(README 行号)

> L11: Coherence Studio is a free, open-source screen recorder with AI-powered editing. Record your screen, and let AI han
> L23: - AI-powered auto-captions (Whisper)

## 星数曲线

```mermaid
xychart-beta
    title "getcoherence/studio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 75 --> 77
    line [76, 76]
```

2026-10-18 76 → 2026-10-24 76（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `bad065f952fb` · [字段定义](../../DATASET.md)*
