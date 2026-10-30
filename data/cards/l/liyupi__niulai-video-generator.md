# liyupi/niulai-video-generator

⭐ 38 · TypeScript · MIT · 推送 2026-08-19 · [GitHub](https://github.com/liyupi/niulai-video-generator) · 个人维护 · 中文 README

**输入小故事生成《牛来》风格 3D 抽象动画的命令行工具**

面向创意/梗视频创作者与 generative-art 爱好者的 Node.js 命令行工具：输入一段小故事，经 DeepSeek（或离线规则引擎）生成剧本，再用 Three.js 程序化渲染低模直立牛场景、系统 TTS 配音、FFmpeg 合成 mp4，并输出严格同步的 srt 字幕；不调用视频大模型。音频时长为唯一时间基准，字幕时间码由音频反推。限制：环境要求 macOS、Node 22+、ffmpeg，配音依赖系统 `say` 命令；不配 DeepSeek key 时自动走离线规则引擎。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Three.js 程序化渲染 + TTS + FFmpeg 合成，不依赖视频大模型
- 字幕时间码由 ffprobe 实测音频时长反推，误差为 0
- --jank 粗糙度滑块派生帧率、雾浓度、字幕错别字率等十几个参数
- --offline 完全离线，用内置规则引擎替代 LLM 生成剧本

## 适用场景

- 把自己的日常小故事变成牛来草原世界观的抽象动画
- 用 --golden 一键复刻原片「绊倒体」段落
- 离线生成带配音和同步字幕的梗视频成片

## 场景标签

`语音合成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L3: 输入一段现代生活的小故事，产出一条还原《牛来》风格的抽象动画：粗糙低模的直立牛、死平的光照、浓白的雾、卡成 PPT 的动作、毫无感情的配音，以及无厘头到一本正经的台词。带硬字幕和 srt，配音与字幕严格同步。
> L34: - `cp .env.example .env`，填 `DEEPSEEK_API_KEY`；不配也能跑，会自动走离线规则引擎

## 星数曲线

```mermaid
xychart-beta
    title "liyupi/niulai-video-generator 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 36 --> 39
    line [37, 38, 38]
```

2026-10-18 37 → 2026-10-30 38（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `02fefcac9c08` · [字段定义](../../DATASET.md)*
