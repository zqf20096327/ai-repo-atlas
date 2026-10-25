# sourav4243/sift-video

⭐ 47 · Rust · GPL-3.0 · 推送 2026-04-07 · [GitHub](https://github.com/sourav4243/sift-video) · 个人维护

**多模态语义视频搜索引擎：用自然语言检索视频内时间戳**

面向需要视频内容检索用户的语义视频搜索引擎：离线处理视频，用 Whisper small.en 转录音频、MobileCLIP2 提取帧与文本的 768 维嵌入，存入 Qdrant 向量数据库；查询时对音频（权重 0.3）与视觉（权重 0.7）两个集合并行检索，2 秒窗口内合并为 audio+visual 结果并返回精确时间戳。由四个 Docker 服务组成（C++ 摄取/嵌入、Rust 查询引擎、Qdrant），自带 Web UI 与 REST API，支持 yt-dlp URL 下载、文件上传（≤1GB）与浏览器内播放定位；提供 CPU 与 NVIDIA GPU（CUDA）两种部署，许可为 GPLv3。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Whisper 转录 + MobileCLIP2 视觉嵌入写入 Qdrant 双集合
- 音频/视觉加权融合检索并按 2 秒窗口合并结果
- 自带 Web UI（搜索/媒体库/上传/播放器）与 REST API
- 支持 URL 下载（yt-dlp）SSE 实时进度与拖放上传

## 适用场景

- 在长视频中用自然语言找到某个画面或对话出现的时间点
- 建立个人或团队的视频语义检索库并跳转播放
- 通过 API 将视频时间戳检索集成到其他应用

## 场景标签

`语义搜索` `多模态` · 领域:知识与检索

## 证据(README 行号)

> L5: SIFT-Video is a multimodal semantic video search engine that lets you search inside videos using natural language an
> L7: Videos are processed offline, audio and frames are converted into semantic embeddings using pre-trained ONNX models,

## 星数曲线

```mermaid
xychart-beta
    title "sourav4243/sift-video 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 46 --> 48
    line [47, 47]
```

2026-10-18 47 → 2026-10-25 47（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `90ee4e8b7317` · [字段定义](../../DATASET.md)*
