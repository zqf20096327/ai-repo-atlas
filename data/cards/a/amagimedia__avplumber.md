# amagimedia/avplumber

⭐ 50 · C++ · AGPL-3.0 · 推送 2026-10-27 · [GitHub](https://github.com/amagimedia/avplumber) · 组织维护

**基于 FFmpeg/libav 的实时流媒体处理图框架，支持动态重配**

C++ 实现的图式实时音视频处理框架，节点基于 libavcodec/libavformat/libavfilter，通过 TCP 文本命令在运行中重建处理图，覆盖转码、多线程滤镜、多路输出、时间戳与音视频同步、断流垫片、流健康监测等场景。节点间以无锁队列连接，支持 DMA-BUF/EGLImage 零拷贝 GPU 数据传递，可通过编译开关启用 CUDA/VAAPI/DRM 及神经网络绘制、跟踪与重构图节点（TensorRT 推理节点在树外维护）。提供 Docker 构建、静态库与 OBS 插件示例；不支持字幕处理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文本 API 在运行中动态重配处理图（netcat/telnet 控制）
- 节点间无锁队列连接，支持 DMA-BUF/EGLImage GPU 数据传递
- 编码一次分发到多个输出、断流垫片插入与流健康监测
- 可构建为静态库，附 OBS source 插件集成示例

## 适用场景

- 搭建可在线重配的转码与流媒体处理链路，替代部分 FFmpeg 用途
- 多线程视频滤镜与多路分发输出
- 监控输入流健康并在断流时插入垫片画面
- 以静态库形式嵌入自有应用（如 OBS 插件）

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: avplumber is a graph-based real-time processing framework. Graph can be reconfigured on the fly using a text API. Mo
> L106: - NEURAL_NET=1: enable retained neural drawing, tracking, and reframing nodes. Model inference nodes and their Ten
> L107: - HAVE_TENSORRT=1, TENSORRT_ROOT=/path/to/TensorRT: not read by this Makefile. Out-of-tree node fragments included

## 星数曲线

```mermaid
xychart-beta
    title "amagimedia/avplumber 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 48 --> 51
    line [49, 50, 50]
```

2026-10-18 49 → 2026-10-28 50（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `730fe84a7132` · [字段定义](../../DATASET.md)*
