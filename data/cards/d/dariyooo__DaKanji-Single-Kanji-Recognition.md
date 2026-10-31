# dariyooo/DaKanji-Single-Kanji-Recognition

⭐ 64 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/dariyooo/DaKanji-Single-Kanji-Recognition) · 个人维护

**识别单个日语汉字/假名的轻量 CNN 模型（<3MB，亚毫秒延迟）**

用 PyTorch 训练的自定义 CNN，输入任意尺寸灰度图，输出汉字/平假名/片假名的字符概率。管线包含 MLflow 实验跟踪、PT2E QAT 量化，可导出 ONNX 与 ExecuTorch（XNNPACK/CoreML）产物用于端侧 CPU/ARM 推理；导出时内置 resize 与归一化。int8 模型约 2.2MB、延迟约 0.14ms。附视觉相似字排序脚本，可打包为 Yomitan 静态词典。面向需要在应用中嵌入单字符识别的开发者，已被 DaKanji 等应用使用，使用时需署名致谢。流水线语言无关，换数据可支持中文等其他文字。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 任意尺寸灰度输入，模型内部完成 resize 与归一化
- 量化导出为 ONNX / ExecuTorch（XNNPACK int8 约 2.2MB）
- 视觉相似字嵌入排序并可导出 Yomitan 词典
- MLflow 实验跟踪与网格搜索选架构

## 适用场景

- 在移动/桌面应用中集成手写日语单字符识别
- 训练自己的文字识别模型（管线语言无关，可换中文等数据）
- 生成形近字邻居表用于学习类应用

## 场景标签

`OCR` `模型训练` · 领域:感知与多模态

## 证据(README 行号)

> L3: A small, fast CNN that takes a **(grayscale) image of any size** and returns character probabilities.
> L4: Recognize a single handwritten or printed Japanese character (**Kanji, Hiragana, or
> L114: 4. **Export** turns a checkpoint into an ONNX or ExecuTorch artifact with resize and normalize baked in, so it tak

## 星数曲线

```mermaid
xychart-beta
    title "dariyooo/DaKanji-Single-Kanji-Recognition 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 63 --> 65
    line [64, 64]
```

2026-10-18 64 → 2026-10-31 64（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `39fb9ca27cc0` · [字段定义](../../DATASET.md)*
