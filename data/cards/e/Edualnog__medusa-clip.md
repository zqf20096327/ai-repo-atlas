# Edualnog/medusa-clip

⭐ 24 · Python · AGPL-3.0 · 推送 2026-06-23 · [GitHub](https://github.com/Edualnog/medusa-clip) · [官网](https://medusaclip.com) · 个人维护

**本地运行的游戏高光切片工具：长视频自动生成 9:16 竖屏短剪辑**

面向游戏内容创作者的桌面应用（Electron + Python 引擎）：读取本地视频或公开链接，结合音频、动作与画面分析识别 clutch/fail/高光片段，自动生成 9:16 竖屏剪辑，附带标题 hook、逐字卡拉OK字幕与自动构图（facecam+游戏画面或聚焦动作两种布局）。视频全程本地处理，无注册无服务器，AI 调用使用用户自有 API key（OpenRouter/OpenAI/Anthropic），费用直接付给提供商。安装包自带引擎与 ffmpeg，无需另装依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 结合音频/动作/画面的游戏切片识别（clutch、fail、高光、反应）
- 自动生成 hook 标题、逐字卡拉OK字幕与双布局自动构图
- 100% 本地处理，无注册，BYO key（OpenRouter/OpenAI/Anthropic）
- macOS/Windows/Linux 安装包自带引擎与 ffmpeg，无需安装 Python

## 适用场景

- 把长游戏录像批量转成 TikTok/Reels/Shorts 竖屏短视频
- 不想上传视频到云端的本地剪辑处理
- 用自己的 API key 低成本生成游戏高光剪辑

## 场景标签

`语音识别` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L18: O **Medusa Clip** transforma gameplays longos em clipes verticais 9:16 prontos pra
> L19: TikTok, Reels e YouTube Shorts. O motor é **especializado em gameplay**: combina áudio,
> L31: - **🔑 Sua chave de IA (BYO key)** — OpenRouter, OpenAI ou Anthropic; você paga centavos direto ao provedor.

## 星数曲线

```mermaid
xychart-beta
    title "Edualnog/medusa-clip 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `35bd525767a9` · [字段定义](../../DATASET.md)*
