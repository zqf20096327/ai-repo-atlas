# den-run-ai/pdfmini

⭐ 29 · JavaScript · MIT · 推送 2026-10-19 · [GitHub](https://github.com/den-run-ai/pdfmini) · [官网](https://den-run-ai.github.io/pdfmini/) · 组织维护

**浏览器本地压缩与合并 PDF 的静态网页工具，文件不上传**

纯客户端静态网页应用：在浏览器内完成 PDF 压缩与合并，文件不上传。压缩保留文本、矢量、链接与表单域，只按页面实际显示尺寸对图像重采样并重新编码；自带 JPEG 编码器保证各浏览器输出字节一致。提供 Light/Balanced/Strong 三档及高级设置，另有无损清理（去除 XFA 副本、重复流、未用对象等）。无构建步骤，通过 GitHub Pages 发布；限制包括不支持加密 PDF 直接优化、字体不做子集化、数字签名不能保留。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 全流程本地运行，仅从 CDN 加载固定版本的 pdf-lib 与 PDF.js
- 自带 JPEG 编码器，跨浏览器输出字节一致（CI 验证）
- 三档压缩级别，按图像实际显示 DPI 重采样，无损图像优先无损再编码
- 无损清理：内联单次绘制的 Form XObject、去除静态 XFA 副本与未用对象

## 适用场景

- 在手机或电脑上压缩 PDF 以满足邮件或上传大小限制
- 合并多份 PDF 并一次性压缩
- 处理含照片或扫描件的报表、表单等文件

## 场景标签

 · 领域:文档处理/浏览器工具

## 证据(README 行号)

> L3: Compress and combine PDFs in your browser. Files are processed on your
> L45: 1. pdf-lib parses the PDF.

## 星数曲线

```mermaid
xychart-beta
    title "den-run-ai/pdfmini 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-28 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 low · 依据 README sha `2bdd7fdcea91` · [字段定义](../../DATASET.md)*
