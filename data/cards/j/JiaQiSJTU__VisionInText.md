# JiaQiSJTU/VisionInText

⭐ 16 · Python · 推送 2026-04-07 · [GitHub](https://github.com/JiaQiSJTU/VisionInText) · 组织维护

**ASCII 艺术视觉感知基准：评测 LLM/MLLM 从字符识别概念**

ICLR2026 论文 ASCIIEval 的配套代码与数据仓库：以 ASCII 艺术为载体，构造 3,526 样本测试集（359 个概念、三级分类树）与 11,836 样本训练集 ASCIITune，把问题形式化为识别任务。支持本地脚本与 API 两种方式评测 LLM/MLLM，支持 text-only/image-only/both 输入模态，并提供微调脚本与 rationale 辅助微调方法。数据采用 CC BY NC 4.0 许可，仅限非商业研究用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 3,526 测试样本与 11,836 训练样本，三级分类树组织
- 支持本地运行与 API 两种评测路径，覆盖 LLM 与 MLLM
- MLLM 支持 text-only/image-only/both 三种输入模态评测
- 提供 rationale 辅助微调与 vision-focused 微调脚本

## 适用场景

- 评测我的模型对 ASCII 艺术的跨模态视觉感知能力
- 用 ASCIITune 微调提升模型字符视觉理解
- 对比开源与闭源模型在文本/图像模态下的表现

## 场景标签

`模型评测` `微调` · 领域:评测与运维

## 证据(README 行号)

> L1: [ICLR2026] ASCIIEval: Benchmarking Models' Visual Perception in Text Strings via ASCII Art
> L12: Perceiving visual semantics embedded within consecutive characters is a crucial yet under-explored capability for b

## 星数曲线

```mermaid
xychart-beta
    title "JiaQiSJTU/VisionInText 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `ff7cc4823b79` · [字段定义](../../DATASET.md)*
