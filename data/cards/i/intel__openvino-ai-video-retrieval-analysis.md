# intel/openvino-ai-video-retrieval-analysis

⭐ 15 · Python · Apache-2.0 · 推送 2026-03-16 · [GitHub](https://github.com/intel/openvino-ai-video-retrieval-analysis) · 组织维护

**VLC 视频检索扩展：用 AI 对本地视频做语义级内容检索**

基于 OpenVINO 的视频检索（Video RAG）项目，以 VLC 扩展形式提供：在 Windows 端通过 Python 生成视频帧的嵌入并存入 VDMS 向量数据库（Docker 运行于 WSL），再以 VLC Lua 扩展发起检索请求，返回匹配视频片段。安装流程分为两部分：WSL 中安装 Docker 并启动 VDMS 容器，Windows 侧克隆源码、建虚拟环境安装依赖（含 langchain-community、onnx、openvino 2024.3）。Shotcut 版本标注 coming soon。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 VLC Lua 扩展形式集成视频检索功能
- 嵌入生成基于 OpenVINO（2024.3.0）
- VDMS 作为向量数据库，容器化运行并支持持久化存储
- 首次运行生成嵌入，后续运行直接启动服务器复用

## 适用场景

- 在 VLC 播放器中对本地视频库做语义检索
- 快速定位长视频中包含特定内容的片段

## 场景标签

`RAG` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L2:  - Video Retrieval Extension for VLC
> L85:  pip install onnx==1.16.0 openvino==2024.3.0 openvino-dev==2024.3.0

## 星数曲线

```mermaid
xychart-beta
    title "intel/openvino-ai-video-retrieval-analysis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `80f44d9b99bf` · [字段定义](../../DATASET.md)*
