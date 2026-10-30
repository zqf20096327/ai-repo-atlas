# raviksharma/blurfaces

⭐ 78 · Python · AGPL-3.0 · 推送 2026-05-11 · [GitHub](https://github.com/raviksharma/blurfaces) · 个人维护

**视频人脸检测与打码工具，支持模糊/黑条/像素化**

基于 insightface 与 ffmpeg 的命令行工具：检测视频中人脸并 censor 处理，提供三种模式（全部人脸、指定人脸、排除指定人脸）与四种打码样式（模糊、黑块、像素、眼条）。可通过参考人脸图像与余弦相似度阈值做目标匹配，可选模型包（buffalo_l/s/sc）与检测分辨率调节速度与准确度，音轨自动保留。以 Python 3.12+ / uv 源码方式安装，另提供 GHCR 预构建 Docker 镜像。作者注明工具不完美，发布前应配合手工编辑。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种模式：全部/指定/排除特定人脸
- 四种打码样式（blur/blackout/pixel/bar）
- 可选 buffalo_l/s/sc 模型包与检测分辨率调节速度准确度
- ONNX Runtime 可换 onnxruntime-gpu 获得 CUDA 加速，音轨自动保留

## 适用场景

- 对公开视频中的路人面部做匿名化处理
- 仅模糊某个人或保留某个人不打码
- 批量处理需保护隐私的视频素材

## 场景标签

`人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: Detect and censor faces in video using insightface and ffmpeg.
> L17: - **Three modes** — blur all faces, just one specific face, or everyone *except* one face

## 星数曲线

```mermaid
xychart-beta
    title "raviksharma/blurfaces 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 77 --> 79
    line [78, 78]
```

2026-10-18 78 → 2026-10-30 78（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8c9c5226a507` · [字段定义](../../DATASET.md)*
