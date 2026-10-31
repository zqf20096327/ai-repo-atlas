# MagedSaeed/generate-sequences

⭐ 19 · Python · Apache-2.0 · 推送 2025-12-12 · [GitHub](https://github.com/MagedSaeed/generate-sequences) · [官网](https://magedsaeed.github.io/generate-sequences/) · 个人维护

**给开发者的 PyTorch 序列生成解码库：贪心与束搜索**

Python 库，为任意 PyTorch 架构（不限于 Hugging Face 模型）提供序列生成解码管线：用户实现 generation_forward 方法指定模型如何输出 logits，其余贪心搜索与束搜索流程由库标准化处理，支持 decoder-only 与 encoder-decoder 架构。提供采样、温度、top-p、top-k 等生成参数，可自定义解码配置并缓存编码器输出。通过 pip 安装，附单元测试与 Hugging Face 集成示例 notebook，采用 Apache 许可证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 贪心搜索与束搜索两种解码策略，支持自定义配置
- generation_forward 机制适配非 Hugging Face 的任意 PyTorch 模型
- 支持 decoder-only 与 encoder-decoder 架构，可缓存编码器输出
- 支持采样、温度、top-p、top-k 等生成方法

## 适用场景

- 为自研 PyTorch 模型接入贪心/束搜索解码
- 文本生成、语言建模、机器翻译任务的序列解码
- 替代受限的 Hugging Face generate 流程处理自定义架构

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: `generate-sequences` is a Python library for generating sequences from deep learning architectures with support for 
> L15: Hugging Face’s `model.generate` method is a great tool for generating sequences from LLMs. However, in order to use
> L55: from generate_sequences import GreedyGenerator, BeamSearchGenerator

## 星数曲线

```mermaid
xychart-beta
    title "MagedSaeed/generate-sequences 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `5fdf0128418b` · [字段定义](../../DATASET.md)*
