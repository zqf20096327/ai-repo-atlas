# onuralpszr/trackforge

⭐ 35 · Rust · MIT · 推送 2026-10-27 · [GitHub](https://github.com/onuralpszr/trackforge) · [官网](https://onuralpszr.github.io/trackforge/) · 个人维护

**Rust 实现的多目标跟踪库：统一 API 供 Python/Rust 调用**

以 Rust 编写、带 PyO3 Python 绑定的多目标跟踪库，定位为 GPU 检测器与跟踪管线之间的 CPU 粘合层。统一 API 提供 ByteTrack、DeepSORT、OC-SORT、Deep OC-SORT、BoT-SORT、TrackTrack、SORT 七种跟踪器；默认构建轻量、不含图像编解码器，检测框与 Re-ID 嵌入由用户传入，图像特征提取器为可选 reid-model 特性。README 声明处于活跃开发期，API 可能变动，MSRV 为 Rust 1.89。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 7 种跟踪器统一 API，Python/Rust 参数一致
- 默认构建不拉入图像编解码器，检测与嵌入由调用方传入
- 可插拔 Re-ID：reid-model 特性提供逐帧产出嵌入的模型包装
- ByteTrack 宣称单帧耗时 < 1ms（原文数据）

## 适用场景

- 在我的检测管线中接入 ByteTrack/OC-SORT 等跟踪算法
- 用自选 Re-ID 模型驱动 DeepSORT/Deep OC-SORT 外观匹配
- Python 与 Rust 两侧共用同一套跟踪参数做交叉验证

## 场景标签

 · 领域:计算机视觉/多目标跟踪

## 证据(README 行号)

> L3: **Trackforge** is a unified, high-performance computer vision tracking library implemented in Rust with Python bindi
> L36: - 🎯 **Multi-Algorithm** ByteTrack, OC-SORT, DeepSORT, Deep OC-SORT, BoT-SORT, TrackTrack, and SORT with a unified A

## 星数曲线

```mermaid
xychart-beta
    title "onuralpszr/trackforge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-30 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b36da62f37d7` · [字段定义](../../DATASET.md)*
