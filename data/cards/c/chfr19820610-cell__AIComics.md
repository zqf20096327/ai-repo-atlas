# chfr19820610-cell/AIComics

⭐ 25 · Python · Apache-2.0 · 推送 2026-09-26 · [GitHub](https://github.com/chfr19820610-cell/AIComics) · [官网](https://chfr1982.gumroad.com) · 个人维护 · 中文 README

**全本地运行的 AI 漫剧自动生成系统：故事到成片发布一站式**

面向一人创作者的 AI 漫剧（donghua）生产系统，覆盖写剧本、小说导入、ComfyUI+SDXL 生成关键帧与角色四视图、多语言 TTS 配音与字幕、多模型视频路由（Kling/Seedance/Wan）、2D/2.5D/3D 三线渲染、质量门（Drift Gate、伪影检测、沉默失败检测、成本预算门禁）与多平台发布（国内三平台+YouTube/TikTok/Instagram）。提供 CLI、FastAPI Web API（17 端点）、Electron 桌面端与 Docker 部署。运行依赖 Python 3.12+、ComfyUI、Piper TTS、FFmpeg、Node.js 20+。README 同页推广 Gumroad 付费产品（成片/工具包/手册）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 故事/小说→分镜→生图→配音→视频→发布的完整管线，v5.2 共 1357 测试通过
- Drift Gate 画面防偏移 + 跨集角色一致性检查（Triple-Lock）
- 多模型视频路由（动作→Kling/对话→Seedance/远景→Wan）与 2D/2.5D/3D 三线渲染
- 7-agent Director 编排管线 + 成本仪表盘与预算门禁，支持 Docker 一键部署

## 适用场景

- 独立创作者从故事文本批量产出带配音字幕的漫剧视频
- 将小说拆分为整季分镜并自动生成成片
- 把成品一键发布到抖音/小红书/B站及 YouTube 等平台

## 场景标签

`图像生成` `视频生成` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L80: AIComics 是一个**全本地运行**的 AI 漫剧创作系统。v5.1 已支持从故事到发布的完整管线 + MLLM 智能层 + 质量控制闭环 + Agent 架构：
> L84: |📝 **写剧本**|设定世界观、角色、剧情，自动生成分镜脚本|大语言模型|
> L90: |🎬 **做视频**|多模型路由（动作→Kling/对话→Seedance/远景→Wan）+ FLF插值|`VideoRouter` + FFmpeg|
> L91: |📡 **发平台**|YouTube/TikTok/Instagram + 小红书/B站/抖音|`international.py` + social-auto-upload|

## 星数曲线

```mermaid
xychart-beta
    title "chfr19820610-cell/AIComics 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-29"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-29 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `8644be3d6a95` · [字段定义](../../DATASET.md)*
