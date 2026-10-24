# Albonire/notebooklm-watermark-remover

⭐ 82 · Python · MIT · 推送 2026-09-15 · [GitHub](https://github.com/Albonire/notebooklm-watermark-remover) · 个人维护 · 中文 README

**去除 NotebookLM 导出文件中水印的 Python 工具**

处理 NotebookLM 生成的 PDF、PPTX 与图片（PNG/JPG/WEBP）的命令行工具：通过分析局部对比度与模糊差异检测水印区域，再用基于计算机视觉（OpenCV）的 inpainting 重建文字背后的背景，并过滤掉水印附近的正文内容避免误删。支持批量处理文件夹、PDF 首页预览模式与边距参数调节；Windows 下可按 BUILD.md 自行打包 EXE。README 附带法律免责声明，限定仅对用户拥有权利的文档使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于对比度/模糊差异检测水印并用 CV inpainting 重建背景
- 支持 PDF、PPTX、PNG/JPG/JPEG/WEBP（含透明通道）
- 批量处理、PDF 首页预览与边距参数调节
- 智能过滤水印附近的正文内容

## 适用场景

- 清理自己拥有的 NotebookLM 导出 PDF/PPTX 中的水印
- 批量处理整个文件夹的导出文件
- 先预览首页效果再决定是否全量处理

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L12: Instead of just covering the watermark with a solid color box (which looks bad on gradients or textured backgrounds
> L108: - `remover.py` - Core logic using PyMuPDF and OpenCV.

## 星数曲线

```mermaid
xychart-beta
    title "Albonire/notebooklm-watermark-remover 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 81 --> 83
    line [82, 82]
```

2026-10-18 82 → 2026-10-24 82（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `8e12f3895372` · [字段定义](../../DATASET.md)*
