# mftnakrsu/Comparison-of-OCR

⭐ 63 · Python · MIT · 推送 2026-07-30 · [GitHub](https://github.com/mftnakrsu/Comparison-of-OCR) · 个人维护

**OCR 引擎对比评测工具：同一图像跑多个引擎并报告结果**

在同一批图像上运行 Tesseract、EasyOCR、RapidOCR、PaddleOCR、keras-ocr 等多个 OCR 引擎，报告每个引擎读取的文本、耗时与置信度，便于用户按自身图像选择引擎。每个引擎是可选 extras，按需安装；统一返回 TextBox(text, polygon, confidence) 结构，新增引擎只需写一个 adapter 注册。提供 CLI（python -m ocr_compare）与 Python API。2022 年的原始结论（README 中）基于 keras-ocr、EasyOCR 与 pytesseract，README 建议在自己的图像上重新跑基准再下结论。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多引擎（Tesseract/EasyOCR/RapidOCR/PaddleOCR/keras-ocr）同一图像对比，输出文本、耗时与置信度
- 每个引擎为可选 extra，pip install -e ".[easyocr,tesseract]" 按需安装
- 统一 TextBox 数据结构与 adapter 注册机制，可扩展新引擎
- 提供 CLI 与 Python API，keras-legacy 隔离在独立 extra 不影响其他引擎

## 适用场景

- 为自己的图像集实测候选 OCR 引擎的速度与识别结果
- 通过统一 API 在项目中切换或组合多个 OCR 后端
- 查看各引擎安装体积与依赖差异以决定部署方案

## 场景标签

`OCR` · 领域:感知与多模态

## 证据(README 行号)

> L11: This repository runs several OCR engines over the same images and reports what each
> L113: Every engine returns the same `TextBox(text, polygon, confidence)` shape, so adding

## 星数曲线

```mermaid
xychart-beta
    title "mftnakrsu/Comparison-of-OCR 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-28 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `927b6ca08280` · [字段定义](../../DATASET.md)*
