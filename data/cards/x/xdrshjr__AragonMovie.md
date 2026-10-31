# xdrshjr/AragonMovie

⭐ 16 · Python · 推送 2026-10-22 · [GitHub](https://github.com/xdrshjr/AragonMovie) · 个人维护 · 中文 README

**多Agent架构的AI短剧自动生成工具，剧本转完整视频**

基于Python和多Agent架构的短剧生成系统：剧本解析生成分镜脚本，调用Nano Banana Pro生成图片，Veo3或Sora2（可配置切换）转视频片段，再自动合成。支持可选的LLM角色一致性判断（多候选图片并发评分选优，如Doubao多模态模型）。提供CLI与Web双界面（FastAPI+Next.js），另有Electron桌面端（免Python/Node/ffmpeg环境），以及REST API与OpenAI兼容API。断点续传、并发配置与进度监控均支持；图片/视频API按量计费。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 剧本→分镜图片→视频片段→合成的多Agent管道
- Veo3/Sora2 视频服务可配置切换，Sora2支持故事板多镜头模式
- LLM角色一致性判断：多候选图片并发评分选优
- CLI + Web（FastAPI/Next.js）+ Electron 桌面端三种使用方式，含OpenAI兼容API

## 适用场景

- 把写好的文字剧本自动生成完整短剧视频
- 批量生产短视频内容并断点续传
- 通过Web界面可视化配置和监控生成流程

## 场景标签

`多智能体` `视频生成` · 领域:Agent 开发

## 证据(README 行号)

> L8: - 🖼️ AI驱动的分镜图片生成（Nano Banana Pro）
> L9: - 🎥 图片到视频的智能转换（Veo3 / Sora2，可配置切换）
> L48: - **ImageGenerationAgent**: 调用Nano Banana Pro API生成分镜图片（支持多候选图片并发生成）

## 星数曲线

```mermaid
xychart-beta
    title "xdrshjr/AragonMovie 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b645f2010556` · [字段定义](../../DATASET.md)*
