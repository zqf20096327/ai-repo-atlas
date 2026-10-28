# muyexiuluo/ComfyUI-Muye-nodes

⭐ 95 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/muyexiuluo/ComfyUI-Muye-nodes) · 个人维护 · 中文 README

**ComfyUI 自定义节点集：图像反推提示词、面部处理与图像/遮罩/文本工具**

面向 ComfyUI 用户的自定义节点集合，覆盖音频转换、文件读写、图像混合与宫格拼接、遮罩编辑、文本操作、数学计算与尺寸选择等通用工具。核心功能包括基于 Qwen2.5-VL / Qwen3-VL / LLaVA 多模态模型的图像描述与提示词反推/扩写/校对节点（支持文本、单图、多图参考、视频序列帧四种推理模式，BF16/FP16/INT8/INT4 量化），以及基于 UniFace(ONNX) 的人脸检测、性别识别、智能裁剪与面部粘贴节点。通过 ComfyUI Manager 或 git clone 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Qwen2.5-VL / Qwen3-VL / LLaVA 的提示词反推节点，四种推理模式、支持量化与结果可复现
- UniFace(ONNX) 人脸检测、性别识别、多脸索引与智能旋转扶正
- 图像宫格拼接（最多 16 张自动布局）、遮罩编辑、批量文本替换等通用工具节点
- 模型加载后自动缓存，UniFace 权重首次运行自动下载

## 适用场景

- 为 LoRA 训练集批量生成图片 caption 或打标
- 多图交叉参考生成与校对提示词
- 工作流中做人脸检测、裁剪与贴回处理

## 场景标签

`提示工程` `人脸识别` `图像视频处理` · 领域:Agent 开发

## 证据(README 行号)

> L16: 基于 Qwen2.5-VL / Qwen3-VL / LLaVA 等多模态模型的图像描述与提示词处理节点。
> L24: 基于 Qwen3-VL / Qwen2.5-VL / LLaVA 的通用指令节点,支持四种推理模式:
> L166: 以下是一些我自己常用的一些节点分享,这些节点都是AI写的,全中文实现节点。

## 星数曲线

```mermaid
xychart-beta
    title "muyexiuluo/ComfyUI-Muye-nodes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 94 --> 96
    line [95, 95]
```

2026-10-18 95 → 2026-10-28 95（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `af20608cc0f8` · [字段定义](../../DATASET.md)*
