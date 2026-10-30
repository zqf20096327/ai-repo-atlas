# rookiestar28/ComfyUI-TranslateGemma

⭐ 33 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/rookiestar28/ComfyUI-TranslateGemma) · 个人维护 · 中文 README

**在 ComfyUI 中运行 Google TranslateGemma 的翻译节点**

ComfyUI 自定义节点，封装 Google 开源的 TranslateGemma 翻译模型（基于 Gemma 3）：支持 55 种语言文本翻译、图像内文字的多模态翻译，可选 4B/12B/27B 模型规格。模型经 Hugging Face 门控下载（需接受 Gemma 条款并认证），支持共享模型根复用、设备覆盖（cpu/gpu:N）、bitsandbytes 可选量化（bnb-8bit/4bit 需 CUDA）、OpenCC 简繁转换（不加载模型）及长文本分段策略。面向 ComfyUI 用户，经 ComfyUI-Manager 或 git clone 安装，要求 Python 3.12/3.13 与 Transformers ≥4.57。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 55 种语言文本翻译与图像文字多模态翻译（两遍模式：先提取后翻译）
- 4B/12B/27B 三档模型规格与 bnb-8bit/4bit 可选量化（需 CUDA）
- OpenCC 简繁转换模式，无需加载模型
- 支持 ComfyUI 共享 LLM 模型根复用与手动离线下载

## 适用场景

- 在 ComfyUI 工作流中翻译文本或图像中的文字
- 受网络限制环境（如 HF 被阻断地区）手动下载模型离线使用
- 需要简繁转换的处理流水线

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L3: A ComfyUI integration for TranslateGemma — Google's open source translation model family built on Gemma 3. It suppor
> L39: - Text translation across 55 languages
> L43: - Optional image input: translate text found in images (multimodal)

## 星数曲线

```mermaid
xychart-beta
    title "rookiestar28/ComfyUI-TranslateGemma 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-30 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `f8dbef5cb49c` · [字段定义](../../DATASET.md)*
