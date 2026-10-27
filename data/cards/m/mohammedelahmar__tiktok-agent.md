# mohammedelahmar/tiktok-agent

⭐ 31 · Python · MIT · 推送 2026-02-23 · [GitHub](https://github.com/mohammedelahmar/tiktok-agent) · 个人维护

**AI 自动从长视频中截取热门片段并转成竖屏短视频**

面向内容创作者的视频再利用工具：通过运动评分与场景分析自动识别长视频中最具吸引力的片段，裁剪为 9:16 竖屏格式并输出 MP4，支持水印、YouTube URL 或本地文件输入、逐帧修剪剪辑。可选接入 Google Gemini API 生成标题、描述与标签。AI 元数据功能需自备 API key，FFmpeg 需手动安装并加入 PATH。提供 Web 界面（React+FastAPI）与 CLI 两种使用方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 运动评分与场景分析自动识别候选片段
- 9:16 竖屏自动转换（裁剪/背景模糊/黑边模式）
- Google Gemini 生成标题、描述与标签（可选）
- Web UI 逐帧修剪与批量渲染，另提供 CLI

## 适用场景

- 把长视频转成 TikTok/Shorts/Reels 竖屏短视频
- 让 AI 挑选高吸引力的片段再人工微调导出
- 批量为短视频生成标题和标签

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: **TikTok Agent** is an advanced AI-powered tool that automatically extracts viral-worthy clips from long-form videos
> L9: * **🤖 AI Viral Detection**: Automatically identifies the most engaging segments using motion scoring and scene analy
> L14: * **📝 AI Metadata Generator**: Generates viral titles, descriptions, and hashtags using Google Gemini LLM.

## 星数曲线

```mermaid
xychart-beta
    title "mohammedelahmar/tiktok-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-27 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `100c0a055a81` · [字段定义](../../DATASET.md)*
