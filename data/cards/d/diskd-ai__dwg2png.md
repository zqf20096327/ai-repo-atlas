# diskd-ai/dwg2png

⭐ 16 · Rust · 推送 2026-06-25 · [GitHub](https://github.com/diskd-ai/dwg2png) · 组织维护

**纯 Rust 的 DWG 转多页 PNG 渲染器与元数据索引器**

面向需要对 DWG 图纸做 RAG/VLM 摄取的 SaaS 后端场景：解析原生 DWG（R13–R2018，acadrust，MPL-2.0，无 C 依赖、无 FFI、无 GPU），用 tiny-skia 在 CPU 上将模型空间与布局空间渲染为多页 PNG，并输出图层、块、标题栏属性、文本等结构化 JSON 索引文档。文本层直接来自 DWG 数据而非 OCR，每条标签带像素坐标。支持分块 tile 输出供 VLM 使用，提供预编译二进制与 Docker 镜像。v1 尚不渲染填充、标注几何与光栅图像等实体。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- DWG（R13–R2018）解析→多页 PNG 渲染，纯 Rust、无 C 依赖/FFI/GPU
- 无损位置参照文本层：文本直取自 DWG（无 OCR），带像素 x,y,w,h、旋转、颜色、图层
- 每文件 IndexDoc JSON：图层、块、标题栏属性、布局
- --tiles 生成约 1500px 可读切块及逐块标签，供 VLM 输入

## 适用场景

- 把 DWG 图纸转成可检索、可引用的文本与图像产物接入 RAG 流水线
- 为 VLM 提供高分辨率可读 tile 与已提取文本做多模态检索
- 批量转换 DWG 目录并生成含缩略图与 SVG 文本叠加的 HTML 报告

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L3: Pure-Rust **DWG &rarr; multipage PNG** renderer and **metadata indexer** for a
> L110: dwg2png turns an opaque binary DWG into retrievable, citable artifacts. Run the

## 星数曲线

```mermaid
xychart-beta
    title "diskd-ai/dwg2png 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `fc1bd4308dbc` · [字段定义](../../DATASET.md)*
