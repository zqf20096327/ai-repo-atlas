# jishnujayakumar/MV-Tractus

⭐ 124 · C · 推送 2025-12-04 · [GitHub](https://github.com/jishnujayakumar/MV-Tractus) · 组织维护

**从 H264 视频中提取运动向量的 CLI 与 Python 工具**

围绕 FFmpeg 构建的运动向量提取工具：C 语言 CLI（extract_mvs / extract_mvs_with_frames）从 H264/MPEG 流读取运动向量输出 JSON，可同时抽取帧；Python 包 mv-tractus 提供相同能力并支持用 Pillow 在帧上叠加向量可视化。面向计算机视觉/视频分析开发者，作为特征提取的数据预处理环节。CLI 需本地编译并自行准备 FFmpeg 库，README 声明 FFmpeg 未经修改、性能 best effort。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- C CLI 从 H264/MPEG 流提取运动向量，输出 JSON
- Python 包支持向量+帧抽取及 Pillow 叠加可视化
- 提供无需 Python 的 FFmpeg 原生可视化命令

## 适用场景

- 为视频动作识别/目标跟踪等任务提取运动向量特征
- 将运动向量叠加到视频帧上做可视化检查
- 批量从 H264 视频导出运动向量 JSON 数据

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L2: Extract motion vectors from H264/MPEG streams. CLI tools wrap FFmpeg; the Python package (`mv-tractus`) offers the s
> L12: 2. Build or point to FFmpeg; ensure libs are discoverable (see `install_ffmpeg.sh`, `ffmpeg.conf`).
> L22: ffmpeg -flags2 +export_mvs -debug vis_mv=pf+bf -i input.mp4 -c:v libx264 -crf 18 -preset fast output_with_mv.mp4

## 星数曲线

```mermaid
xychart-beta
    title "jishnujayakumar/MV-Tractus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 123 --> 125
    line [124, 124]
```

2026-10-18 124 → 2026-10-28 124（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 low · 依据 README sha `cca0787df313` · [字段定义](../../DATASET.md)*
