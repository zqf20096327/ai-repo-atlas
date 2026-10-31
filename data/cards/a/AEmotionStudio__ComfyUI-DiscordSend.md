# AEmotionStudio/ComfyUI-DiscordSend

⭐ 15 · Python · GPL-3.0 · 推送 2026-10-20 · [GitHub](https://github.com/AEmotionStudio/ComfyUI-DiscordSend) · [官网](https://aemotionstudio.org/) · 组织维护

**把 ComfyUI 生成的图像/视频经 webhook 直发 Discord 的扩展**

ComfyUI 自定义节点扩展，包含图像与视频两个节点：图像节点支持 PNG/JPEG/WebP 保存、批量分组（每条消息最多 9 张）、附带提示词与工作流 JSON；视频节点可将图像序列转为 GIF/MP4/WebM/ProRes 等格式（0.1-120 fps）并加音频，经 webhook 发送 Discord；还可将 Discord CDN URL 写入 GitHub 仓库。视频功能需系统安装 ffmpeg；节点本身仅依赖 requests。另含可选独立 Discord bot，可通过斜杠命令触发 ComfyUI 工作流，需额外依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 图像/视频节点经 webhook 直发 Discord，附带提示词与工作流 JSON
- 视频支持 GIF/MP4/WebM/ProRes，帧率 0.1-120 fps，可加音频与 ping-pong 循环
- 批量图像每条消息最多 9 张，含唯一标识防冲突
- 可选独立 Discord bot，斜杠命令触发 ComfyUI 工作流

## 适用场景

- 在 ComfyUI 工作流中生成后直接把图/视频发到 Discord 频道
- 把生成的 Discord CDN 链接自动汇总到 GitHub 仓库做媒体图库
- 让 Discord 用户通过斜杠命令远程触发 ComfyUI 工作流

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L17: **Send your AI-generated images and videos directly to Discord from ComfyUI!**
> L99: |**What it does**|Send images/videos to Discord from your workflow|Standalone bot that lets Discord users trigger C
> L100: |**How to use**|Add `DiscordSendSaveImage` or `DiscordSendSaveVideo` to your workflow|Run `python -m bot` as a sep

## 星数曲线

```mermaid
xychart-beta
    title "AEmotionStudio/ComfyUI-DiscordSend 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `9111a0693283` · [字段定义](../../DATASET.md)*
