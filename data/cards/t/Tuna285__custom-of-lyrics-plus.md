# Tuna285/custom-of-lyrics-plus

⭐ 16 · JavaScript · LGPL-2.1 · 推送 2026-10-25 · [GitHub](https://github.com/Tuna285/custom-of-lyrics-plus) · 个人维护 · 中文 README

**Spicetify 歌词插件：AI 翻译歌词并显示注音与视频背景**

基于 Lyrics Plus 重建的 Spicetify 自定义应用，为 Spotify 提供带翻译的歌词显示：通过 Google Gemini API 将歌词翻译为越南语/英语/日语/韩语/中文/乌克兰语 6 种目标语言，支持 Furigana、Romaji、Pinyin 等注音显示，提供 6 种翻译语气、越南语人称代词模式、多 API Key 轮换与预翻译。另有本地注音模式（Kuromoji 等）与 YouTube 视频背景。以 PowerShell 一键脚本或手动复制到 Spicetify CustomApps 目录安装，需网络版 Spotify 与 Google AI Studio API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | LGPL-2.1 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Google Gemini API 歌词翻译，支持 6 种目标语言
- Furigana/Romaji/Romaja/Pinyin 注音双显示模式
- 多 API Key 轮换与配额故障转移、预翻译下一曲目
- YouTube 视频背景（跳过广告、影院模式）

## 适用场景

- 在 Spotify 听歌时查看带母语翻译的歌词
- 学日语/韩语/中文时同时看注音与原文
- 为歌词页添加音乐视频背景

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L10: > A personalized version of **Lyrics Plus** for Spicetify, rebuilt to focus on high-quality lyric translation, phon
> L19: Connects to Google Gemini API to translate lyrics naturally and accurately.

## 星数曲线

```mermaid
xychart-beta
    title "Tuna285/custom-of-lyrics-plus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `d454f629fe56` · [字段定义](../../DATASET.md)*
