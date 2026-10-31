# matthewlam721/octopus-parallel

⭐ 26 · Python · MIT · 推送 2026-04-14 · [GitHub](https://github.com/matthewlam721/octopus-parallel) · 个人维护

**变长批次的块级 GPU 调度技术：免填充处理大小不一的图像**

面向 GPU 上批量变长图像处理的调度技术对比与实现：将不同尺寸图像拼接为扁平数组，用块级元数据让每个 CUDA 块 O(1) 定位所属图像，替代逐像素查找表与二分查找。基于 numba JIT 实现，在 RTX 4090、T4、Jetson Orin Nano 上用 VisDrone 无人机影像与 Sentinel-2 卫星数据做基准测试，报告速度、能耗（INA3221 电压×电流测量）与 VRAM 占用，并附自动调优器判断块元数据是否值得启用。TensorRT 对比数据亦在列。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 块级元数据实现 O(1) 定位，仅约 31 KB 元数据开销
- 在 Jetson Orin Nano 上较二分查找快 2.5-3.5 倍，T4 快 22-28%
- 真实 VisDrone 数据上端到端 1.23 倍加速、每帧能耗约降 12-13%
- 附带 <50 ms 的自动调优器，判断块元数据是否适用当前硬件

## 适用场景

- 无人机/卫星等边缘设备上批量裁剪变尺寸检测框做预处理
- 内存受限 GPU 上避免批量填充（padding）造成的显存与带宽浪费
- YOLO 检测后的实时分类预处理流水线提速

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L142: Setup: real VisDrone-DET val frames as canonical 1920×1080 input, 28 detections/frame avg sampled from real bbox p
> L191: Also ran YOLO object detection on 200 frames. GPU preprocessing gave 2.9× end-to-end speedup (4384 ms → 1490 ms) w

## 星数曲线

```mermaid
xychart-beta
    title "matthewlam721/octopus-parallel 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-31 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `3b3542954ca4` · [字段定义](../../DATASET.md)*
