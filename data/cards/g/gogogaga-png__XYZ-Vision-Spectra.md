# gogogaga-png/XYZ-Vision-Spectra

⭐ 53 · HTML · 推送 2026-10-25 · [GitHub](https://github.com/gogogaga-png/XYZ-Vision-Spectra) · 个人维护

**跨平台实时视觉检测工具包：图像/视频/摄像头/屏幕检测**

XYZ-Vision-Aura 提供图像、视频文件、摄像头直播流与屏幕内容的实时检测管线，输出统一的结构化检测结果（对象、人脸、文本区域、姿态、分割掩码与置信度标签）。同一检测请求可在 CUDA GPU 或 CPU 上执行，CPU 环境下回退到量化模型；按内存、延迟与精度要求自适应选择模型层级。支持 ROI 裁剪、置信度阈值、类过滤、批量与流式模式，检测事件可经回调、异步迭代器或消息队列输出。以自包含运行时分发包形式提供，解压后运行内置启动器，面向开发者、科研与自动化测试场景。README 以能力描述为主，未见具体命令行安装或代码示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 图像/视频/摄像头/屏幕四类来源共用统一检测输出 schema
- 同一请求可在 CUDA GPU 或 CPU 上执行，配置切换无需改代码
- ROI 裁剪、置信度阈值、类过滤与批量/流式调度
- 检测事件可输出为回调、异步迭代器、消息队列或 webhook 通知

## 适用场景

- 对摄像头直播流做实时对象检测并叠加显示
- 扫描屏幕指定区域用于 UI 自动化或无障碍辅助工具
- 批量处理图片文件夹并导出结构化检测结果
- 长视频分块或关键帧采样检测以控制内存占用

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L24: ### 🖼️ Image Detection
> L25: Feed Aura a single frame — a photograph, a scanned document, a screenshot, a generated artwork — and it returns str
> L33: ### 🖥️ Screen Detection
> L37: The same detection request can run on a CUDA-capable GPU for maximum throughput or on a CPU for portability and ene

## 星数曲线

```mermaid
xychart-beta
    title "gogogaga-png/XYZ-Vision-Spectra 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-25 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `6c59b8ee1b44` · [字段定义](../../DATASET.md)*
