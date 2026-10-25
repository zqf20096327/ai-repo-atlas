# ims-kdks/Learning-to-Parallel-Decoding

⭐ 37 · Python · MIT · 推送 2026-01-27 · [GitHub](https://github.com/ims-kdks/Learning-to-Parallel-Decoding) · [官网](https://ims-kdks.github.io/learning-to-parallel/) · 组织维护

**扩散语言模型可学习并行解码的推理加速研究与代码**

ICLR 2026 论文 Learning to Parallel: Accelerating Diffusion Large Language Models via Learnable Parallel Decoding 的官方代码库。方法包含两部分：训练一个过滤器 f_theta 模拟 Extreme Greedy Parallel 策略，在各解码步后选择 token 并决定是否重掩码；以及 [EoT] 终止符预测，在检测到结束符后丢弃其后的 token 以缩短输入长度。论文在 GSM8K/MATH/HumanEval/MBPP 上评测吞吐（最高加速 22.58 倍）与准确率。提供依赖安装、生成/评测脚本、训练数据生成与过滤器训练 notebook。

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

- 训练过滤器模拟 Extremely Greedy Parallel 策略决定 token 重掩码
- [EoT] 预测：检测到结束符后丢弃后续 token 以减少计算量
- 四个基准上报告 TPS、加速比与准确率三项指标
- 支持用 training.ipynb 在自有数据上训练新过滤器

## 适用场景

- 复现论文的加速解码实验与评测结果
- 在自有数据集上训练并部署解码过滤器
- 研究扩散语言模型的并行解码与推理加速方法

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L10: - [2026-01-26]: Our paper is accept by ICLR 2026.
> L18: Use a trained filter $f_\theta$ that simulate the Extremely Greedy Parallel strategy after each decoding step to se

## 星数曲线

```mermaid
xychart-beta
    title "ims-kdks/Learning-to-Parallel-Decoding 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-25 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `03d7e308579f` · [字段定义](../../DATASET.md)*
