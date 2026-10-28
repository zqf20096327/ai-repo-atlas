# PraveenElango/ros2-fast-stereo

⭐ 31 · C++ · 推送 2026-07-27 · [GitHub](https://github.com/PraveenElango/ros2-fast-stereo) · 个人维护

**给机器人开发者的 ROS2 实时双目深度估计工作空间**

基于 ROS2 Jazzy 的工作空间，将 Fast-FoundationStereo 立体匹配模型经 TensorRT 加速部署，实时输出视差图与彩色点云。由三个包组成：camera_models（7 种投影模型统一抽象）、perception_utils（像素级重投影映射）、ffs_depth（GPU 矫正 + TensorRT 推理节点）。支持鱼眼等广角非平行相机对，四组立体对的 quad 模式可做全向深度。需 NVIDIA GPU 与自行导出的 TensorRT 引擎，通过 Docker Dev Container 提供 CUDA/TensorRT 预装环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 种相机投影模型统一到 pixelToRay/rayToPixel 接口
- 全流程（GPU remap、归一化、TensorRT 推理、视差转深度）在设备端 CUDA/NPP/TensorRT 运行，每帧仅跨主机/设备边界各一次
- quad_stereo_node 用单个 batch-4 引擎跑 4 组立体对实现全向深度
- 提供含 ROS2 Jazzy + CUDA 13.2 + TensorRT 10.16 的 VS Code Dev Container

## 适用场景

- 在 ROS2 机器人上用鱼眼等广角相机对做实时深度估计
- 多相机环绕布置实现全向点云感知
- SLAM / 机器人导航的前置立体深度节点

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L6: A ROS2 (Jazzy) workspace for real-time stereo-rectified depth estimation from both pinhole and wide-FOV camera pairs
> L24: Once a synchronised frame pair arrives over ROS subscription, every stage of the pipeline from GPU remap, normalisa
> L12: |`ffs_depth`|ROS2 nodes (`ffs_depth_node`, `quad_stereo_node`) that rectify camera pairs on the GPU and run a Tenso

## 星数曲线

```mermaid
xychart-beta
    title "PraveenElango/ros2-fast-stereo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-28 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `09f4b08f681a` · [字段定义](../../DATASET.md)*
