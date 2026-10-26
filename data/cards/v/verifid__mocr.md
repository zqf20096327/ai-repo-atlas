# verifid/mocr

⭐ 25 · Python · MIT · 推送 2026-04-13 · [GitHub](https://github.com/verifid/mocr) · [官网](https://mocr.verifid.app) · 组织维护

**证件卡 OCR 与人脸检测 Python 库：识别有效文本并定位人脸**

纯 Python 库，针对身份证件做有意义的文字识别与人脸检测。内置 EAST 预训练文本检测模型（frozen_east_text_detection.pb），结合 OpenCV 深度学习技术定位文本框，OCR 依赖系统级 Tesseract，支持传入自定义训练模型替换默认 EAST 检测器。提供 TextRecognizer API 与 CLI，可从图片和视频中检测并裁剪人脸，输出带边界框的文本结果与人脸字节数组。限制：需先安装 Tesseract 才能使用 OCR 功能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 EAST 预训练文本检测模型，支持自定义模型参数
- 从图片与视频检测并裁剪人脸区域
- 提供 CLI（python -m mocr）覆盖 OCR 与人脸检测

## 适用场景

- 从身份证件图像提取有效文本与边界框
- 从证件照或视频中检出并裁剪人脸区域
- 集成到证件信息录入流程中做 OCR 前处理

## 场景标签

`OCR` `人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L25: **mocr** is a library that can be used to detect meaningful optical characters from identity cards. Code base is pu
> L26: works with 3.x versions. It has some low level dependencies such as ``Tesseract``. **mocr** uses a pre-trained east

## 星数曲线

```mermaid
xychart-beta
    title "verifid/mocr 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-26 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `35f4044d56f9` · [字段定义](../../DATASET.md)*
