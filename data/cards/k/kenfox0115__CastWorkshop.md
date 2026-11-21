# kenfox0115/CastWorkshop

⭐ 9 · Python · Apache-2.0 · 推送 2026-11-11 · [GitHub](https://github.com/kenfox0115/CastWorkshop) · [官网](https://castworkshop.com) · 个人维护

**本地 AI 角色工作室：持久角色生成对话、图像与视频**

本地优先的角色工作室，用于创建带个性、外观、语音与对话历史的持久化 AI 角色，并可生成多角色对话、图像与视频场景。本身不内置生成能力，通过单独安装的 Ollama（对话与媒体规划）和 ComfyUI（图像、MOSS 语音、MiniMax H3 说话视频工作流）提供本地生成；以 Flask+SQLite 队列调度长 GPU 任务。以源码分发（beta），无独立安装包，无内置登录/HTTPS，GPU 兼容性尚未验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 持久角色：档案、身份引用、语音与对话历史跨会话保留
- 多角色场景：双人图像/视频，含身份与语音引用、说话人处理
- 场景连续性：视觉锚点与从结尾帧续接视频
- 本地编排：Ollama 与 ComfyUI 由本地 Flask/SQLite 服务队列协调

## 适用场景

- 在本地机器上创建并维护一组可复用的 AI 角色
- 从同一角色连续生成对话、图像和视频场景
- 通过浏览器或可选 Telegram 机器人与角色互动

## 场景标签

`聊天机器人` `图像生成` `视频生成` `语音合成` · 领域:对话与助手

## 证据(README 行号)

> L7: CastWorkshop is a local-first character studio for creating persistent AI characters
> L11: Separately installed **Ollama** and **ComfyUI** services provide the underlying local
> L36: Ollama writes the conversation and plans media. ComfyUI runs the image workflows,

## 星数曲线

```mermaid
xychart-beta
    title "kenfox0115/CastWorkshop 星数(近 3 点)"
    x-axis ["2026-10-22", "2026-11-13", "2026-11-21"]
    y-axis "stars" 7 --> 10
    line [8, 9, 9]
```

2026-10-22 8 → 2026-11-21 9（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `d04663a87284` · [字段定义](../../DATASET.md)*
