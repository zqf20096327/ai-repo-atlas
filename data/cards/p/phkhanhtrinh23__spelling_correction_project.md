# phkhanhtrinh23/spelling_correction_project

⭐ 20 · Python · 推送 2026-09-13 · [GitHub](https://github.com/phkhanhtrinh23/spelling_correction_project) · [官网](https://youtu.be/J-JnNqeN9zU) · 个人维护

**英文拼写纠错模型项目：Transformer 与 GPT-2 两种实现**

面向具备 Python/PyTorch 基础的开发者，提供两个版本的英文句子拼写纠错方案：v1 从零构建 Transformer Encoder-Decoder 模型，v2 在 Hugging Face GPT-2（gpt2-medium）上微调。输入为英文词典 english.txt，通过训练脚本训练后可运行评估脚本；v1 附带前后端 Web 演示（api.py）。README 记录了 v2 推理三处 bug 的修复过程，并在 200 句留出集上评测出 86.0% 精确匹配率；训练在 151,086 句 Tatoeba 风格数据上进行，4/20 epoch 后提前停止，作者指出继续训练可能提升准确率。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两个版本：从零构建的 Transformer Encoder-Decoder 与微调的 GPT-2
- v1 提供前后端 Web 演示（python api.py）
- 200 句留出集评测精确匹配率 86.0%
- README 记录 v2 推理三处 bug 的定位与修复（BOS token、左填充、max_new_tokens）

## 适用场景

- 学习 Transformer/GPT-2 在拼写纠错任务上的训练与评估流程
- 参考序列生成中 padding 与生成参数的常见错误修复方法
- 基于 v1 的 Web 演示体验拼写纠错效果

## 场景标签

`微调` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L7: My project is called **Spelling Correction**. This is a solution which helps a person correct a sentence with spelli
> L48:  - `spelling_correction_v1` is based on **Transformer Encoder-Decoder** model. It is fast in training and inference

## 星数曲线

```mermaid
xychart-beta
    title "phkhanhtrinh23/spelling_correction_project 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `953450f02fea` · [字段定义](../../DATASET.md)*
