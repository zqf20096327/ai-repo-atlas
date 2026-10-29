# Anil-matcha/gemini-omni-comfyui

⭐ 24 · Python · MIT · 推送 2026-08-27 · [GitHub](https://github.com/Anil-matcha/gemini-omni-comfyui) · [官网](https://anil-matcha.github.io/gemini-omni-comfyui/) · 个人维护

**在 ComfyUI 中调用 Gemini Omni API 的视频生成节点集**

ComfyUI 自定义节点包，将 muapi.ai 上的 Google Gemini Omni API 封装为可视化节点：支持文生视频、图生视频（最多 5 张参考图）与视频编辑，可指定时长（4-10 秒）、宽高比、分辨率（720p/1080p/4K）、最多 3 个 AI 语音与角色 ID。另含语音配置、角色创建与视频下载/解码为 ComfyUI 帧张量的辅助节点。需注册 muapi.ai 获取 API key，可在 ComfyUI Manager 中经 Git URL 安装或手动 git clone 后 pip 安装依赖。

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

- 文生视频/图生视频（最多 5 图）/视频编辑三类生成节点
- 支持自定义 AI 语音档案与参考图角色创建
- 输出视频 URL 可下载到磁盘并解码为 ComfyUI IMAGE 帧张量
- 提供三个可直接导入的示例工作流 JSON

## 适用场景

- 在 ComfyUI 工作流里用文字或图片生成带配音的视频
- 对已有视频片段做风格化或变换编辑
- 用参考图创建角色并在多个生成节点中复用

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L16: - **Text-to-Video** — generate video from a text description with optional AI voiceover
> L20: These ComfyUI nodes wrap the Google Gemini Omni API so you can use the model directly inside ComfyUI workflows with
> L27: |🎬 Gemini Omni Text to Video|Generate video from a text prompt via Google Gemini Omni|

## 星数曲线

```mermaid
xychart-beta
    title "Anil-matcha/gemini-omni-comfyui 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `242d2fd06de6` · [字段定义](../../DATASET.md)*
