# LRriver/AIPPT

⭐ 23 · Python · Apache-2.0 · 推送 2026-07-08 · [GitHub](https://github.com/LRriver/AIPPT) · 个人维护 · 中文 README

**文档转可编辑 PPT 的 AI 工作台，支持逐页编辑与可编辑 PPTX 导出**

受 NotebookLM 启发的 AI PPT 工作台：读取论文等文档（md/txt/pdf/docx/pptx），生成可编辑大纲与逐页设计，再生成幻灯片页面，可逐页编辑、回退历史并导出 PDF、位图 PPTX 或可编辑 PPTX（OCR 文本转为文本框、线条/表格边框重建为原生形状、素材拆分为独立图片）。文本规划、VLM、OCR、图像生成与编辑各角色可分别配置 OpenAI 兼容模型，项目数据与 API key 存于浏览器本地。通过 git clone 源码、start.sh 启动前后端，另提供 CLI 方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多格式输入（md/txt/pdf/docx/pptx）转 Markdown 并生成 PPT 大纲与页面设计
- 逐页独立编辑、版本回退与替换确认
- 可编辑 PPTX 导出：文本框化、原生形状重建、素材拆分
- 五类模型角色（text/vlm/ocr/image/edit）可分别配置 OpenAI 兼容 API

## 适用场景

- 把论文或文档整理成可演示的 PPT
- 对生成的幻灯片逐页修改后导出继续在 PowerPoint 中编辑
- 自选不同模型承担文本规划、OCR 与图像生成等环节

## 场景标签

`图像生成` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L5: Build a controllable, editable, model-configurable AI PPT workbench inspired by NotebookLM. AIPPT converts papers, d
> L27: - **Model control**: Configure separate OpenAI-compatible models for text planning, visual understanding, OCR, imag

## 星数曲线

```mermaid
xychart-beta
    title "LRriver/AIPPT 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `13c6d3c07d0a` · [字段定义](../../DATASET.md)*
