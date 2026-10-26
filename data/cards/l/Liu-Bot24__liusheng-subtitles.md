# Liu-Bot24/liusheng-subtitles

⭐ 60 · JavaScript · MIT · 推送 2026-09-01 · [GitHub](https://github.com/Liu-Bot24/liusheng-subtitles) · [官网](https://blog.liu-qi.cn/tools) · 个人维护 · 中文 README

**为网页视频生成与翻译字幕的 Chrome 扩展（ASR+LLM）**

流声字幕是一款 Chrome 扩展，面向没有字幕、字幕缺失或需翻译外语内容的流媒体视频、动漫、课程、访谈和直播回放。自动发现网页视频来源，用户选择识别服务与翻译模型后生成原文、译文或双语字幕并叠加到播放器，支持逐条编辑、时间轴校正、SRT/VTT/ASS 导入导出与本地缓存。识别支持 OpenAI Whisper、Groq Whisper、xAI Grok、Fun-ASR 与自定义接口，翻译支持 OpenAI/Anthropic 兼容接口。0.1.6 将长任务迁移到持久化 offscreen 执行链路。部分加密或跨域受限的视频来源可能无法处理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动发现网页视频来源，生成原文/译文/双语三种字幕
- 识别支持 OpenAI Whisper、Groq Whisper、xAI Grok、Fun-ASR 与自定义接口
- 翻译支持 OpenAI-compatible、Anthropic-compatible 接口
- 字幕逐条编辑、时间轴校正、SRT/VTT/ASS 导入与本地缓存

## 适用场景

- 给无字幕或字幕缺失的流媒体视频配字幕
- 把外语课程、访谈或影视翻译成目标语言
- 生成双语字幕并导出 SRT 文件

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L9: 流声字幕是一款 Chrome 扩展，用来给网页视频生成字幕并翻译。适合没有字幕、字幕缺失，或需要把外语内容翻译成所选目标语言的流媒体影视、动漫、课程、访谈和直播回放。
> L11: 打开视频页面后，流声字幕会在侧边栏中显示可处理的视频来源。用户选择识别服务和翻译模型后，就可以生成原文字幕、译文字幕或双语字幕，并把字幕显示到网页播放器上。

## 星数曲线

```mermaid
xychart-beta
    title "Liu-Bot24/liusheng-subtitles 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 59 --> 61
    line [60, 60]
```

2026-10-18 60 → 2026-10-26 60（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d9df27dcc850` · [字段定义](../../DATASET.md)*
