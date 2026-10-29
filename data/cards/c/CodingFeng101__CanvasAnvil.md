# CodingFeng101/CanvasAnvil

⭐ 97 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/CodingFeng101/CanvasAnvil) · [官网](https://canvasanvil.codingfgd.asia) · 个人维护 · 中文 README

**AI 多画布创作平台：图表/室内设计/PPT 生成工作区**

基于 React + TypeScript + Vite 的自部署 Web 应用，将图表、室内设计（CAD 出图与材料清单）、PPT 制作统一在一个工作区。PPT 生成走先大纲后制作的管线，可导出可编辑 .pptx、PDF 与图片版 PPT；每个画布有本地技能包（flow-skill/cad-skill/ppt-skill）。模型调用统一走 OpenAI HTTP 协议，通过 base URL 指向任意 OpenAI 兼容端点，仅图像生成需单独配置。当前版本 v2.1.0 已收敛为三个画布，海报/产品/信息图画布被移除。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三画布统一工作区：Diagram / Interior Design / PPT
- PPT 管线先大纲后生成，支持可编辑 .pptx / PDF / 图片导出
- 每个画布配套本地技能包，交付 CAD 图纸包与 CSV 材料清单
- 统一走 OpenAI 兼容端点，文本与图像通道分别配置

## 适用场景

- 用结构化提示生成研究框架图、架构图与实施路线图
- 室内设计从概念板到 2D 图纸与材料清单的一体化交付
- 通过大纲评审流程生成并导出可编辑演示文稿

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L5:  AI-powered multi-canvas creation for Diagrams, CAD, and PPT.
> L56: Generate full presentations through a controlled pipeline: outline first, visual production second, then export as 
> L175: - Every model call uses the OpenAI HTTP protocol. To use another vendor, point the base URL in Settings at their O

## 星数曲线

```mermaid
xychart-beta
    title "CodingFeng101/CanvasAnvil 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 96 --> 98
    line [97, 97]
```

2026-10-18 97 → 2026-10-29 97（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d72a080f037a` · [字段定义](../../DATASET.md)*
