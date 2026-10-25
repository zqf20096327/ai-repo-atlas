# alebal123bal/khadas_yolov8n_multithread

⭐ 93 · C++ · Apache-2.0 · 推送 2026-06-19 · [GitHub](https://github.com/alebal123bal/khadas_yolov8n_multithread) · 个人维护

**RK3588S NPU 上实时检测无人机的多线程视觉流水线**

面向 Rockchip RK3588S SoC 的 C++ 多进程计算机视觉流水线：采集 1080p MIPI 帧，用 3 个 NPU 核并行运行 YOLOv8n 推理，吞吐达到相机 46 FPS 上限，内存稳定在单流约 140 MB；捕获（ISP）、色彩转换/缩放（RGA）与推理（NPU）全部由固定功能硬件完成，CPU 不参与。检测结果经 Unix 域套接字流向 ByteTrack 跟踪、时序特征、存在性 FSM，并在目标离场时由同板 NPU 上运行的 Qwen2.5-0.5B 生成自然语言场景评估。需从源码编译，目标硬件为带 OS08A10 MIPI 相机的 RK3588S 板卡（在 Khadas Edge2 上开发测试）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 3 线程 NPU 推理将吞吐从约 31 FPS 提升至 46 FPS 相机上限
- 单流约 140 MB、双流约 290 MB 的恒定内存占用
- 检测→ByteTrack→时序特征→存在性 FSM→按需 LLM 摘要的可组合多进程流水线
- blackout/resume 控制面将 NPU 让渡给 LLM 全速运行后交还相机

## 适用场景

- 在低成本 RK3588S 板卡上做实时无人机检测与追踪
- 通过 HDMI 或 RTSP 查看带标注的检测结果流
- 检测事件后获取板上 LLM 生成的自然语言场景描述

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3:  Real-time YOLOv8n UAV detection (single 1280x1280 stream) running on the RK3588S NPU
> L10: YOLOv8n across all **3 NPU cores** in parallel (lifting throughput from ~31 to
> L19: (Qwen2.5-0.5B, on the *same* NPU) writes a natural-language assessment of what

## 星数曲线

```mermaid
xychart-beta
    title "alebal123bal/khadas_yolov8n_multithread 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 92 --> 94
    line [93, 93]
```

2026-10-18 93 → 2026-10-25 93（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `c9db2b4e68ab` · [字段定义](../../DATASET.md)*
