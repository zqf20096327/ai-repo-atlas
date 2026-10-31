# neonwatty/youtube-gif-maker

⭐ 19 · Python · Apache-2.0 · 推送 2026-07-31 · [GitHub](https://github.com/neonwatty/youtube-gif-maker) · 个人维护

**自托管 YouTube 视频 GIF 生成器：文本描述定位片段并生成 GIF**

基于 Python 和 Streamlit 的自托管 Web 应用：输入 YouTube/Shorts 链接和描述短语，应用拉取视频与自动字幕，可用 Whisper 系列模型（含 turbo）自行生成转写，对转写做向量嵌入后语义匹配输入短语，命中时间戳生成初始剪辑与 GIF，用户可手动调整起止时间后下载分享。支持 pip 依赖安装和 Docker Compose 两种运行方式，本地运行无需 GPU。浏览器扩展版 YTgify 为其后续形态。

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

- Whisper 系列模型（含 turbo）生成视频转写
- 转写向量嵌入后按输入短语语义匹配定位时间戳
- 生成 GIF 后可手动调整起止时间
- 提供 Docker Compose 与 Python 两种运行方式

## 适用场景

- 把 YouTube 视频中的特定台词片段做成 GIF 分享
- 用自然语言描述快速定位并截取视频瞬间
- 在本地自托管部署，无需 GPU 即可运行

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L41: The app pulls your desired YouTube video and - if available - YouTube's automated transcript. Because these transcr
> L43: A vector embedding of the transcription is then created for semantic matching of your input phrase.

## 星数曲线

```mermaid
xychart-beta
    title "neonwatty/youtube-gif-maker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c022f54e1e17` · [字段定义](../../DATASET.md)*
