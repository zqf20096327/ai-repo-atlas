# SamurAIGPT/Text-To-Video-API

⭐ 30 · MIT · 推送 2026-08-02 · [GitHub](https://github.com/SamurAIGPT/Text-To-Video-API) · [官网](https://docs.vadoo.tv) · 组织维护

**文本生成短视频的 API 文档仓库：调用生成 TikTok/Shorts 风格视频**

Vadoo Text-to-Video API 的使用文档仓库：通过一个 POST 端点，传入主题、AI 配音、视觉主题、语言与时长（如 30-60s）等参数，生成面向 TikTok、YouTube Shorts、Instagram Reels 的短视频；生成结果通过预配置的 webhook 回调返回视频下载 URL，需在官网注册获取 API key。示例以 Python requests 调用，完整选项（声音/主题/语言）见外部文档站，另提供网页版无代码入口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单端点 POST API，支持主题、配音、主题风格、语言、时长参数
- Webhook 回调投递生成的视频下载 URL
- 支持多语言与多种 AI 配音选择
- 提供无代码网页版使用入口

## 适用场景

- 为 TikTok/YouTube Shorts/Instagram Reels 批量生成短视频内容
- 生成产品演示、教程类营销短视频
- 在自有应用中集成文本转视频能力

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L7: Generate AI videos from text with a simple API call. Create engaging short-form content for TikTok, YouTube Shorts, 
> L51: POST https://viralapi.vadoo.tv/api/generate_video
> L79: The download URL will be sent to your configured webhook.

## 星数曲线

```mermaid
xychart-beta
    title "SamurAIGPT/Text-To-Video-API 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-28 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 low · 依据 README sha `c13ec7e72b56` · [字段定义](../../DATASET.md)*
