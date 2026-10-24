# yeyupiaoling/PaddlePaddle-DeepSpeech

⭐ 764 · Python · Apache-2.0 · 推送 2025-12-17 · [GitHub](https://github.com/yeyupiaoling/PaddlePaddle-DeepSpeech) · [官网](https://yeyupiaoling.blog.csdn.net/article/details/102904306) · 个人维护 · 中文 README

**基于 PaddlePaddle 的 DeepSpeech2 中文语音识别训练与预测引擎**

DeepSpeech2 论文的 PaddlePaddle 实现，提供端到端 ASR 训练与推理，支持 AIShell、Librispeech、WenetSpeech 等数据集和多种数据增强方法。可在 Windows、Linux 下训练与预测，并支持 Nvidia Jetson 开发板推理。提供预训练模型下载（含错误率指标）、模型导出、长语音预测、Web 部署、GUI 界面部署等方式；README 同时指向动态图新版项目 PPASR，本分支为静态图旧版本维护分支。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 Windows/Linux 训练与预测，支持 Nvidia Jetson 开发板推理
- 提供 AIShell/Librispeech/WenetSpeech 预训练模型及错误率指标
- 支持长语音预测、Web 部署、GUI 界面部署多种使用形式
- 支持多种数据增强方法

## 适用场景

- 训练自己的中文语音识别模型
- 使用预训练模型对音频文件做语音转文字
- 在 Jetson 开发板上部署离线语音识别
- 通过 Web 或 GUI 界面提供录音识别服务

## 场景标签

 · 领域:语音识别/深度学习

## 证据(README 行号)

> L8: DeepSpeech2是基于PaddlePaddle实现的端到端自动语音识别（ASR）引擎，其论文为《Baidu's Deep Speech 2 paper》 ，本项目同时还支持各种数据增强方法，以适应不同的使用场景。支持在Wind
> L47:  - 下载作者提供的模型或者训练模型，然后执行导出模型，使用`infer_path.py`预测音频，通过参数`--wav_path`指定需要预测的音频路径，完成语音识别，详情请查看模型部署。

## 星数曲线

```mermaid
xychart-beta
    title "yeyupiaoling/PaddlePaddle-DeepSpeech 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 762 --> 765
    line [763, 764, 764]
```

2026-10-18 763 → 2026-10-24 764（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `c8148a2a0322` · [字段定义](../../DATASET.md)*
