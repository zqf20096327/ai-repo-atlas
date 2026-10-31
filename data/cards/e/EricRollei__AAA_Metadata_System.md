# EricRollei/AAA_Metadata_System

⭐ 14 · Python · NOASSERTION · 推送 2025-12-19 · [GitHub](https://github.com/EricRollei/AAA_Metadata_System) · 个人维护

**ComfyUI 图像元数据管理与多格式存取自定义节点集**

面向 ComfyUI 用户的自定义节点包，提供图像元数据的读取、写入、智能合并、XMP 边车文件、SQLite 数据库存储与工作流数据保存；图像格式覆盖 PNG/JPEG/TIFF/WebP/PSD（含图层、混合模式）/APNG/SVG，支持 ICC 色彩配置嵌入与 MWG-RS 标准区域。附带元数据查询节点、文字叠加节点、基于感知哈希的重复图查找节点，以及适配 Wan 2.2 视频工作流的尺寸计算节点。以 git clone 到 custom_nodes 目录方式安装，PyExiv2 与 ExifTool 为可选依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PSD/TIFF 图层保存与读取，ICC 色彩配置嵌入
- 元数据智能合并、多源存储（XMP/EXIF/TXT/JSON/SQLite）
- 感知哈希重复图查找（pHash/dHash/aHash/wHash）
- Wan 2.2 视频工作流尺寸计算节点（6 档尺寸、15 种比例）

## 适用场景

- 我在 ComfyUI 生成图像时保存完整工作流与生成参数以便复现
- 我在 Photoshop/Lightroom 工作流中保留 XMP 元数据与色彩配置
- 我想批量清理图库中的重复与相似图像

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L1: # AAA Metadata System for ComfyUI
> L40: - **ComfyUI Integration**: Seamlessly integrates with ComfyUI nodes for workflow capture and parameter extraction

## 星数曲线

```mermaid
xychart-beta
    title "EricRollei/AAA_Metadata_System 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `0a3c434e9d5d` · [字段定义](../../DATASET.md)*
