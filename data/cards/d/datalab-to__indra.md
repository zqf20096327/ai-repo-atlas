# datalab-to/indra

⭐ 1,989 · Python · Apache-2.0 · 推送 2026-11-24 · [GitHub](https://github.com/datalab-to/indra) · [官网](https://www.datalab.to) · 组织维护

**CPU 上运行的轻量 OCR 流水线：将 PDF 与图片转为 markdown/文本/JSON**

Indra OCR 是一个约 1M 参数的紧凑 OCR 流水线，基于 ONNX Runtime 运行于 CPU，无需 PyTorch 或 GPU。将 PDF 和图片转换为带框信息的 markdown、文本或 JSON，支持手写体、80+ 种语言及任意角度页面。提供 CLI 与 Python API，含本地 web 查看器、多进程批量转换、数学公式识别（LaTeX 输出）与数字 PDF 文本层读取。限制包括复杂表格、草书手写与退化扫描读取较弱。代码为 Apache 2.0，模型权重采用修改版 OpenRAIL-M 许可，商业使用需另行授权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ONNX Runtime 运行于 CPU，无需 PyTorch 或 GPU
- 支持 80+ 种语言与手写识别，四种脚本识别器分工
- 输出含行/框/布局块/阅读顺序的结构化 JSON
- 附带本地 web 查看器，可对比 Tesseract 结果

## 适用场景

- 将扫描件和图片批量转为 markdown 或 JSON
- 提取含框和阅读顺序的版面结构数据
- 读取数字 PDF 文本层并对缺失部分做 OCR
- 多语言文档（含 CJK、RTL 文字）的文字识别

## 场景标签

`OCR` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L20: Indra OCR is a compact OCR pipeline that runs on CPU. It turns PDFs and images into markdown, text, or JSON with bo
> L23: - **CPU-first** - ONNX Runtime, no PyTorch or GPU required. Use multiple processes for batch conversion.

## 星数曲线

```mermaid
xychart-beta
    title "datalab-to/indra 星数(近 27 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 924 --> 2085
    line [1074, 1157, 1228, 1347, 1426, 1469, 1526, 1569, 1020, 1681, 1734, 1764, 1788, 1799, 1820, 1839, 1860, 1871, 1886, 1892, 1908, 1912, 1916, 1939, 1962, 1978, 1989]
```

2026-10-26 1,074 → 2026-11-28 1,989（+915）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `889263da3977` · [字段定义](../../DATASET.md)*
