# Kitware/dive

⭐ 110 · TypeScript · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/Kitware/dive) · [官网](https://kitware.github.io/dive) · 组织维护

**面向视频/图像标注与 VIAME 算法运行的 Web 界面**

DIVE 是 Kitware 维护的 Web 数据管理与标注界面：支持视频、单帧图像与图像序列标注，提供单帧框/多边形/线条、多帧包围框轨迹插值、属性化标签与视频自动转码；深度集成 VIAME 计算机视觉分析工具，可运行检测算法流水线并输出 CSV 检测结果。基于 Girder 5 + Girder Worker + Docker 架构（MongoDB、RabbitMQ、Redis），支持 GPU 与 CPU-only 两种 Docker Compose 模式，CPU 模式下自动禁用流水线与训练功能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 视频与图像序列标注，含多帧轨迹插值
- 集成 VIAME 检测流水线，输出 CSV 检测结果
- GPU / CPU-only 两种 Docker Compose 部署模式
- VIAME 与 FFmpeg 可执行文件内置于 worker 镜像

## 适用场景

- 为视频/图像数据集做目标标注与轨迹管理
- 运行 VIAME 检测流水线并导出检测结果
- 搭建本地或在线的视频标注与数据分析服务

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: DIVE is a web interface for performing data management, video annotation, and running a portion of the algorithms st
> L11: * deep integration with VIAME computer vision analysis tools
> L28: DIVE uses Girder 5 for data management and has a typical Girder + Girder Worker + Docker architecture (MongoDB, Rab

## 星数曲线

```mermaid
xychart-beta
    title "Kitware/dive 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 109 --> 111
    line [110, 110]
```

2026-10-18 110 → 2026-10-24 110（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `dfbc7f7a3c8a` · [字段定义](../../DATASET.md)*
